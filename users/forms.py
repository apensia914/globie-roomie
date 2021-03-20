from django import forms 
from . import models

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    #14.2 Validating Email
    def clean_email(self): # In order to check validity, method should always start with "clean_". 
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            models.User.objects.get(email=email)
            if user.check_password(password): 
                return self.cleaned_data
            else:
                self.add_error('password', forms.ValidationError('Password is wrong'))
        except models.User.DoesNotExist:
            self.add_error('email', forms.ValidationError('User does not exist'))