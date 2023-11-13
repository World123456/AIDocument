from django.shortcuts import render

def hello(request):
    context = {}
    return render(request, 'search_form.html', context)