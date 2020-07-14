"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    # 어디로 가야하는지 경로 지정하는 것
    path('admin/', admin.site.urls),

    # class-based views
    path('bookmark/', BookmarkLV.as_view(), name='index'),
    # int 형의 primary key 가 붙으면 BookmarkDV로 넘겨줌
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]

