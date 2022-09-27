from django.urls import path

from app.api import views as api_views

urlpatterns = [
    path("items/", api_views.HelloWorldView.as_view(), name="hello_world_items",),
]

