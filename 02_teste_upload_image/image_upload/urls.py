"""
URL configuration for image_upload project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from image_app.views import hotel_image_view, success, index

from image_app.views import display_hotel_images, hotel_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image_upload', hotel_image_view, name='image_upload'),
    path('success', success, name='success'),
    path('index', index, name='teste'),
    path('hotel_images', display_hotel_images, name='hotel_images'),
    path('delete/<int:id>/', hotel_delete, name='deletar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
