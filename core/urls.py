from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # authentication routing
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Registration Routes
    path('register/', views.customer_signup_view, name='signup'),
    path('register/seller/', views.seller_signup_view, name='seller_signup'),
]