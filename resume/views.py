from django.db.models.query import EmptyQuerySet
from django.shortcuts import render
from .models import MySocial, MySkills, MyCertificates, MyEducation, MyWorkExperience, MyUser

# Create your views here.
def my_main_view(request):
    user = MyUser.objects.get(id=1)
    work = MyWorkExperience.objects.all()
    edu = MyEducation.objects.all()
    context = {
        "user":user,
        "work":work,              
        "edu": edu,
    }
    return render(request, 'resume/main.html', context)

def my_education_view(request):
    edu = MyEducation.objects.all()
    context = {
        "edu": edu,
    }
    return render(request, 'resume/edu.html', context)

def my_work_view(request):
    work = MyWorkExperience.objects.all()
    context = {
        "work": work,
    }
    return render(request, 'resume/work.html', context)

def my_skills_view(request):
    tech_skill = (MySkills.objects.filter(skill_is_tech = True),"Tech Skills",)
    lang_skill = (MySkills.objects.filter(skill_is_language = True), "Languages")
    other_skill = (MySkills.objects.filter(skill_is_other = True), "Other Skils")
    soft_skill = (MySkills.objects.filter(skill_is_soft = True), "Soft skills")
    skill_list = [tech_skill, lang_skill, other_skill, soft_skill]
    context = {
        "skill_list":skill_list,
    }
    return render(request, 'resume/skills.html', context)

def my_projects_view(request):
    return render(request, 'resume/projects.html', {})
