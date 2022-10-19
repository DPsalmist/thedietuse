from django.urls import path, re_path
from apps.home import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),


    # The Report views
    path('reports/', views.ReportListView.as_view(template_name='reports/reports.html')),
    path('report/new/', views.ReportCreateView.as_view(template_name='reports/report_form.html'), name='create-report'),
    path('report/<int:pk>/', views.ReportDetailView.as_view(template_name='reports/report_detail.html'), name='report-detail'),
    path('report/<int:pk>/update/', views.ReportUpdateView.as_view(template_name='reports/report_update_form.html'), name='report-update'),
    path('report/<int:pk>/delete/', views.ReportDeleteView.as_view(template_name='reports/report_confirm_delete.html'), name='report-delete'),

    # The Project views
    path('projects/', views.ProjectListView.as_view(template_name='projects/projects.html')),
    path('project/new/', views.ProjectCreateView.as_view(template_name='projects/project_form.html'), name='create-project'),
    path('project/appraisals<int:pk>/', views.ProjectDetailView.as_view(template_name='projects/project_detail.html'), name='project-detail'),
    path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(template_name='projects/project_update_form.html'), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(template_name='projects/project_confirm_delete.html'), name='project-delete'),

    # The Appraisal views - Job Appraisal
    path('jobappraisals/', views.JobAppraisalListView.as_view(template_name='appraisals/jobappraisals.html')),
    path('jobappraisal/new/', views.JobAppraisalCreateView.as_view(template_name='appraisals/jobappraisal_form.html'), name='create-jobappraisal'),
    path('jobappraisal/<int:pk>/', views.JobAppraisalDetailView.as_view(template_name='appraisals/jobappraisal_detail.html'), name='jobappraisal-detail'),
    path('jobappraisal/<int:pk>/update/', views.JobAppraisalUpdateView.as_view(template_name='appraisals/jobappraisal_update_form.html'), name='jobappraisal-update'),
    path('jobappraisal/<int:pk>/delete/', views.JobAppraisalDeleteView.as_view(template_name='appraisals/jobappraisal_confirm_delete.html'), name='jobappraisal-delete'),

    # General Appraisal
    path('appraisals/', views.GenAppraisalListView.as_view(template_name='appraisals/genappraisals.html')),
    path('staff/appraisal/new/', views.GenAppraisalCreateView.as_view(template_name='appraisals/genappraisal_form.html'), name='create-genappraisal'),
    path('staff/appraisal/<int:pk>/', views.GenAppraisalDetailView.as_view(template_name='appraisals/genappraisal_detail.html'), name='genappraisal-detail'),
    path('staff/appraisal/<int:pk>/update/', views.GenAppraisalUpdateView.as_view(template_name='appraisals/genappraisal_update_form.html'), name='genappraisal-update'),
    path('staff/appraisal/<int:pk>/delete/', views.GenAppraisalDeleteView.as_view(template_name='appraisals/genappraisal_confirm_delete.html'), name='genappraisal-delete'),


    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
