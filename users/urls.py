from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="users-page"),
    path("login/", views.LoginPageView.as_view(), name="login-page"),
    path("register/", views.RegisterPageView.as_view(), name="register-page"),
    path("<int:id>", views.UserDetailView.as_view(), name="user-detail"),
    path("settings/<int:id>/", views.UserSettingsView.as_view(), name="user-settings"),
]
