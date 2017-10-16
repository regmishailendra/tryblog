from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from stories.models import Story


class StoryForm(ModelForm):
    class Meta:
        model=Story
        fields=['title','content','image']



class LoginForm(forms.Form):
   username=forms.CharField(max_length=15)
   password=forms.CharField(widget=forms.PasswordInput)



   # def clean(self):
   #     username=self.cleaned_data.get('username')
   #     password=self.cleaned_data.get('password')
   #     user=authenticate(username=username,password=password)
   #     if not user:
   #         raise forms.ValidationError('Your credientials donot match')
   #     #can do of check password for raising password doesnot match and is not active

class RegisterForm(forms.ModelForm):

    email2=forms.EmailField(label='Confirm Email')
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','email2','password']



    def clean_email2(self):
       email2= self.cleaned_data.get('email2')
       email= self.cleaned_data.get('email')



       if email2!=email:
           print('invalid')
           raise forms.ValidationError('Emails must match!')

       else:

           print('valid')

           email_see= User.objects.filter(email=email)
           if email_see.exists():
               print('already email took')
               raise forms.ValidationError('This email is already taken')
           return email2
