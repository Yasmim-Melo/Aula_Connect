from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('', views.inicial, name='inicial'),
    path('signup/', views.registrar, name='signup'),
    path('meus-planos/', views.meus_planos, name='meus_planos'),
    path('modelos/', views.modelos_planos, name='modelos_planos'),
]