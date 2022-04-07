from django.urls import path
from post import views


urlpatterns = [
    path('index/', views.post_index),
    path('detail/<int:id>/', views.post_detail),
    path('create/', views.post_create),
    path('update/', views.post_update),
    path('delete/', views.post_delete),
]