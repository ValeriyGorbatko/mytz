from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Comment


class TreeListView(TemplateView):

    template_name = 'comments/base.html'

    def get_context_data(self, **kwargs):
        context = super(TreeListView, self).get_context_data(**kwargs)
        context['nodes'] = Comment.objects.all
        return context

    def post(self, request):
        if request.POST.get('parent'):
            parent = Comment.objects.get(name=request.POST.get('parent'))
            Comment.objects.create(name=request.POST.get('comment'), parent=parent)
        else:
            Comment.objects.create(name=request.POST.get('area'))
        return render(request, self.template_name, self.get_context_data())

