from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogEntru


class BlogEntruCreateView(CreateView):
    model = BlogEntru
    fields = ('title', 'preview', 'creation_date',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogEntruUpdateView(UpdateView):
    model = BlogEntru
    fields = ('title', 'preview', 'content', 'creation_date',)
    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogEntruListView(ListView):
    model = BlogEntru

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_attribute=True)

        return queryset


class BlogEntruDetailView(DetailView):
    model = BlogEntru

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()

        return self.object


class BlogEntruDeleteView(DeleteView):
    model = BlogEntru
    success_url = reverse_lazy('blog:list')
