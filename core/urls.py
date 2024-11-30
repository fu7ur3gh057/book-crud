from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from core.settings import API_URL, APPS_ROOT

schema_view = get_schema_view(
    openapi.Info(
        title="Milligram Server API",
        default_version="v1",
        description="Distribution Message API",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="milligram@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    # url="https://milligram.az/",
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{API_URL}/books/", include(f"{APPS_ROOT}.books.api.urls")),
    # Swagger
    path(
        "swagger<str:format>",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
