from dataclasses import field
from random import choices

from django.core import validators



from django import forms

class user_form(forms.Form):
    # user_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder':'Enter you full name'}))
    # user_email = forms.EmailField(label='User Email', widget=forms.TextInput(attrs={'placeholder':'Please,Enter your Email'}))
    
    # user_dob = forms.DateField(label='Date Of Birth',widget=forms.TextInput(attrs={'type':'date'}))
      # boolean_field = forms.BooleanField(required=False)
  #  field = forms.CharField(max_length=15, min_length=5)
  # choices = (('','--SELECT OPTION'),('1','First'),('2','Second'),('3','Third'))
  # field = forms.ChoiceField(choices=choices,required=False)
  
  # choices = (('A','A'),('B','B'),('C','C'),('D','D'))
  # field = forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
  
   choices = (('A','A'),('B','B'),('C','C'),('D','D'))
   field = forms.MultipleChoiceField(choices=choices,widget=forms.CheckboxSelectMultiple)
  
        
      
      