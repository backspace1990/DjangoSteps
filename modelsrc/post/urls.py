from django.urls import path
from post import views

# Baska uygulamalarda index,detail vb.
# URL falan varsa hata cikabilir. 
# Bunu onlemek icin alttaki 
# isimlendirme kullanilir.
app_name = 'post'

urlpatterns = [
    path('index/', views.post_index, name='index'),
    path('detail/<int:id>/', views.post_detail, name="detail"),
    path('create/', views.post_create, name='create'),
    path('<int:id>/update/', views.post_update, name='update'),
    path('delete/', views.post_delete, name='delete'),
]