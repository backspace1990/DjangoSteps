from django.contrib import admin

# Register your models here.
# Yonetim paneliyle ilgili 
# ayarlarin bulundugu yerdir.
# Bir model olusturulunca modelin 
# yonetim arayuzunu saglamak icin admin 
# dosyasinda tanimlanmasi lazim.
# Uygulama ile ilgili ayarlarin 
# bulundugu yer.
#from .models import Post
from post.models import Post


admin.site.register(Post)