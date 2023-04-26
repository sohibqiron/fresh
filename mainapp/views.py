from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee, Product,UserProfile
from .forms import  CreateEmployeeForm, CreateUserForm

# Create your views here.

def testPage(request):
    return render(request, 'mainapp/user_profeli.html')

def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('dashboard')
    
    context = {
        'form':form
    }

    return render(request, 'mainapp/registrations.html')
   
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password) 

        if user is not None: 
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username or password was incorrect")
        
    context = {

    }

    return render(request, 'mainapp/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login_user')

@login_required(login_url='login_user')
def user_profile(request):
    profiles = UserProfile.objects.all()
    context = {
        'username': request.user,
        'profiles': profiles
    }
        
    return render(request,'mainapp/user_profile.html',context)

@login_required(login_url='login_user')
def dashboard(request):
    return render(request,'mainapp/dashboard.html')

@login_required(login_url='login_user')
def employee_table(request):
    if request.method == "POST":
        q = request.POST.get("q")
        employees = Employee.objects.filter(full_name__contains=q)
    else:
        employees = Employee.objects.all()
        context = {
            'employees': employees,
        }
        return render(request,'mainapp/e_table.html',context)

@login_required(login_url='login_user')   
def product_table(request):
    products = Product.objects.all()
    contex = {
        'products': products,
    }
    return render(request,'mainapp/p_tables.html',contex)

@login_required(login_url='login_user')
def createEmployee(request):
    if request.user.is_superuser or request.user.is_staff:
        form = CreateEmployeeForm()
        if request.method == "POST":
            form = CreateEmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('e-table')
            else:
                form = CreateEmployeeForm()

        contex = {
            'form':form
        }
        return render(request, 'mainapp/e_create.html', contex)
    else:
        return redirect('e-table')

@login_required(login_url='login_user')
def updateEmployee(request,pk):
    if request.user.is_superuser or request.user.is_staff:
            employee = Employee.objects.get(id=pk)
            form = CreateEmployeeForm(instance=employee)
            if request.method == "POST":
                form = CreateEmployeeForm(request.POST,instance=employee)
                if form.is_valid():
                    form.save()
                    return redirect('e-table')
                
            context = {
                'form':form
            }
            return render(request, 'mainapp/e_create.html', context)
    else:
        return redirect('e-table')   

@login_required(login_url='login_user')
def daleteEmployee(request,pk):
    if request.user.is_superuser:
        employee = Employee.objects.get(id=pk)
        if request.method =="POST":
            employee.delete()
            return redirect('e-table')

        context = {
            'employee':employee
        }
        return render(request, 'mainapp/e_delete.html', context)
    else:
        return redirect('e-table') 


