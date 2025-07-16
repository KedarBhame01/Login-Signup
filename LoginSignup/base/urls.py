from django.urls import path, include
from .views import authView, home, StudentViewSet
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students',StudentViewSet)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="signup"),
    path("home/", home, name="home"),
    path("", include(router.urls)),
    # path("login/", auth_views.LoginView.as_view(), name="login"),  # Add this line
]