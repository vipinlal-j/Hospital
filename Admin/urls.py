from django.urls import path
from Admin import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('add_departments/', views.add_departments, name="add_departments"),
    path('add_departments_save/', views.add_departments_save, name="add_departments_save"),
    path('add_staff/', views.add_staff, name="add_staff"),
    path('add_staff_save/', views.add_staff_save, name="add_staff_save"),
    path('view_department/', views.view_department, name="view_department"),
    path('delete_department/<int:dept_id>/', views.delete_department, name="delete_department"),

    path('view_employee/', views.view_employee, name="view_employee"),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name="delete_staff"),

    path('salary/', views.salary, name="salary"),

    path('view_appointments/', views.view_appointments, name="view_appointments"),

]