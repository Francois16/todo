from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404


# Models
from .models import Profile

# Forms
from .forms import UpdateUserForm, UpdateUserProfileForm


def profile_view(request):

    template_name = "accounts/profile.html"

    if request.method == "POST":
        user_form = UpdateUserForm(
            request.POST, instance=get_object_or_404(get_user_model(), id=request.user.id)
        )
        profile_form = UpdateUserProfileForm(
            request.POST, instance=get_object_or_404(Profile, user=request.user)
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect("profile")

    else:
        user_form = UpdateUserForm(instance=get_object_or_404(get_user_model(), id=request.user.id))
        profile_form = UpdateUserProfileForm(instance=get_object_or_404(Profile, user=request.user))

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, template_name, context)
