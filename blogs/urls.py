from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blogdetail/', views.blogdetail, name='blogdetail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('termsofconditions/', views.termsofconditions, name='termsofconditions'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('helpcenter/', views.faq, name='faq'),
]