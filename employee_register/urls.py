from django.urls import path

from .migrations.views import create
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Employee

    path('create/', create.employee_create, name='employee_insert'), # get and post req. for insert operations

    path('list/',create.employee_list, name='employee_list'), # get req. to retrieve and display all records

    # Etudiant

    path('create1/', create.etudiant_create, name='etudiant_insert'), # get and post req. for insert operations

    path('list1/',create.etudiant_list, name='etudiant_list'),




    path('login/', auth_views.LoginView.as_view(template_name='employee_register/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='employee_register/logout.html'), name='logout'),

]
