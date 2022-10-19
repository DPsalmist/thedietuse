from django import forms
from .models import Profile
from apps.home.models import User


class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
		print('user is', User.account_type)


class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user','headline', 'photo', 'timeline_picture', 'gender', 'staff_bio', 'staff_id', 'school_name', 'department', 'school_type',
			'staff_class', 'staff_subject', 'staff_no_of_subjects', 'bank', 'account_no', 'account_name', 'phone_no', 'address', 'city', 'country',
			'state_of_origin', 'nationality', 'religion')
		'''
		def __init__(self, *args, **kwargs):
			super(ProfileEditForm, self).__init__(*args, **kwargs)
			if Profile.verified == True
				exclude = ('staff_id',)
		'''
			