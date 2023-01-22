from django.contrib import admin
from django.urls import path

from . import settings
from django.conf.urls.static import static

from homepage.views import homepage_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', homepage_view, name='homepage')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
