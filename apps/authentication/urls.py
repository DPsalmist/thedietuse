from django.urls import path
from .views import login_view, register_user, register_teacher
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('teacher/register/', register_teacher, name="register-teacher"),
    path("logout/", LogoutView.as_view(), name="logout")
]
