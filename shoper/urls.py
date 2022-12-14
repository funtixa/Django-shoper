from django.conf import settings
from django.conf.urls.static import static
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from core.views import frontPage,about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about,name='about'),
    
    path('', include('userprofile.urls')),
    path('', include('store.urls')),
    path('',frontPage,name='frontpage'),


    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #django can read images from media folder
