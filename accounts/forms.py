from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Models
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")

    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)

        user.username = self.cleaned_data["email"]
        user.save()

        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "email",
        )


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("about",)
