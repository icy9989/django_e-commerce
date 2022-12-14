from django import forms
from django.contrib.auth.models import User
from . import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class EditCustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username']

class CustomerForm(forms.ModelForm):
    profile_pic = forms.ImageField(label='Company Logo',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']


class ProductForm(forms.ModelForm):
    product_image = forms.ImageField(label='Company Logo',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    class Meta:
        model=models.Product
        widgets = {
            'category': forms.Select(attrs={'class':'form.control'})
        }
        fields=['name','price','description','category','product_image','quantity']    
# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model=models.Customer
#         fields=['address','mobile','profile_pic']

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model=models.Product
#         widgets = {
#             'category': forms.Select(attrs={'class':'form.control'})
#         }
#         fields=['name','price','description','category','product_image']

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
