from django.urls import path
from .views import register_view, login_view, logout_view, activate_view, forgot_password, create_new_password

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("activate/", activate_view, name='activate'),
    path("create-new-password/", create_new_password, name='new_password'),
    path("forgot-password/", forgot_password, name="forgot_password")
]
