from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV


urlpatterns = [
    # class-based views
    path('', BookmarkLV.as_view(), name='index'),
    # int 형의 primary key 가 붙으면 BookmarkDV로 넘겨줌
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]