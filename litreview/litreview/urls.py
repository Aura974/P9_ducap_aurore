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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
import feeds.views as feeds
import authentication.views as auth
from authentication.forms import CustomLoginForm
import followers.views as followers


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", feeds.home, name="home"),
    path("posts/", feeds.posts, name="posts"),
    path("", LoginView.as_view(
        template_name="authentication/login.html",
        authentication_form=CustomLoginForm,
        redirect_authenticated_user=True
    ), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("password_change/", PasswordChangeView.as_view(
        template_name="authentication/password_change.html"
    ), name="password-change"),
    path("password_change_done/", PasswordChangeDoneView.as_view(
        template_name="authentication/password_change_done.html"
    ), name="password-change-done"),
    path("signup/", auth.signup_page, name="signup"),
    path("create_ticket/", feeds.create_ticket, name="create_ticket"),
    path("create_review/", feeds.create_review, name="create_review"),
    path("create_answer_review/<int:ticket_id>/", feeds.create_answer_review, name="create_answer_review"),
    path("posts/edit/<str:content_type>/<int:content_id>", feeds.edit_content, name="edit_content"),
    path("posts/delete/<str:content_type>/<int:content_id>", feeds.delete_post, name="delete"),
    path("follow_users/", followers.follow_users, name="follow_users")
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
