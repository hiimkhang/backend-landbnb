from django.urls import path, include
from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
