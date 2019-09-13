from django import forms

class EmpForm(forms.Form):
    ename = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    sal = forms.IntegerField(
        label="Enter Your Salary",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Salary'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email ID'
            }
        )
    )
    location = forms.CharField(
        label="Enter Your LOcation",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Location'
            }
        )
    )