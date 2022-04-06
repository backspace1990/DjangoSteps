from django.shortcuts import render, HttpResponse

# Create your views here.
# Icinde python fonksiyonlari yazacagimiz
# yerdir.
# Kullanicinin istekte bulunmasi ve web 
# sitesinin bu isteklere cevap vermesi 
# burada katmanda yazilan fonksiyonlarla
# saglanir.
# tr karsiligi goruntu demektir view

# Migrations : Uygulamanin veritabanini tutan yerdir. 

def post_home(request):
    return HttpResponse('<b><h1>Burasi Post Home</h1></b>')


def post_index(request):
    return HttpResponse('<b><h1>Burasi Post index</h1></b>')


def post_detail(request):
    return HttpResponse('<b><h1>Burasi Post detail</h1></b>')


def post_create(request):
    return HttpResponse('<b><h1>Burasi Post create</h1></b>')


def post_update(request):
    return HttpResponse('<b><h1>Burasi Post update</h1></b>')


def post_delete(request):
    return HttpResponse('<b><h1>Burasi Post delete</h1></b>')