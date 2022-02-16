from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('main.urls', namespace='main')),
    prefix_default_language=False,
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.error_404_view'
