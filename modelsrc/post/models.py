from django.db import models

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
    publishing_date = models.DateTimeField(verbose_name='Yayimlanma Tarihi')

#return f"/post/detail/{self.id}/"
#return "/post/index/"
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})
    
    def get_index(self):
        return reverse('index')