
from re import template
from django.urls import path
from client_lib import views
from django.views.generic import TemplateView

app_name = 'client_lib'
urlpatterns = [
    path('user_login', views.user_login , name='user_login'),
    path('login',views.login,name='login'),
    path('admin/',views.admin_redirect, name='admin_redirect'), 
    path('user_view',views.user_view,name='user_view'),
    path(r'borrowed/<int:id>',views.borrowed,name='borrowed'),
    path('logout',views.logout,name='logout'),
    path('borrowed_book',views.borrowed_book,name='borrowed_book'),
    path(r'return_book/<str:title>',views.return_book,name='return_book'),
    path('user_signup_page',views.user_signup_page,name='user_signup_page'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('delete_account',views.delete_account,name='delete_account'),
]
