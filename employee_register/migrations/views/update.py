from django.shortcuts import render,redirect
from ...forms import EmployeeForm
from ...models import Employee
from django.contrib.auth.decorators import login_required 

@login_required(login_url='/employee/login/')
def employee_update(request, id=0):

    if request.method == "GET":
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html",{'form':form})
    else:
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST, instance=employee)

    if form.is_valid():
        form.save()
        
    return redirect('/employee/list')