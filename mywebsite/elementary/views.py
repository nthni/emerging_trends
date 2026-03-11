from django.shortcuts import render

def index(request):
        return render(request, 'elementary.html')

def about_elementary(request):
        return render(request, 'about_elementary.html')