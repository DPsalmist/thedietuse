from django.contrib import admin
from .models import Report, Project, StaffAppraisal, GeneralAppraisal, JobAppraisal, User

# Register your models here.
admin.site.register(Report)
admin.site.register(Project)
admin.site.register(StaffAppraisal)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'first_name', 'last_name', 'email', 'account_type', 'verified', 'date_created']

@admin.register(GeneralAppraisal)
class GeneralAppraisalAdmin(admin.ModelAdmin):
	list_display = ('staff_name', 'week', 'term', 'year', 'avg_general_appraisal_performance', 'hod_remarks', 'date_created')
	list_filter = ('week','term', 'created_at')
	search_fields = ('staff_name','week',)
	date_hierarchy = 'created_at'
	ordering = ('-avg_general_appraisal_performance',)

@admin.register(JobAppraisal)
class JobAppraisalAdmin(admin.ModelAdmin):
	list_display = ('staff_name', 'week', 'term', 'year', 'avg_job_appraisal_performance', 'hod_remarks', 'appraisal_date')
	list_filter = ('week','term', 'created_at')
	search_fields = ('staff_name','week',)
	ordering = ('-avg_job_appraisal_performance',)
