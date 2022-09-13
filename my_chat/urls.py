from django.urls import path

from . import views




urlpatterns = [
    path('', views.test_chat, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('/del<int:id>/', views.delete_room, name='delete_room'),
]