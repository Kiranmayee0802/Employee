from django import forms
from .models import Login
from .models import Attendance


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Login
        fields = '__all__'
        # fields = ('username','password','type')

        # labels = {
        #     'emp_name':'Full Name',
        #     'emp_phno':'Phone Number'
        # }

    def __init__(self, *args,**kwargs):
     super(LoginForm,self).__init__(*args, **kwargs)
     self.fields['type'].empty_label = "Select"

    

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']

    def __init__(self, *args,**kwargs):
     super(AttendanceForm,self).__init__(*args, **kwargs)
     self.fields['employee'].empty_label = "Select"
     
