from django import forms
class InsertDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter Product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    product_color = forms.CharField(
        label="Enter Product Color",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter Product Class",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    number_of_items = forms.IntegerField(
        label="Enter Number of Items",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Number Of Items'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    customer_name = forms.CharField(
        label="Enter Customer Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )
    customer_mobile = forms.IntegerField(
        label="Enter Customer Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    customer_email = forms.EmailField(
        label="Enter Customer Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Email'
            }
        )
    )

class UpdateDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )


class DeleteDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )