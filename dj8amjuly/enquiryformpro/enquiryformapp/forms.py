from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Number'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )
    location = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Location'
            }
        )
    )

    COUESES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('java', 'Java'),
        ('ui', 'UI'),
        ('Fl', 'Flask')
    )
    courses = MultiSelectFormField(choices=COUESES_CHOICES, label="Select Required Courses:")

    BRANCHES_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Bangalore'),
        ('che', 'Chennai'),
        ('pune', 'Pune')
    )
    branches = MultiSelectFormField(choices=BRANCHES_CHOICES, label="Select Required Branches:")

    SHIFTS_CHOICES = (
        ('mrg', 'Morning Shift'),
        ('aftn', 'Afternoon Shift'),
        ('evng', 'Evening Shift'),
        ('ngt', 'Night Shift')
    )
    shifts = MultiSelectFormField(choices=SHIFTS_CHOICES, label="Select Required Shifts:")

    GENDER_CHOICES = (
        ('m','Male'),
        ('f','Female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES, label="Select Your Gender:")

    y = range(1960,2050)

    start_date = forms.DateField(
        widget=forms.SelectDateWidget(years=y),label="Enter Your Comfortable Data:"
    )