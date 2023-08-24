from django.urls import include, path, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('report_builder/', include('report_builder_scheduled.urls')),
    path('report_builder/', include('report_builder.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
