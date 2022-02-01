from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
    """ Display user profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,

    }

    return render(request, template, context)
