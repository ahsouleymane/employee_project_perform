from django.urls import path

from .migrations.views import create,update,delete,home,register
from django.contrib.auth import views as auth_views
from django.contrib.auth import views

urlpatterns = [

    path('', home.home_page, name='home'), # home page

    path('create/', create.employee_create, name='employee_insert'), # get and post req. for insert operations

    path('update/<int:id>/', update.employee_update, name='employee_update'), # get and post req. for update operations

    path('delete/<int:id>/', delete.employee_delete, name='employee_delete'),

    path('list/',create.employee_list, name='employee_list'), # get req. to retrieve and display all records

    path('register/',register.register_account, name='register_account'),

    path('login/', auth_views.LoginView.as_view(template_name='employee_register/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='employee_register/logout.html'), name='logout'),

    path('reset_password/', 
        views.PasswordResetView.as_view(template_name='employee_register/reset_password.html'), 
            name='reset_password'),
    path('reset_password_send/', 
        views.PasswordResetDoneView.as_view(template_name='employee_register/reset_password_sent.html'), 
            name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        views.PasswordResetConfirmView.as_view(template_name='employee_register/reset_password_form.html'), 
            name='password_reset_confirm'),
    path('reset_password_complete/', 
        views.PasswordResetCompleteView.as_view(template_name='employee_register/reset_password_done.html'), 
            name='password_reset_complete'),
]
