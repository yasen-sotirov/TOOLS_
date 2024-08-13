from django import forms


class CreateNewList(forms.Form):
    # полета за формата
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(label="Truly?", required=False)