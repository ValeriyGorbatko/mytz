from django.http import HttpResponseRedirect
from django.views import generic
from .models import Comment


class TreeListView(generic.ListView):

    template_name = 'comments/content.html'
    model = Comment
    
    def post(self, request, *args, **kwargs):
        parent_id = request.POST.get('parent')
        comment = self.model(name=request.POST.get('name'), user=request.user)
        if parent_id:
            comment.parent = self.model.objects.get(id=parent_id)
        comment.save()
        return HttpResponseRedirect('/')


