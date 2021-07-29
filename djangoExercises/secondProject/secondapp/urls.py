from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_request, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_request, name="logout"),
    path("blog/create/", views.createBlog, name="createblog"),
    path("blog/<pk>/update/", views.UpdateBlog.as_view(), name="updateblog"),
    path("blog/<pk>/delete/", views.DeleteBlog.as_view(), name="deleteblog"),
]