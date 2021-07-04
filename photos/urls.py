from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),
    url(r'^photo/', views.viewPhoto, name='view_photo'),
    url(r'^location/', views.locatePhoto, name='locate_photo'),
]
