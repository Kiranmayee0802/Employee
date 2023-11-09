from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),

    # employee
     path('addemp',views.addemp,name='addemp'),
    path('employee-edit/<int:pid>', views.edit_employee, name="edit_employee"),
    path('employee_list',views.employee_list,name='employee_list'),
    path('delete_employee/<int:pid>', views.delete_employee, name="delete_employee"),

    # company
     path('addcomp',views.addcomp,name='addcomp'),
     path('comp_list',views.comp_list,name='comp_list'),
    path('edit_comp/<int:pid>/', views.edit_comp, name='edit_comp'),
    path('delete_comp/<int:pid>/', views.delete_comp, name='delete_comp'),

    # login
    path('loginpage/',views.loginn,name='loginn'), #get and post request for insert operation
    path('loginlist/',views.log_list,name='log_list'), # get request to retrieve and display all records
    path('delete/<int:id>/',views.delete_log,name='delete_log'),

    # attendance

    path('attendance-list/', views.attendance_list, name='attendance_list'),
    path('update-attendance/', views.update_attendance, name='update_attendance'),
]

