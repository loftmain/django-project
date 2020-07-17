from django.urls import path
from photo import views



app_name = 'photo'
urlpatterns = [
    # Example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    path('album', views.AlbumLV.as_view(), name='album_list'),

    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),

    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),

    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),

    path('album/update/<int:pk>/', views.AlbumPhotoUV.as_view(), name='album_update'),

    path('album/delete/<int:pk>/', views.AlbumDelV.as_view(), name='album_delete'),

    path('photo/add/', views.PhotoCV.as_view(), name='photo_add'),

    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'),

    path('photo/update/<int:pk>/', views.PhotoUV.as_view(), name='photo_update'),

    path('photo/delete/<int:pk>/', views.PhotoDelV.as_view(), name='photo_delete'),

]