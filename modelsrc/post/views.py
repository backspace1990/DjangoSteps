from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect

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
from .forms import PostForm
from django.contrib import messages


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
    #form = PostForm(request.POST)
    #context = {
    #    'form': form,
    #}
    #if request.method == "POST":
        #print(request.POST)
    #if request.method == "POST": #1.YONTEMMMMMMM
    #    title = request.POST.get('title')
    #    content = request.POST.get('content')
    #    Post.objects.create(title=title, content=content)

    #---------Iyi yontem 1 ---------
    #if request.method == "POST":
    #    #formdan gelen bilgileri kaydet
    #    form = PostForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #else:
    #    #formu kullaniciya goster
    #    form = PostForm()
    #
    #context = {
    #    'form': form,
    #}
    #---------------------Iyi yontem 1 sonu
    #---------Iyi yontem2  ---------
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Basarili bir post olusturdunuz')
        return HttpResponseRedirect(post.get_absolute_url())
    
    context = {
        'form': form,
    }
    #---------------------Iyi yontem 2 sonu
    return render(request, 'post/form.html', context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Postu basariyla guncellediniz')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/update.html', context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')


