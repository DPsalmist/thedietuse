from django.forms import ModelForm
from .models import Report, Project

class CreatReportForm(ModelForm):
	class Meta:
		model = Report
		fields = '__all__'
		exclude = ['writer']


class CreatProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = '__all__'
		exclude = ['author']