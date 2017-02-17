from django.shortcuts import render

# Create your views here.
def reg_list(request):
    return render(request, 'blog/reg_list.html', {})
