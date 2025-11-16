from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fileds =["username", "password"]