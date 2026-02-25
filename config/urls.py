from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from slider.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("filer/", include("filer.urls")),
    path("", home, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
