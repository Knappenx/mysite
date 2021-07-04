from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class MyUser(models.Model):
    user_name = models.CharField('First Name', max_length=20)
    user_middle_name = models.CharField('Middle Name', max_length=20, blank=True)
    user_last_name = models.CharField('Last Name', max_length=20)
    user_mothers_last_name = models.CharField("Mother's Last Name", max_length=20, blank=True)
    user_bio = models.TextField('Bio', max_length=1000)
    user_job_title = models.CharField('Job Title', max_length=50)
    user_email = models.EmailField('Email', max_length= 100)
    user_phone = models.CharField('Mobile', max_length= 20, default="x", blank=True)
    user_to_display = models.BooleanField('Show user cv', null=True, default=None, unique=True)

    def save(self, *args, **kwargs):
        if self.user_to_display is False:
            self.user_to_display = None
        super(MyUser, self).save(*args, **kwargs)

class MyWorkExperience(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    inst_name = models.CharField('Company Name', max_length=20)
    deg_or_pos = models.CharField('Job Position', max_length=40)
    company_fow = models.CharField('Field of Work',  max_length=60)
    company_url = models.URLField('Company Website',  max_length=200, blank=True)
    inst_logo = models.URLField('Company Logo URL',  max_length=200, blank=True)
    location_city = models.CharField('City', max_length=25)
    location_country = models.CharField('Country', max_length=25)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    current = models.BooleanField('Current Job', default=False)
    job_description = models.TextField('Job Description', max_length=1000)

class MyEducation(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    deg_or_pos = models.CharField('Degree', max_length=60)
    inst_name = models.CharField('Univeristy / Institution', max_length=60)
    inst_logo = models.URLField('Uni/Inst logo URL', max_length=200, blank=True)
    edu_url = models.URLField('Uni/Inst Website', max_length=200, blank=True)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    current = models.BooleanField('Currently Studying', default=False)
    activities = models.TextField('Description', max_length=1000, blank=True)

class MyCertificates(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    certificate = models.CharField('Certificate Name', max_length=30)
    certificate_desc = models.CharField('Certificate Description', max_length=50, blank=True)
    certificate_institution = models.CharField('Institution', max_length=50, blank=True)
    certificate_icon = models.CharField('Font Awesome Icon', max_length=30, blank=True)

class MySkills(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    skill_name = models.CharField('Skill', max_length=30)
    skill_description = models.CharField('Skill Description', max_length=60, blank=True)
    skill_icon = models.CharField('Font Awesome Icon', max_length=30, blank=True)
    skill_is_language = models.BooleanField('Language Skill', default=False, blank=True)
    skill_is_tech = models.BooleanField('Tech Skill', default=False, blank=True)
    skill_is_other = models.BooleanField('Other Skill', default=False, blank=True)
    skill_is_soft = models.BooleanField('Soft Skill', default=False, blank=True)
    skill_is_hobby = models.BooleanField('Hobby', default=False, blank=True)

class MySocial(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    social_name = models.CharField('Social Name (Ref only)', max_length=20)
    social_desc = models.CharField('Social name to display', max_length=30)
    social_url = models.URLField('Social URL', max_length=200, blank=True)
    social_icon = models.CharField('Font Awesome Icon', max_length=30, blank=True)
    social_is_contact = models.BooleanField('Contact info', default=False)

class MyProjects(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    project_name = models.CharField('Project Name', max_length=20)
    project_desc = models.TextField('Description', max_length=1000)
    project_code_url = models.URLField('Link to project', max_length=200, blank=True)
    project_live_url = models.URLField('Link to live page', max_length=200, blank=True)
    project_photo = models.URLField('Preview photo link', max_length=200, blank=True)
    project_techs = ArrayField(models.CharField(max_length=35, blank=True))