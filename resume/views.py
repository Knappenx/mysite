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

def my_skills_view(request):
    tech_skill = MySkills.objects.filter(skill_is_tech = True)
    lang_skill = MySkills.objects.filter(skill_is_language = True)
    other_skill = MySkills.objects.filter(skill_is_other = True)
    soft_skill = MySkills.objects.filter(skill_is_soft = True)
    context = {
        "tech_skill":tech_skill,
        "lang_skill":lang_skill,
        "other_skill":other_skill,
        "soft_skill":soft_skill
    }
    return render(request, 'resume/skills.html', context)

