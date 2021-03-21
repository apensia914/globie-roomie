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

#15.0
class SignUpForm(forms.ModelForm):
    class Meta: 
        model = models.User
        fields = ['first_name', 'last_name', 'email']

    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    # #15.0 Validating email
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     try:
    #         models.User.objects.get(email=email)
    #         raise forms.ValidationError('User already exists with that email')
    #     except models.User.DoesNotExist:
    #         return email
    
    #15.0 Validating password
    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('Password does not match!')
        else:
            return password 
    
    #15.2 
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user.username = email
        user.set_password(password)
        user.save() 

        