from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm
from django .views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'usersdetail/register.html'
    success_url = '/login'


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
