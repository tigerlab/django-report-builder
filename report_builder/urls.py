from django.urls import path
from django.urls import re_path, include
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import routers
from . import views
from .api import views as api_views
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'reports', api_views.ReportViewSet)
router.register(r'report', api_views.ReportNestedViewSet)
router.register(r'formats', api_views.FormatViewSet)
router.register(r'filterfields', api_views.FilterFieldViewSet)
router.register(r'contenttypes', api_views.ContentTypeViewSet)

urlpatterns = [
    path('report/<int:pk>/download_file/', views.DownloadFileView.as_view(), name="report_download_file"),
    path('report/<int:pk>/download_file/<path:filetype>/', views.DownloadFileView.as_view(), name="report_download_file"),
    path('report/<int:pk>/check_status/<path:task_id>/', views.check_status, name="report_check_status"),
    path('report/<int:pk>/add_star/', views.ajax_add_star, name="ajax_add_star"),
    path('report/<int:pk>/create_copy/', views.create_copy, name="report_builder_create_copy"),
    path('export_to_report/', views.ExportToReport.as_view(), name="export_to_report"),
    path('api/', include(router.urls)),
    re_path(r'^api/config/', api_views.ConfigView.as_view()),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/related_fields', staff_member_required(api_views.RelatedFieldsView.as_view()), name="related_fields"),
    re_path(r'^api/fields', staff_member_required(api_views.FieldsView.as_view()), name="fields"),
    re_path(r'^api/report/(?P<report_id>\w+)/generate/', staff_member_required(api_views.GenerateReport.as_view()), name="generate_report"),
    path('api/report/<int:pk>/download_file/<path:filetype>/', views.DownloadFileView.as_view(), name="report_download_file"),
    path('api/report/<int:pk>/check_status/<path:task_id>/', views.check_status, name="report_check_status"),
    path('report/<int:pk>/', views.ReportSPAView.as_view(), name="report_update_view"),
]

if not hasattr(settings, 'REPORT_BUILDER_FRONTEND') or settings.REPORT_BUILDER_FRONTEND:
    urlpatterns += [
        re_path(r'^', staff_member_required(views.ReportSPAView.as_view()), name="report_builder"),
    ]
