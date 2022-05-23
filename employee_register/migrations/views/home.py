from django.shortcuts import render
from ...forms import EmployeeForm
from django.contrib.auth.decorators import login_required 

@login_required(login_url='login/')
def home_page(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, "employee_register/base.html",{'form':form})
