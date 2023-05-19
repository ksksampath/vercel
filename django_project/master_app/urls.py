from master_app import views
from django.urls import path
urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    path('create_page', views.create_page, name='create_page'),
    path('create_account', views.create_account, name='create_account'),
]