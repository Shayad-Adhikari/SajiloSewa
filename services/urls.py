from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage / service listing
    path('gigs/', views.gig_list, name='gig_list'),
    path('gigs/<int:id>/', views.gig_detail, name='gig_detail'),
    path('gigs/create/', views.create_gig, name='create_gig'),
]