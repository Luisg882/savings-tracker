from django import forms
from django.contrib.auth.models import User

from .models import Profile, SavingPot
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


# Form to create a new user
class CustomSignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nominated_bank_account', 'main_balance')

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.save()

        profile = Profile(
            user=user,
            slug=user.username,
            age=0,
            email=user.email,
            nominated_bank_account=self.cleaned_data['nominated_bank_account'],
            main_balance=self.cleaned_data['main_balance']
        )
        profile.save()
        return user


# Form to add money to the user’s main balance
class AddMoney(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('main_balance',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False


# Form to open a new saving pot
class OpenNewPot(forms.ModelForm):
    class Meta:
        model = SavingPot
        fields = ('name',)


# Form to move money to a saving pot
class AddMoneySavingPot(forms.ModelForm):
    class Meta:
        model = SavingPot
        fields = ('balance',)


# Form to change the name of a saving pot
class ChangeNameSavingPot(forms.ModelForm):
    class Meta:
        model = SavingPot
        fields = ('name',)
