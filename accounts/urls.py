from django.urls import path
from . import views

urlpatterns = [
    # Placeholder / dummy pages
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]