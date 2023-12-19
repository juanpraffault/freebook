from django.shortcuts import render 

def index_v(request):
    return render(request, 'index.html', {})

def leftsb_v(request):
    return render(request, 'left-sidebar.html', {})

def rightsb_v(request):
    return render(request, 'right-sidebar.html', {})

def nosb_v(request):
    return render(request, 'no-sidebar.html', {})