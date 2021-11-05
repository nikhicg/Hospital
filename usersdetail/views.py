from django.db.models import fields
from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm
from django .views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.http import JsonResponse


# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'usersdetail/register.html'
    success_url = '/login'


class DoctorListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'usersdetail/view_profile.html'
    context_object_name = 'doctor'
    paginate_by = 3

    def get_queryset(self):
        return CustomUser.objects.filter(type_user='Doctor')


@login_required()
def autocompleteModel(request):
    if 'term' in request.GET:
        search_qs = CustomUser.objects.filter(
            username__icontains=request.GET.get('term'))
        results = []
        for r in search_qs:
            if r.type_user == 'Doctor':
                results.append(r.username)
        print(results)
        return JsonResponse(results, safe=False)
    else:
        print(request.POST)
        search_qs = CustomUser.objects.filter(
            username=request.POST.get('doctor_name'))
        doctor_name = []
        for i in search_qs:
            if i.type_user == 'Doctor':
                doctor_name.append(i)
        context = {'name': doctor_name, 'hii': '1'}
        return render(request, 'usersdetail/view_profile.html', context)


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST,  request.FILES, instance=request.user)
        if u_form.is_valid() and u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        context = {
            'u_form': u_form,
        }
    return render(request, 'usersdetail/profile.html', context)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'usersdetail/profile_detail.html'
    context_object_name = 'doctor_name'
