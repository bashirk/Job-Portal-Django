from django.urls import path
from jobapp import views

app_name = "jobapp"


urlpatterns = [

    path('', views.home_view, name='home'),
    path('tasks/', views.job_list_View, name='job-list'),
    path('task/create/', views.create_job_View, name='create-job'),
    path('task/<int:id>/', views.single_job_view, name='single-job'),
    path('apply-task/<int:id>/', views.apply_job_view, name='apply-job'),
    path('bookmark-task/<int:id>/', views.job_bookmark_view, name='bookmark-job'),
    path('about/', views.single_job_view, name='about'),
    path('contact/', views.single_job_view, name='contact'),
    path('result/', views.search_result_view, name='search_result'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/taskowner/job/<int:id>/applicants/', views.all_applicants_view, name='applicants'),
    path('dashboard/taskowner/job/edit/<int:id>', views.job_edit_view, name='edit-job'),
    path('dashboard/taskowner/applicant/<int:id>/', views.applicant_details_view, name='applicant-details'),
    path('dashboard/taskowner/close/<int:id>/', views.make_complete_job_view, name='complete'),
    path('dashboard/taskowner/delete/<int:id>/', views.delete_job_view, name='delete'),
    path('dashboard/taskowner/delete-bookmark/<int:id>/', views.delete_bookmark_view, name='delete-bookmark'),
    path('dashboard/taskowner/applicant/<int:id>/customer-info', views.customer_info, name='customer-info'),


]
