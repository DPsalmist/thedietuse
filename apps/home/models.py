from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from datetime import datetime, timedelta
from django.conf import settings
 

# Create your models here.
updated_time = ( datetime.now() + timedelta( hours=1 ))

# common choices
week_choices = (
		('1', 'Week 1'),
		('2', 'Week 2'),
		('3', 'Week 3'),
		('4', 'Week 4'),
		('5', 'Week 5'),
		('6', 'Week 6'),
		('7', 'Week 7'),
		('8', 'Week 8'),
		('9', 'Week 9'),
		('10', 'Week 10'),
		('11', 'Week 11'),
		('12', 'Week 12'),
		('13', 'Week 13'),
		('14', 'Week 14'),
		('15', 'Week 15'),
	)

term_choices = (
		('First Term', 'First Term'),
		('Second Term', 'Second Term'),
		('Third Term', 'Third Term'),
	)

year_choices = (
		('2022','2022'),
		('2023','2023'),
		('2024','2024'),
		('2025','2025'),
		('2026','2026'),
		('2027','2027'),
		('2028','2028'),
		('2029','2029'),
		('2030','2030'),
		('2031','2031'),
		('2032','2032'),
		('2033','2033'),
		('2034','2034'),
		('2035','2035'),
		('2036','2036'),
		('2037','2037'),
		('2038','2038'),
		('2039','2039'),
		('2040','2040'),
		('2041','2041'),
	)

# User Model
class User(AbstractUser):
	account = (
			('select account', 'select account'),
			('teacher', 'teacher'),
			('management', 'management'),
			('accountant', 'accountant'),
			('resource management', 'resource management'),
			('board member', 'board member')
		)
	account_type = models.CharField(max_length=200, choices=account, default='select account')
	email = models.CharField(max_length = 200, blank=True, unique=True)
	first_name = models.CharField(max_length=200, blank=True)
	last_name = models.CharField(max_length=200, blank=True)
	username = models.CharField(max_length = 200, blank=True, unique=True)
	verified = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.username

class Teacher(User):
	teacher_name = models.CharField(max_length=30, blank=True)
	subjects = models.CharField(max_length=100, blank=True)
	what_class = models.CharField(max_length=20, default='No Class')
	department = models.CharField(max_length=20)
	school_type = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.teacher_name


