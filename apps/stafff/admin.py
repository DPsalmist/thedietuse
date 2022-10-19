from django.contrib import admin
from .models import Profile

# Register your models here.
#admin.site.register(Report)
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'gender', 'photo', 'school_type', 'staff_no_of_subjects', 'department', 'staff_id']

'''
@admin.register(Profile)
class JobAppraisalAdmin(admin.ModelAdmin):
	list_display = ('staff_name', 'week', 'term', 'year', 'avg_job_appraisal_performance', 'hod_remarks', 'appraisal_date')
	list_filter = ('week','term', 'created_at')
	search_fields = ('staff_name','week',)
	ordering = ('-avg_job_appraisal_performance',)
'''