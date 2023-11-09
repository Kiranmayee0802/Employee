from django.db import models

# Create your models here.

class Company(models.Model):
    cName = models.CharField(max_length=100, null=True, blank=True)
    # def __str__(self):
    #     return self.cName
    cEmail = models.EmailField()
    cUrl = models.CharField(max_length=50)
    cAddress = models.TextField()
    cContact = models.CharField(max_length=10)

class Employee(models.Model):
    fname = models.CharField(max_length=100, null=True, blank=True)
    lname = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phno = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    # eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True, default=0)
    leave_count = models.IntegerField(null=True, blank=True, default=0)
    on_leave = models.BooleanField(default=False)

    def __str__(self):
        return self.fname

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"

    def __str__(self):
        return f"{self.fname} {self.lname}"  

# login page

class Type(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.ForeignKey(Type,on_delete=models.CASCADE)

    #attendance

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    