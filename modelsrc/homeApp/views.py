from django.shortcuts import render, HttpResponse

# Create your views here.
def homeapp_view(request):
    return HttpResponse('<b><h1>Hosgeldiniz</h1></b>')