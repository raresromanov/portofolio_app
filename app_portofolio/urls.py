from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('aboutme/',views.aboutme_page, name='aboutme'),
    path('contact/', views.contact_page, name='contact'),
    path('portofolio/',views.portofolio_page, name='portofolio'),
    path('<slug:slug>', views.post_detail, name='post_detail')
]