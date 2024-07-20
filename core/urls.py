from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('class_/', views.class_, name='class_'),
    path('schedule/', views.schedule, name='schedule'),
    path('contact/', views.contact, name='contact'),
    path('footer/', views.footer, name='footer'),
    path('modal/', views.modal, name='modal'),
]
