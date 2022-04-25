from django.urls import path
from .migrations.views import create,update,delete

urlpatterns = [
    path('', create.employee_create, name='employee_insert'), # get and post req. for insert operations
    path('update/<int:id>/', update.employee_update, name='employee_update'), # get and post req. for update operations
    path('delete/<int:id>/', delete.employee_delete, name='employee_delete'),
    path('list/',create.employee_list, name='employee_list'), # get req. to retrieve and display all records
]