from django import forms

class registrationForm(forms.Form):
    fullName = forms.CharField(label="Full Name",widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))

class checkEvenOddForm(forms.Form):
    anyNumber = forms.CharField(label="Enter any number ...",widget=forms.NumberInput(attrs={"class":"form-control"}))
    
    