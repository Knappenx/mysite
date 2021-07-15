from django.urls import path
from .views import my_education_view, my_main_view, my_projects_view, my_skills_view, my_work_view

app_name = 'resume'
urlpatterns = [
    path('', my_main_view, name='main'),
    path('education/', my_education_view, name='education'),
    path('work/', my_work_view, name='work'),
    path('projects/', my_projects_view, name='projects'),
    path('other/', my_skills_view, name='skills'),
]
