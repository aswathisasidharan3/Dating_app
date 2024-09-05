from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'myapp'

urlpatterns=[
   
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    
    path('login/', views.LoginView.as_view(), name='login'),
    path('details', views.DetailsView.as_view(), name='details'),
    path('job_status', views.JobStatusView.as_view(), name='job_status'),
    path('job_details', views.JobDetailsView.as_view(), name='job_details'),
    path('job_title', views.JobTitleView.as_view(), name='job_title'),
    path('relationship', views.RelationView.as_view(), name='relationship'),
    path('interested', views.InterestView.as_view(), name='interest'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    # path('reset_password/',auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_done'),
]