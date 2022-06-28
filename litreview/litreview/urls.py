"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
import feeds.views as feeds
import authentication.views as auth


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", feeds.home, name="home"),
    path("", LoginView.as_view(
        template_name="authentication/login.html", redirect_authenticated_user=True
    ), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("password_change/", PasswordChangeView.as_view(
        template_name="authentication/password_change.html"
    ), name="password-change"),
    path("password_change_done/", PasswordChangeDoneView.as_view(
        template_name="authentication/password_change_done.html"
    ), name="password-change-done"),
    path("signup/", auth.signup_page, name="signup")
]
