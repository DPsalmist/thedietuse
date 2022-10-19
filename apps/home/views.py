from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
#from django.contrib.auth.models import User
from django.template import loader
from django.urls import reverse, reverse_lazy
from .models import Report, Project, JobAppraisal, GeneralAppraisal, User

from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.views.generic import ( 
    ListView, 
    DetailView, 
    CreateView,
    DeleteView
)

# from datetime import datetime, timedelta
  
@login_required(login_url="/login/")
def index(request):
    # staff data
    tot_users = User.objects.count()
    tot_projects = Project.objects.count()
    tot_reports = Report.objects.count()

    # top 5 projects
    top_projects = Project.objects.order_by('-completion')[:5]

    avg_staff_performance = 23
    print('total staff: ', tot_users)
    context = {
        'segment': 'index', 'tot_staff':tot_users, 'tot_projects':tot_projects, 
        'tot_reports':tot_reports, 'top_projects':top_projects, 
        }
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def user_reports(request):
    pass



'''
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url and loads that template.
    try:
        load_template = request.path.split('/')[-1] # returns a list of the given url
        #print('Curent route: ', load_template)
        load_template2 = request.path

        # Get the routes for each view
        if load_template == 'admin':
            print('Going to admin...')
            return HttpResponseRedirect(reverse('admin:index'))
            context['segment'] = load_template
            html_template = loader.get_template('home/' + load_template)
            return HttpResponse(html_template.render(context, request))

        # Profile App
        elif load_template == '/profile.html':
            print('Inside profile route', load_template)
            user = request.user
            print('current user: ', user, user.profile.photo)
            users = User.objects.all()
            context = {'users':users, 'user': user}
            #html_template = loader.get_template('appraisals/testpage.html')
            html_template = loader.get_template('home/profile.html')
            print('Expected template: ', html_template)
            return HttpResponse(html_template.render(context, request))

        # Reports App
        elif load_template2 == '/reports':
            print('Inside reports route')
            reports = Report.objects.all()
            context = {'reports':reports}
            html_template = loader.get_template('reports/reports.html')
            #return HttpResponse(html_template.render(context, request))
            return render(request, 'reports/reports.html', context)

        # Projects App
        elif load_template2 == '/projects':
            print('Inside projects route')
            projects = Project.objects.all()
            context = {'projects':projects}
            html_template = loader.get_template('projects/projects.html')
            return HttpResponse(html_template.render(context, request))


        # Appraisal App (Job)
        elif load_template2 == '/jobappraisals':
            print('Inside jobappraisals route', load_template2)
            jobs = JobAppraisal.objects.all()            
            context = {'jobs':jobs}
            #html_template = loader.get_template('appraisals/testpage.html')
            html_template = loader.get_template('appraisals/jobappraisals.html')
            return HttpResponse(html_template.render(context, request))

        # Appraisal App (General)
        elif load_template2 == '/appraisals':
            print('Inside appraisals route', load_template)
            gens = GeneralAppraisal.objects.all()
            context = {'gens':gens}
            #html_template = loader.get_template('appraisals/testpage.html')
            html_template = loader.get_template('appraisals/genappraisals.html')
            
            return HttpResponse(html_template.render(context, request))

        # Appraisal App (General)
        elif load_template2 == '/media/':
            print('Inside appraisals route', load_template)
            gens = GeneralAppraisal.objects.all()
            context = {'gens':gens}
            #html_template = loader.get_template('appraisals/testpage.html')
            html_template = loader.get_template('appraisals/genappraisals.html')
            return HttpResponse(html_template.render(context, request))
                

        # Get other implicit pages    
        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))


    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
'''

# Report Class Views
class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = ['title', 'summary', 'body', 'recommendation']

    #overriding the form valid method
    def form_valid(self, form):
        form.instance.writer  = self.request.user
        return super().form_valid(form)

class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    #context_object_name = 'reports'
    #template_name = 'home/reports.html'

class ReportDetailView(DetailView):
    model = Report

class ReportUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin,):
    model = Report
    fields = ['title', 'summary', 'body', 'recommendation']

    def form_valid(self, form):
        form.instance.writer  = self.request.user
        return super().form_valid(form)

    #test function to make only an authorised user update a post
    def test_func(self):
        report = self.get_object()
        if self.request.user == report.writer:
            return True
        return False

class ReportDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin,):
    model = Report
    success_url = '/reports.html'
    #success_url = reverse_lazy('reports') #('staff-report-list')

    #test function to make only an authorised user delete a post
    def test_func(self):
        report = self.get_object()
        if self.request.user == report.writer:
            return True
        return False


# Project Class Views
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project    
    fields = ['title', 'objective', 'description', 'project_class', 'budget', 'requirements', 'completion']

    #overriding the form valid method
    def form_valid(self, form):
        form.instance.author  = self.request.user
        return super().form_valid(form)

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project    #context_object_name = 'reports'
    #template_name = 'home/reports.html'

class ProjectDetailView(DetailView):
    model = Project

class ProjectUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin,):
    model = Project
    fields = ['title', 'objective', 'description', 'project_class', 'budget', 'requirements', 'completion']

    def form_valid(self, form):
        form.instance.author  = self.request.user
        return super().form_valid(form)

    #test function to make only an authorised user update a post
    def test_func(self):
        project= self.get_object()
        if self.request.user == project.author:
            return True
        return False

class ProjectDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin,):
    model = Project    
    success_url = '/projects.html'

    #test function to make only an authorised user delete a post
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False


# Job Appraisal Class Views
class JobAppraisalListView(LoginRequiredMixin, ListView):
    model = JobAppraisal

class JobAppraisalCreateView(LoginRequiredMixin, CreateView):
    model = JobAppraisal    
    fields = ['staff_name', 'week', 'term', 'year', 'up_to_date_lesson_notes', 'class_management_skills', 'neatness_and_appearance', \
     'classroom_communication', "time_management", 'syllabus_compliance', 'teaching_competence', 'students_performance_in_subjects_taught', \
     'parents_relationship', 'students_relationship', 'colleagues_relationship', 'resource_management', 'knowledge_of_subjects_taught', \
     'comments_by_parents', 'comments_by_students', 'comments_by_colleagues', 'hod_remarks']

    #overriding the form valid method
    def form_valid(self, form):
        form.instance.staff_name  = self.request.user
        return super().form_valid(form)

class JobAppraisalDetailView(DetailView):
    model = JobAppraisal

    def get_context_data(self, **kwargs):
        context = super(JobAppraisalDetailView, self).get_context_data(**kwargs)
        obj = self.object
        this_job_rating = obj.avg_job_appraisal_performance
        this_job_rating = int(this_job_rating)
        # set necessary contexts
        context['this_job_rating'] = this_job_rating
        context['distinction'] = list(range(90, 101))
        context['excellent'] = list(range(75,90))
        context['good'] = list(range(60,75))
        context['avg'] = list(range(50,60))
        context['fair'] = list(range(30,50))
        context['poor'] = list(range(0,30))
        return context

class JobAppraisalUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin,):
    model = JobAppraisal
    fields = ['staff_name', 'week', 'term', 'year', 'up_to_date_lesson_notes', 'class_management_skills', 'neatness_and_appearance', \
     'classroom_communication', "time_management", 'syllabus_compliance', 'teaching_competence', 'students_performance_in_subjects_taught', \
     'parents_relationship', 'students_relationship', 'colleagues_relationship', 'resource_management', 'knowledge_of_subjects_taught', \
     'comments_by_parents', 'comments_by_students', 'comments_by_colleagues', 'hod_remarks']

    def form_valid(self, form):
        form.instance.staff_name  = self.request.user
        return super().form_valid(form)

    #test function to make only an authorised user update a post
    def test_func(self):
        jobappraisal= self.get_object()
        if self.request.user == jobappraisal.staff_name:
            return True
        return False

class JobAppraisalDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin,):
    model = JobAppraisal    
    success_url = '/appraisals.html'

    #test function to make only an authorised user delete a post
    def test_func(self):
        jobappraisal = self.get_object()
        if self.request.user == jobappraisal.staff_name:
            return True
        return False

