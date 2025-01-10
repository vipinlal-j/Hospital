from django.shortcuts import render, redirect
from Admin.models import DepartmentDB, StaffDB
from WebApp.models import GuestAppointmwntDB

# Create your views here.
def index(req):
    return render(req, "index.html")
def admin_home(req):
    return render(req, "admin_home.html")
def add_departments(req):
    return render(req, "add_departments.html")
def add_departments_save(req):
    if req.method=="POST":
        a = req.POST.get('name')
        b = req.POST.get('email')
        c = req.POST.get('phone')
        d = req.POST.get('hod')
        e = req.POST.get('message')
        obj = DepartmentDB(Name=a, Email=b, Phone=c, HOD=d, Description=e)
        obj.save()
        return redirect(add_departments)
def add_staff(req):
    dept = DepartmentDB.objects.all()
    return render(req, "add_staff.html", {'dept':dept})
def add_staff_save(req):
    if req.method=="POST":
        a = req.POST.get('name')
        b = req.POST.get('email')
        c = req.POST.get('phone')
        d = req.POST.get('type')
        e = req.POST.get('message')
        f = req.POST.get('Department')
        g = req.POST.get('date')
        obj = StaffDB(Name=a, Email=b, Phone=c, Type=d, Qualifications=e, Department=f, DOB=g)
        obj.save()
        return redirect(add_staff)

def delete_staff(req,staff_id):
    a= StaffDB.objects.filter(id=staff_id)
    a.delete()
    return redirect(view_employee)

def view_department(req):
    data = DepartmentDB.objects.all()
    return render(req, "view_department.html", {'data':data})
def delete_department(req,dept_id):
    a= DepartmentDB.objects.filter(id=dept_id)
    a.delete()
    return redirect(view_department)
def view_employee(req):
    data = StaffDB.objects.all()
    return render(req, "view_employee.html", {'data':data})
def salary(req):
    return render(req, "salary.html")

def view_appointments(req):
    data = GuestAppointmwntDB.objects.all()
    return render(req, "view_appointments.html", {'data':data})