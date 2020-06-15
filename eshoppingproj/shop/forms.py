from django import forms


class RegistrationForm(forms.Form):
     '''first_name = forms.CharField(max_length=100)
     last_name = forms.CharField(max_length=100)
     user_name = forms.CharField(max_length=100)
     password = forms.CharField(max_length=100)
     mobile = forms.IntegerField()
     email = forms.EmailField(max_length=50)'''

     first_name = forms.CharField(
         label="Enter First Name",
         widget=forms.TextInput(
             attrs={
                 'placeholder': 'First Name',
                 'class': 'form-control'
             }
         )
     )
     last_name = forms.CharField(
         label="Enter Your Last Name",
         widget=forms.TextInput(
             attrs={
                 'placeholder': 'Last Name',
                 'class': 'form-control'
             }
         )
     )
     user_name = forms.CharField(
         label="Enter Your USerName",
         widget=forms.TextInput(
             attrs={
                 'placeholder': 'UserName',
                 'class': 'form-control'
             }
         )
     )
     password = forms.CharField(
         label="Enter Your Password",
         widget=forms.PasswordInput(
             attrs={
                 'placeholder': 'Password',
                 'class': 'form-control'
             }
         )
     )
     mobile = forms.CharField(
         label="Enter Your Mobile Number",
         widget=forms.NumberInput(
             attrs={
                 'placeholder': 'Mobile Number',
                 'class': 'form-control'
             }
         )
     )
     email = forms.EmailField(
         label="Enter Your Email ID",
         widget=forms.EmailInput(
             attrs={
                 'placeholder': 'Email ID',
                 'class': 'form-control'
             }
         )
     )


class loginform(forms.Form):
    user_name = forms.CharField(
        label="Enter Your USerName",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'User Name',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )
