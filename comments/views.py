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
    
    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous():
            return HttpResponseRedirect('/')
        parent_id = request.POST.get('parent')
        name = request.POST.get('name')
        parent = None
        if parent_id:
            parent = self.model.objects.get(id=parent_id)
        Comment.objects.create(name=name, parent=parent, user=request.user)
        return HttpResponseRedirect('/')