# Report Model
class Report(models.Model):
	report_choices = (
			('pending', 'pending'),
			('approved', 'approved'),
			('unapproved', 'unapproved')
		)
	title = models.CharField(max_length=200, unique=True)
	summary = models.CharField(max_length=250)
	report_class = models.CharField(max_length=60, blank=True)
	#body = RichTextField(blank=True, null=True)
	body = models.TextField(blank=True, default='enter description')
	status = models.CharField(max_length=60, choices=report_choices, default='pending')
	recommendation = models.CharField(max_length=500)
	date_created = models.DateTimeField(default=updated_time)
	date_updated = models.DateTimeField(auto_now=True)
	writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='writers')
	#likes = models.ManyToManyField(User, related_name='likes')

	# def total_likes(self):
	# 	return self.likes.count()

	def __str__(self):
		return self.title + ' by ' + str(self.writer)

	def get_absolute_url(self):
		return reverse('report-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ('-date_created',)
		
# Project Model
class Project(models.Model):
	project_choices = (
			('awaiting approval', 'awaiting approval'),
			('approved', 'approved'),
			('unapproved', 'unapproved'),
			('completed','completed'),
			('delayed', 'delayed')

		)
	updated_time = ( datetime.now() + timedelta( hours=1 ))
	title = models.CharField(max_length=200, unique=True)
	description = models.CharField(max_length=250)
	objective = models.CharField(max_length=500)
	project_class = models.CharField(max_length=60, blank=True)
	requirements = models.TextField(blank=True)
	status = models.CharField(max_length=60, choices=project_choices, default='awaiting approval')
	budget = models.FloatField()
	date_created = models.DateTimeField(default=updated_time)
	date_updated = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authors')
	completion = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.title + ' by ' + str(self.author) + ' with budget #' + str(self.budget)

	def get_absolute_url(self):
		return reverse('project-detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ('-date_created',)


# Appraisal Models
class StaffAppraisal(models.Model):
	staff_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_appraisals')
	#job_rating = models.ForeignKey(JobAppraisal, on_delete=models.CASCADE, related_name='staff_job_rating') 
	#gen_rating = models.ForeignKey(GeneralAppraisal, on_delete=models.CASCADE, related_name='staff_gen_rating') 
	staff_rating = models.CharField(max_length=50, blank=True, default='100')
	created_at = models.DateTimeField(default=updated_time)

	class Meta:
		abstract = False
		ordering = ['staff_rating']

	# def save(self, *args):
	# 	self.staff_rating = (((job_rating.avg_job_appraisal_performance + gen_rating.avg_general_appraisal_performance) / 2) * 100)
	# 	super(StaffAppraisal, self).save(*args)

	def __str__(self):
		return str(self.staff_rating)
		#return str(self.staff_name) + "'s rating ==> " + self.staff_rating


class GeneralAppraisal(StaffAppraisal):
	#Poor: 0-29, fair:30-49, avg:50-59, good:60-74, excellent:75-90, disctinction:91-100
	
	#appraisal_type = models.ForeignKey(Appraisal, on_delete=models.CASCADE)
	week = models.CharField(max_length=20, choices=week_choices, default='Week 1')
	term = models.CharField(max_length=20, choices=term_choices, default='First Term')
	year = models.CharField(max_length=20, choices=year_choices, default='2022')
	punctuality_to_school = models.IntegerField(blank=True)
	punctuality_to_class = models.IntegerField(blank=True)
	neatness_and_appearance = models.IntegerField(blank=True)
	respect_for_constituted_authority = models.IntegerField(blank=True)
	adherence_to_code_of_conduct = models.IntegerField(blank=True)
	initiative = models.IntegerField(blank=True)
	sense_of_responsibility = models.IntegerField(blank=True)
	courtesy_to_parents_and_supervisors = models.IntegerField(blank=True)
	acceptance_to_correction = models.IntegerField(blank=True)
	team_bonding_capacity = models.IntegerField(blank=True)
	attendance_and_participation_in_staff_meeting = models.IntegerField(blank=True)
	adherence_to_school_organogram = models.IntegerField(blank=True)
	involvement_in_extra_curricular_activities = models.IntegerField(blank=True)
	hod_remarks = models.CharField(max_length=500, blank=True)
	avg_general_appraisal_performance = models.DecimalField(decimal_places=2, default=0, max_digits=6)
	date_created = models.DateTimeField(default=updated_time)

	def save(self, *args, **kwargs):
		general_appraisal_ratings = self.punctuality_to_school + self.punctuality_to_class + self.neatness_and_appearance + self.respect_for_constituted_authority \
		+ self.adherence_to_code_of_conduct + self.initiative + self.sense_of_responsibility + self.courtesy_to_parents_and_supervisors + self.acceptance_to_correction \
		+ self.team_bonding_capacity + self.attendance_and_participation_in_staff_meeting + self.adherence_to_school_organogram + self.involvement_in_extra_curricular_activities 
	
		self.avg_general_appraisal_performance = general_appraisal_ratings / 16
		super(GeneralAppraisal, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('genappraisal-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return str(self.staff_name) + ' average general rating is ' + str(self.avg_general_appraisal_performance) + '%' + ' for ' + \
		 str(self.week) + ' (' + str(self.term) + ', Year ' + str(self.year) + ')'


class JobAppraisal(StaffAppraisal):
	# Poor: 0-29, fair:30-49, avg:50-59, good:60-74, excellent:75-90, disctinction:91-100
	Poor = (0,30)
	Fair = (30,50)
	Avg = (50,60)
	Good = (60,75) 
	Excellent = (75,90)
	Distinction = (91,100)

	appraisal_choices = (	
		(Poor, 'Poor'),
		(Fair, 'Fair'),
		(Avg, 'Average'),
		(Good, 'Good'),
		(Excellent, 'Excellent'),
		(Distinction, 'Distinction')
	)
	
	#appraisal_type = models.ForeignKey(Appraisal, on_delete=models.CASCADE)
	week = models.CharField(max_length=20, choices=week_choices, default='Week 1')
	term = models.CharField(max_length=20, choices=term_choices, default='First Term')
	year = models.CharField(max_length=20, choices=year_choices, default='2022')
	up_to_date_lesson_notes = models.IntegerField(blank=True)
	class_management_skills = models.IntegerField(blank=True)
	neatness_and_appearance = models.IntegerField(blank=True)
	classroom_communication = models.IntegerField( blank=True)
	time_management = models.IntegerField( blank=True)
	syllabus_compliance = models.IntegerField( blank=True)
	teaching_competence = models.IntegerField( blank=True)
	students_performance_in_subjects_taught = models.IntegerField( blank=True)
	parents_relationship = models.IntegerField( blank=True)
	students_relationship = models.IntegerField( blank=True)
	colleagues_relationship = models.IntegerField( blank=True)
	resource_management = models.IntegerField( blank=True)
	knowledge_of_subjects_taught = models.IntegerField( blank=True)
	comments_by_parents = models.IntegerField( blank=True)
	comments_by_students = models.IntegerField( blank=True)
	comments_by_colleagues = models.IntegerField( blank=True)
	hod_remarks = models.CharField(max_length=500, blank=True)
	avg_job_appraisal_performance = models.DecimalField(decimal_places=2, default=0, max_digits=6)
	appraisal_date = models.DateTimeField(default=updated_time)

	def save(self, *args, **kwargs):
		general_ratings = self.up_to_date_lesson_notes + self.class_management_skills + self.neatness_and_appearance + self.classroom_communication \
		+ self.time_management + self.syllabus_compliance + self.teaching_competence + self.students_performance_in_subjects_taught + self.parents_relationship \
		+ self.students_relationship + self.colleagues_relationship + self.resource_management + self.knowledge_of_subjects_taught + self.comments_by_parents \
		+ self.comments_by_students + self.comments_by_colleagues 
		
		self.avg_job_appraisal_performance = general_ratings / 16
		super(JobAppraisal, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('jobappraisal-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return str(self.staff_name) + ' average job rating is ' + str(self.avg_job_appraisal_performance) + '%' + ' for ' + \
		 str(self.week) + ' (' + str(self.term) + ', Year ' + str(self.year) + ')'
