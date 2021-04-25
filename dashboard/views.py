from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        'index.html'
    )

def write(request):
    return render(
        request,
        'write/write.html'
    )

def read(request):
    return render(
        request,
        'read/read.html'
    )