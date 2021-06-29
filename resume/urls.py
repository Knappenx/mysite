from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.my_main_view, name='main'),
    path('education/', views.my_education_view, name='education'),
    path('work/', views.my_work_view, name='work'),
    path('projects/', views.my_projects_view, name='projects'),
    path('other/', views.my_skills_view, name='skills'),
]
