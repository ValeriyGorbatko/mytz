from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from .models import Comment
from .forms import TreeForm


class TreeListView(generic.ListView):

    template_name = 'comments/base.html'
    model = Comment

    def get_context_data(self, **kwargs):
        context = super(TreeListView, self).get_context_data(**kwargs)
        context['form'] = TreeForm()
        return context


class ParentCreateView(generic.CreateView):

    model = Comment
    template_name = 'comments/base.html'
    form_class = TreeForm
    success_url = reverse_lazy('tree_list')
    
    def post(self, request, *args, **kwargs):
        parent = request.POST.get('parent')
        if parent:
            name = request.POST.get('name')
            parent = self.model.objects.get(name=parent)
            Comment.objects.create(name=name, parent=parent)
            return HttpResponseRedirect('/')
        return super(ParentCreateView, self).post(request)

