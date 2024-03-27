from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Profilenewmain
from .models import JobApplication

from django import forms



class SignUpFormStu(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label="",max_length=100,widget= forms.TextInput(attrs={'class':'control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100,widget= forms.TextInput(attrs={'class':'control','placeholder':'Last Name'}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignUpFormStu,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



    
class Profilerec(forms.ModelForm):        
    father_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'father_name'}))
   
    marks = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'marks'}))
    phone_number = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    address = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))        
    city = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    backlogs = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'backlogs'}))
    date_of_birth = forms.DateField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'date_of_birth'}))
    year_of_passing = forms.IntegerField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'year_of_passing'}))
    skills = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'skills'}))
    zipcode = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'zipcode'}))


    class Meta:
        model = Profilenewmain
        fields = ['marks', 'backlogs', 'date_of_birth', 'father_name', 'year_of_passing', 'address', 'city', 'zipcode', 'phone_number', 'skills']


class ProfileUpdateForm(forms.ModelForm):
   
    phone_number = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    address = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    city = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    marks = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'marks'}))
    backlogs = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'backlogs'}))
    date_of_birth = forms.DateField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'date_of_birth'}))
    father_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'father_name'}))
    year_of_passing = forms.IntegerField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'year_of_passing'}))
    skills = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'skills'}))
    zipcode = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'zipcode'}))

    class Meta:
        model = Profilenewmain
        fields = ['marks', 'backlogs', 'date_of_birth', 'father_name', 'year_of_passing', 'address', 'city', 'zipcode', 'phone_number', 'skills']


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Adress'}))
    
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude the password field from the form
        self.fields.pop('password', None)



class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []  # Add any additional fields you want in the form

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        # Customize form fields here if needed