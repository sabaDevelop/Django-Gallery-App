from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    
class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput( attrs={'placeholder': 'Password'}))


