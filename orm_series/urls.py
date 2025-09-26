from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + debug_toolbar_urls() + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
