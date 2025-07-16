from django.urls import path, include
from .views import authView, home, StudentViewSet, student_form_page
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students',StudentViewSet)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="signup"),
    path("home/", home, name="home"),
    path("", include(router.urls)),
    path("add-student-form/",student_form_page, name = 'student-form'),
    # path("login/", auth_views.LoginView.as_view(), name="login"),  # Add this line
]