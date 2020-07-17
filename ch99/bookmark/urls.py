from django.urls import path
#from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views


app_name = 'bookmark'

urlpatterns = [
    # class-based views
    path('', views.BookmarkLV.as_view(), name='index'),
    # int 형의 primary key 가 붙으면 BookmarkDV로 넘겨줌
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),

    # Exmaple: /bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name='add',),

    path('change/', views.BookmarkChangeLV.as_view(), name='change',),

    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),

    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete',),
]