from django.contrib import admin
from django.urls import path, include
from homeApp.views import homeapp_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeapp_view, name='Welcome'),
    path('post/', include('post.urls'))
]
