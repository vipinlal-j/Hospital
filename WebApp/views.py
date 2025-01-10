from django.shortcuts import render, redirect
from WebApp.models import GuestAppointmwntDB
from Admin.models import StaffDB, DepartmentDB

# Create your views here.
def index(req):
    return render(req, "index.html")
def home(req):
    return render(req, "home.html")
def book_appointment_guest(req):
    data = DepartmentDB.objects.all()
    return render(req, "book_appointment_guest.html", {'data':data})
def save_appointment_guest(req):
    if req.method=="POST":
        a = req.POST.get('name')
        b = req.POST.get('email')
        c = req.POST.get('phone')
        d = req.POST.get('Department')
        e = req.POST.get('message')
        f = req.POST.get('date')
        g = req.POST.get('fee')
        obj = GuestAppointmwntDB(Name=a, Email=b, Phone=c, Department=d, Description=e, Date=f, Fee=g)
        obj.save()
        return redirect(book_appointment_guest)


