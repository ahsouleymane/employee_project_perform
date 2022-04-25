from functools import wraps
from django.shortcuts import render,redirect
from ...forms import EmployeeForm
from ...models import Employee
import time

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


def timer(func):
    """fonction d'assistance pour estimer le temps d'exécution de la vue"""

    @wraps(func)  # Utilisé pour copier les métadonnées func
    def wrapper(*args, **kwargs):
        # Enregistrer l'heure de début
        start = time.time_ns()

        # Execution de la fonction
        result = func(*args, **kwargs)
        
        duration = (time.time_ns() - start)

        # Sortie du temps d'execution sur la console
        print("\n")

        print(bcolors.FAIL + "" + 'view {} takes {} ns'.format(func.__name__, duration) + "" + bcolors.RESET)

        print("\n")

        return result
    return wrapper


# Create your views here.

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, "employee_register/employee_list.html",context)

# la fonction ci-dessous permet de faire 1000 enregistrements dans la BD


@timer
def employee_create(request):
    
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, "employee_register/employee_form.html",{'form':form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/employee/list')
