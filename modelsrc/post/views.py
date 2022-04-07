from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
# Icinde python fonksiyonlari yazacagimiz
# yerdir.
# Kullanicinin istekte bulunmasi ve web 
# sitesinin bu isteklere cevap vermesi 
# burada katmanda yazilan fonksiyonlarla
# saglanir.
# tr karsiligi goruntu demektir view

# Migrations : Uygulamanin veritabanini tutan yerdir. 
from .models import Post


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post':post
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    return HttpResponse('<b><h1>Burasi Post create</h1></b>')


def post_update(request):
    return HttpResponse('<b><h1>Burasi Post update</h1></b>')


def post_delete(request):
    return HttpResponse('<b><h1>Burasi Post delete</h1></b>')