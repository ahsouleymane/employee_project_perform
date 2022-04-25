from django.shortcuts import redirect
from ...models import Employee

def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
