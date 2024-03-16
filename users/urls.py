from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="users-page"),
    path("login/", views.LoginPageView.as_view(), name="login-page"),
    path("register/", views.RegisterPageView.as_view(), name="register-page"),
    path("<int:id>", views.UserDetailView.as_view(), name="user-detail"),
    path("settings/<int:id>/", views.UserSettingsView.as_view(), name="user-settings"),
    path("logout/", views.LogOutView.as_view(), name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
