from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model() 

from django import forms 

class UserCreationForm(forms.ModelForm):

    """
    A form that creats a custom user with no privilages
    form a provided email and password.
    """

    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args, **kargs)
        # del self.fields['username']

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name',]

    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        # password2 = self.cleaned_data.get('password2')
        # if password1 and password2 and password1 != password2:
        #     raise forms.ValidationError("passwords do not match")
        return password1

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user