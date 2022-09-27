from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()

from app.api import views as api_views

urlpatterns = [
    path("items/", api_views.HelloWorldView.as_view(), name="hello_world_items",),
]


urlpatterns = [
    path("", include(router.urls)),  # default view with API URLS
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("hello-world/", include("app.api.urls")),
]

