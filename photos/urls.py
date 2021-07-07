from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),
    url(r'^photo/<str:pk>', views.viewPhoto, name= 'photo'),
    url(r'^location/', views.locatePhoto, name='location'),
    url(r'^search/', views.search_image, name='search_image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