# General Appraisal Class Views
class GenAppraisalListView(LoginRequiredMixin, CreateView):
    model = GeneralAppraisal
    fields = ['staff_name', 'week', 'term', 'year', 'punctuality_to_school', 'punctuality_to_class', 'neatness_and_appearance', \
     'respect_for_constituted_authority', "adherence_to_code_of_conduct", 'initiative', 'sense_of_responsibility', 'courtesy_to_parents_and_supervisors', \
     'acceptance_to_correction', 'team_bonding_capacity', 'attendance_and_participation_in_staff_meeting', 'adherence_to_school_organogram', \
        'involvement_in_extra_curricular_activities', 'hod_remarks']

class GenAppraisalCreateView(LoginRequiredMixin, CreateView):
    model = GeneralAppraisal    
    fields = ['staff_name', 'week', 'term', 'year', 'punctuality_to_school', 'punctuality_to_class', 'neatness_and_appearance', \
     'respect_for_constituted_authority', "adherence_to_code_of_conduct", 'initiative', 'sense_of_responsibility', 'courtesy_to_parents_and_supervisors', \
     'acceptance_to_correction', 'team_bonding_capacity', 'attendance_and_participation_in_staff_meeting', 'adherence_to_school_organogram', \
        'involvement_in_extra_curricular_activities', 'hod_remarks']

    #overriding the form valid method
    def form_valid(self, form):
        form.instance.staff_name  = self.request.user
        return super().form_valid(form)

class GenAppraisalDetailView(DetailView):
    model = GeneralAppraisal

    def get_context_data(self, **kwargs):
        context = super(GenAppraisalDetailView, self).get_context_data(**kwargs)
        obj = self.object
        this_appraisal_rating = obj.avg_general_appraisal_performance
        this_appraisal_rating = int(this_appraisal_rating)
        # set necessary contexts
        context['this_appraisal_rating'] = this_appraisal_rating
        context['distinction'] = list(range(90, 101))
        context['excellent'] = list(range(75,90))
        context['good'] = list(range(60,75))
        context['avg'] = list(range(50,60))
        context['fair'] = list(range(30,50))
        context['poor'] = list(range(0,30))
        return context

class GenAppraisalUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin,):
    model = GeneralAppraisal
    fields = ['staff_name', 'week', 'term', 'year', 'punctuality_to_school', 'punctuality_to_class', 'neatness_and_appearance', \
     'respect_for_constituted_authority', "adherence_to_code_of_conduct", 'initiative', 'sense_of_responsibility', 'courtesy_to_parents_and_supervisors', \
     'acceptance_to_correction', 'team_bonding_capacity', 'attendance_and_participation_in_staff_meeting', 'adherence_to_school_organogram', \
        'involvement_in_extra_curricular_activities', 'hod_remarks']

    def form_valid(self, form):
        form.instance.staff_name  = self.request.user
        return super().form_valid(form)

    #test function to make only an authorised user update a post
    def test_func(self):
        generalappraisal= self.get_object()
        if self.request.user == generalappraisal.staff_name:
            return True
        return False

class GenAppraisalDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin,):
    model = GeneralAppraisal    
    success_url = '/appraisals.html'

    #test function to make only an authorised user delete a post
    def test_func(self):
        generalappraisal = self.get_object()
        if self.request.user == Generalappraisal.staff_name:
            return True
        return False

'''
class UserExamListView(ListView):
    model = Exam
    template_name = 'exams/user_exams.html' 
    context_object_name = 'my_exams'
    ordering = ['-created'] 
    paginate_by = 3

    def get_queryset(self):
        #getting the username from the url 
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        print('this user:', user)
        return Exam.objects.filter(poster=user).order_by('-exam_date')

    def get_context_data(self, **kwargs):
        pending_exams = Exam.objects.filter(completed=False)
        pending_exams = pending_exams.count()
        print('pending_exams', pending_exams)
        context = {'pending_exams':pending_exams}
        kwargs.update(context)
        return super().get_context_data(**kwargs)
'''