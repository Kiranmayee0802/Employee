from audioop import reverse
# from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AttendanceForm,LoginForm

from empapp.models import Attendance, Company, Employee, Login
from django.contrib import messages



# Create your views here.

def index(request):
    return render(request,'empapp/index.html')

def addemp(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        address = request.POST['address']
        phno = request.POST['phno']
        email = request.POST['email']
      
        designation = request.POST['designation']
        doj = request.POST['doj']
        salary = request.POST['salary']
        
        emp_obj = Employee.objects.create(fname=fname,lname=lname,dob=dob,address=address,phno=phno,email=email,designation=designation,doj=doj,salary=salary)
        emp_obj.save()

        return redirect('employee_list')
    return render(request, 'empapp/addemp.html')


def employee_list(request):
      emp_data = Employee.objects.filter()
      d = {'Employee':emp_data}
      return render(request, 'empapp/employee_list.html',d)

def edit_employee(request, pid):
    emp_data =Employee.objects.get(id=pid)
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        address = request.POST['address']
        phno = request.POST['phno']
        email = request.POST['email']
        designation = request.POST['designation']
        doj = request.POST['doj']
        salary = request.POST['salary']
        emp_obj = Employee.objects.filter(id=pid).update(fname=fname,lname=lname,dob=dob,address=address,phno=phno,email=email,designation=designation,doj=doj,salary=salary)
       
        return redirect('employee_list')
    return render(request, 'empapp/edit_employeee.html', {'emp_data':emp_data})

def delete_employee(request, pid):
    employee = get_object_or_404(Employee, id=pid)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')  # Replace 'employee_list' with the actual URL name
    return render(request, 'empapp/delete_employee.html')

#company 

def addcomp(request):
    if request.method == "POST":
        cName = request.POST['cName']
        cEmail = request.POST['cEmail']
        cUrl = request.POST['cUrl']
        cAddress = request.POST['cAddress']
        cContact = request.POST['cContact']
        comp_obj = Company.objects.create(cName=cName,cEmail=cEmail,cUrl =cUrl ,cAddress=cAddress,cContact=cContact)
        comp_obj.save()
        return redirect('comp_list')
    return render(request, 'empapp/addcomp.html')

def comp_list(request):
      comp_data = Company.objects.filter()
      d = {'Company':comp_data}
      return render(request, 'empapp/comp_list.html',d)

 

def edit_comp(request,pid):
    comp_data =Company.objects.get(id=pid)
    if request.method == "POST":
        cName = request.POST['cName']
        cEmail = request.POST['cEmail']
        cUrl = request.POST['cUrl']
        cAddress = request.POST['cAddress']
        cContact = request.POST['cContact']
        comp_obj = Company.objects.filter(id=pid).update(cName=cName,cEmail=cEmail,cUrl =cUrl ,cAddress=cAddress,cContact=cContact)
        return redirect('comp_list')
    return render(request, 'empapp/edit_comp.html', {'comp_data':comp_data})

def delete_comp(request,pid):
    company = get_object_or_404(Company, id=pid)
    if request.method == 'POST':
        company.delete()
        return redirect('comp_list')  # Replace 'employee_list' with the actual URL name
    return render(request, 'empapp/delete_comp.html')


    ####-------login---------------####

def loginn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('log_list')
    else:
        form = LoginForm()
    return render(request,'empapp/login.html', {'form': form})

def delete_log(request, id):
    login = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        login.delete()
        return redirect('log_list')
    return render(request, 'empapp/delete_log.html', {'login': login})

def log_list(request):
    log = Login.objects.all()
    return render(request, 'empapp/log_list.html', {'log': log})

# attendance

def attendance_list(request):
    attendance_list = Attendance.objects.all()
    return render(request, 'empapp/attendance_list.html', {'attendance_list': attendance_list})

def update_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    
    return render(request, 'empapp/update_attendance.html', {'form': form})




