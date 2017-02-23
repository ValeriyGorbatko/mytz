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
        #Comment.objects.create(name=request.POST.get('area'))
        print(request.POST)
        return render(request, self.template_name, self.get_context_data())

