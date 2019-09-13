from django import forms
class HotelForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-class',
                'placeholder':"Name"
            }
        )
    )
    hotel_Main_Img = forms.ImageField(
        label="Select Your Image",
        widget=forms.FileInput(
            attrs={
                'class':'form-control'
            }
        )
    )