from django.shortcuts import redirect
from ...models import Employee
from django.contrib.auth.decorators import login_required 

@login_required(login_url='/employee/login/')
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
