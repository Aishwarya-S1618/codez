from django import forms



class CreateNewList(forms.Form):
    name = forms.CharField(max_length=20, default='', null=False)
    email = forms.CharField(max_length=30, default='', null=False)
    phone = forms.CharField(max_length=10, default='', null=False)
    comment = forms.CharField(max_length=200, default='', null=False)

 