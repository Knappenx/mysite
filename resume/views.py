from django.db.models.query import EmptyQuerySet
from django.shortcuts import render
from .models import MyProjects, MySocial, MySkills, MyCertificates, MyEducation, MyWorkExperience, MyUser, MyTemplateURLs


def inicialization():
    try:
        user = MyUser.objects.get(user_to_display=True)
        social = MySocial.objects.filter(user=user)
        template_urls = MyTemplateURLs.objects.get(user=user)
        return user, social, template_urls
    except:
        user = None
        social = None
        template_urls = None
        return user, social, template_urls

# Create your views here.
def my_main_view(request):
    user, social, template_urls = inicialization()
    work = MyWorkExperience.objects.filter(user=user).order_by("end_date")
    edu = MyEducation.objects.filter(user=user).order_by("end_date")
    wk_list = [item for item in work]
    edu_list = [item for item in edu]
    obj_list = wk_list + edu_list
    obj_list.sort(key=lambda x: x.start_date, reverse=True)
    context = {
        "user":user,
        "obj_list": obj_list,
        "social": social,
        "template_urls": template_urls,
    }
    return render(request, 'resume/main.html', context)

def my_education_view(request):
    user, social, template_urls = inicialization()
    all_edu = MyEducation.objects.filter(user=user).order_by("end_date")
    certificates = MyCertificates.objects.all()
    edu = [item for item in all_edu]
    edu.sort(key=lambda x: x.start_date, reverse=True)
    page_is_active = "education"
    context = {
        "edu": edu,
        "user":user,
        "social": social,
        "page_is_active": page_is_active,
        "certificates": certificates,
        "template_urls": template_urls,
    }
    return render(request, 'resume/edu.html', context)

def my_work_view(request):
    user, social, template_urls = inicialization()
    all_work = MyWorkExperience.objects.filter(user=user).order_by("end_date")
    work = [item for item in all_work]
    work.sort(key=lambda x: x.start_date, reverse=True)
    page_is_active = "professional"
    context = {
        "work": work,
        "user":user,
        "social": social,
        "page_is_active": page_is_active,
        "template_urls": template_urls,
    }
    return render(request, 'resume/work.html', context)

def my_skills_view(request):
    user, social, template_urls = inicialization()
    tech_skill = (MySkills.objects.filter(skill_is_tech = True),"Tech Skills",)
    lang_skill = (MySkills.objects.filter(skill_is_language = True), "Languages")
    other_skill = (MySkills.objects.filter(skill_is_other = True), "Other Skils")
    soft_skill = (MySkills.objects.filter(skill_is_soft = True), "Soft skills")
    hobby_skill = (MySkills.objects.filter(skill_is_hobby = True), "Hobbies")
    skill_list = [tech_skill, lang_skill, other_skill, soft_skill, hobby_skill]
    page_is_active = "skills"
    context = {
        "skill_list":skill_list,
        "user":user,
        "social": social,
        "page_is_active": page_is_active,
        "template_urls": template_urls,
    }
    return render(request, 'resume/skills.html', context)

def my_projects_view(request):
    user, social, template_urls = inicialization()
    projects = MyProjects.objects.filter(user=user)
    page_is_active = "projects"
    context = {
        'projects':projects,
        "user": user, 
        "social": social,
        "page_is_active": page_is_active,
        "template_urls": template_urls,
    }
    return render(request, 'resume/projects.html', context)