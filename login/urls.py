from django.urls import path
from login.views import login, register, recuperacao, plataforma, reset_password
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('recuperacao/', recuperacao, name='recuperacao'),
    path('plataforma/', plataforma, name='plataforma'),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]