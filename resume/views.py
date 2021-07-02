from django.db.models.query import EmptyQuerySet
from django.shortcuts import render
from .models import MyProjects, MySocial, MySkills, MyCertificates, MyEducation, MyWorkExperience, MyUser
user = MyUser.objects.get(id=1)
social = MySocial.objects.all()
# Create your views here.
def my_main_view(request):
    
    work = MyWorkExperience.objects.all().order_by("end_date")
    edu = MyEducation.objects.all().order_by("end_date")
    wk_list = [item for item in work]
    edu_list = [item for item in edu]
    obj_list = wk_list + edu_list
    obj_list.sort(key=lambda x: x.start_date, reverse=True)
    context = {
        "user":user,
        "obj_list": obj_list,
        "social": social,
    }
    return render(request, 'resume/main.html', context)

def my_education_view(request):
    all_edu = MyEducation.objects.all()
    edu = [item for item in all_edu]
    edu.sort(key=lambda x: x.start_date, reverse=True)
    context = {
        "edu": edu,
        "user":user,
        "social": social,
    }
    return render(request, 'resume/edu.html', context)

def my_work_view(request):
    all_work = MyWorkExperience.objects.all()
    work = [item for item in all_work]
    work.sort(key=lambda x: x.start_date, reverse=True)
    context = {
        "work": work,
        "user":user,
        "social": social,
    }
    return render(request, 'resume/work.html', context)

def my_skills_view(request):
    tech_skill = (MySkills.objects.filter(skill_is_tech = True),"Tech Skills",)
    lang_skill = (MySkills.objects.filter(skill_is_language = True), "Languages")
    other_skill = (MySkills.objects.filter(skill_is_other = True), "Other Skils")
    soft_skill = (MySkills.objects.filter(skill_is_soft = True), "Soft skills")
    hobby_skill = (MySkills.objects.filter(skill_is_hobby = True), "Hobbies")
    skill_list = [tech_skill, lang_skill, other_skill, soft_skill, hobby_skill]
    context = {
        "skill_list":skill_list,
        "user":user,
        "social": social,
    }
    return render(request, 'resume/skills.html', context)

def my_projects_view(request):
    projects = MyProjects.objects.all()
    return render(request, 'resume/projects.html', {'projects':projects,"user":user, "social": social,})

def my_footer_view(request):
    user = MyUser.objects.get(id=1)
    context = {
        'user':user,
    }
    return render(request, 'main_templates/footer.html', context)