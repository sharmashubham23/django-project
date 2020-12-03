from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('X_axis_Data', 'Y_axis_Data')
        