from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form_view, name='student_form'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
]
