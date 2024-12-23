from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi

from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_info = openapi.Info(
    title="test API",
    default_version="v1",
)
schema_view = get_schema_view(
    schema_info,
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('', include('users.urls'), name='users'),
    path('admin/', admin.site.urls),
    re_path("swagger(?P<format>\.json|\.yaml)/$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

]
