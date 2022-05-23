from django.urls import path
from .migrations.views import create,update,delete,home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home.home_page, name='home'), # home page
    path('create/', create.employee_create, name='employee_insert'), # get and post req. for insert operations
    path('update/<int:id>/', update.employee_update, name='employee_update'), # get and post req. for update operations
    path('delete/<int:id>/', delete.employee_delete, name='employee_delete'),
    path('list/',create.employee_list, name='employee_list'), # get req. to retrieve and display all records
    path('register/',create.employee_create_account, name='register_account'),
    path('login/', auth_views.LoginView.as_view(template_name='employee_register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='employee_register/logout.html'), name='logout'),
]
