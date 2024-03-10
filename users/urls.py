from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="users-page"),
    path("login/", views.LoginPageView.as_view(), name="login-page"),
    path("register/", views.RegisterPageView.as_view(), name="register-page"),
]
