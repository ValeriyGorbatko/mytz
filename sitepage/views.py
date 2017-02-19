from django.shortcuts import render


def reg_list(request):
    return render(request, 'sitepage/reg_list.html', {})
