from resume.models import MyCertificates, MyEducation, MySkills, MySocial, MyUser, MyWorkExperience, MyProjects
from django.contrib import admin

# Register your models here.
admin.site.register(MyUser)
admin.site.register(MyWorkExperience)
admin.site.register(MyEducation)
admin.site.register(MyCertificates)
admin.site.register(MySkills)
admin.site.register(MySocial)
admin.site.register(MyProjects)