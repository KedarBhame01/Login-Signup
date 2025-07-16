from django.urls import path, include
from .views import authView, home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="signup"),
    path("", home, name="home"),
    # path("login/", auth_views.LoginView.as_view(), name="login"),  # Add this line
]