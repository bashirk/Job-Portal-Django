from django.urls import path
from account import views

app_name = "account"

urlpatterns = [

    path('freelancer/register/', views.freelancer_registration, name='freelancer-registration'),
    path('taskowner/register/', views.taskowner_registration, name='taskowner-registration'),
    path('profile/edit/<int:id>/', views.employee_edit_profile, name='edit-profile'),
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
