from django.db import models
from django.shortcuts import redirect

# Create your models here.
# Veritabani nesnelerinin olusturdugumuz 
# ve sorgulama yaptigimiz katmandir. 
# Ornegin post(gonderi) modeli tanimlanacaksa :
#   . Baslik
#   . Tarih
#   . Icerik
#   . Resim vb.
# bilgilere ihtiyac vardir. Model katmani bu bilgilerin 
# ve daha fazlasinin tanimlandigi yerdir. 
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name='Baslik')
    content = models.TextField(verbose_name='Icerik')
    publishing_date = models.DateTimeField(verbose_name='Yayimlanma Tarihi', auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True)


#return f"/post/detail/{self.id}/"
#return "/post/index/"
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})
    
    def get_index(self):
        return reverse('post:index')
    
    def get_update_post(self):
        return reverse('post:update', kwargs={'id': self.id})
    
    def get_delete_post(self):
        return reverse('post:delete', kwargs={'id': self.id})
    
    class Meta:
        ordering = ["publishing_date"] #burada Meta clasimizi publishing_date ye bagli kildik. yani en eskiden simdiye,  -publishing_date yazinca tam tersi
        #ordering = ["-id"]
        #ordering = ["publishing_date", "id"] # boyle olunca tarihi ayni olanlarin id alanlarina bakilir