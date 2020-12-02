from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('X_axis_Data', 'Y_axis_Data')
        # widgets={
        #     'X_axis_Data': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Y_axis_Data': forms.TextInput(attrs={'class': 'form-control'}),
        # }