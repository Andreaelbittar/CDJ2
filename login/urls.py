from django.urls import path
from . import views

app_name= 'login'

urlpatterns = [
    path("panel/", views.panel_admin, name="panel_admin"),
    path("create_post/", views.create_post, name="create_post"),
    path("delete_post/<int:post_id>", views.delete_post, name="delete_post")
]