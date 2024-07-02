from django import forms
from django.contrib.auth.models import User
from .models import Profile

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
            age=0,  # Default value or you can add an age field to the form
            email=user.email,
            nominated_bank_account=self.cleaned_data['nominated_bank_account'],
            main_balance=self.cleaned_data['main_balance']
        )
        profile.save()
        return user