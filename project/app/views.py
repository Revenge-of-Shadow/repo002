from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request, "base.html")
def app0(request):
    return render(request, "base0.html")
