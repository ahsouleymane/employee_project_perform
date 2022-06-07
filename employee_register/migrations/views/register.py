from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from ...forms import UserForm
from django.contrib import messages

def register_account(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été creé avec succès !!!")
            return redirect('login')
        else:
            messages.error(request, form.errors)
    return render(request, "employee_register/register_account.html", {'form': form})
