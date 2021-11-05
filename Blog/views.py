from django.shortcuts import render
from .models import Post
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from usersdetail.models import CustomUser
from django.http import JsonResponse


def autocompleteModel(request):
    if 'term' in request.GET:
        search_qs = Post.objects.filter(
            title__icontains=request.GET.get('term'))
        results = []
        for r in search_qs:
            results.append(r.title)
        return JsonResponse(results, safe=False)
    else:
        print(request.POST)
        search_qs = Post.objects.filter(
            title=request.POST.get('your_name'))
        context = {'posts': search_qs, 'hii': '1'}
        return render(request, 'Blog/home.html', context)
    return render(request, 'Blog/home.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(set_as_draft=False)


class FieldPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(category=self.kwargs.get('slug'))


class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user_draft = []
        u = Post.objects.filter(author=self.request.user)
        for i in u:
            if i.set_as_draft:
                user_draft.append(i)
        return user_draft


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'image', 'category', 'summary',
              'content', 'set_as_draft']
    success_url = '/'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        u = CustomUser.objects.get(username=self.request.user)
        if u.type_user == 'Doctor':
            return True
        return False


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'category', 'summary',
              'content', 'set_as_draft']
    success_url = '/'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
