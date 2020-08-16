from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [


    path('', views.login, name='login_page'),
    path('login_validation/', views.login_validation, name="login_validation"),
    path('create_entry/', views.create_entry, name="create_entry"),
    path('create_entry_form/', views.create_entry_form, name="create_entry_form"),
    path('view_entry/', views.view_entry, name="view_entry"),
    path('delete_entry/<int:id>', views.delete_income, name='delete_entry'),
    path('log_out/', views.log_out, name='log_out'),

    ]
