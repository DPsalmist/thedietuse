from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, ProfileEditForm
from .models import Profile
from apps.home.models import StaffAppraisal

# Create your views here.
def profile_view(request):
    profile = Profile.objects.all()
    user = request.user
    user = user
    staff_rating = StaffAppraisal.objects.filter(staff_name=user)
    print(f'staff_rating for {user.username, user.id} =', staff_rating)
    return render(request, 'home/profile.html', {'profile':profile, 'staff_rating':staff_rating})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,
										data = request.POST,
										files = request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			print('updated successfully!')
			messages.success(request, f'Profile updated successfully!')
			return redirect('profile')
		else: 
			messages.warning(request, f'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	context = {
		'user_form':user_form,
		'profile_form':profile_form
	}
	return render(request, 'accounts/edit.html', context)