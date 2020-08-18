"""facein_api URL Configuration"""
from django.conf.urls.i18n import i18n_patterns
from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from moves.views import GetCameras
from moves.views import GetCompaniesView
from .admin import admin_site
from .admin import main_admin_site

urlpatterns = [path('api/profiles/', include('profiles.urls', namespace='profiles')),
               path('api/moves/<int:company_id>/cameras', GetCameras.as_view(),
                    name='company-cameras'),
               path('api/companies/', GetCompaniesView.as_view(),
                    name='companies'),
               path('i18n/', include('django.conf.urls.i18n')),
               ]
urlpatterns += i18n_patterns(path('superadmin/', main_admin_site.urls),
                             prefix_default_language='ru')
urlpatterns += i18n_patterns(path('admin/', admin_site.urls), prefix_default_language='ru')

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns += [
    path('docs/', schema_view.with_ui(cache_timeout=0), name="documentation"),
]
