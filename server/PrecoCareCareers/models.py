import email
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name


class AgentModel(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    verified = models.CharField(max_length=100,null=True, default='No' ,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name


class LocationModel(models.Model):
    location_name = models.CharField(max_length=300,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.location_name

class ProviceModel(models.Model):
    province_name = models.CharField(max_length=300,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.province_name

class JobTypeModel(models.Model):
    job_name = models.CharField(max_length=300,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.job_name

class JobStatusModel(models.Model):
    status_name = models.CharField(max_length=300,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.status_name

class Joblisting(models.Model):
    User = models.ForeignKey(User,null=True, on_delete=models.CASCADE , blank=True, related_name="user", default=None)
    agent = models.ForeignKey(AgentModel, on_delete=models.CASCADE , blank=True, related_name="employer", default=None)
    job_title = models.CharField(max_length=300,null=True)
    company = models.CharField(max_length=300,null=True)
    city = models.CharField(max_length=300,null=True)
    province = models.CharField(max_length=300,null=True)
    start_date = models.DateField(auto_now_add=False,null=True,blank=True)
    end_date = models.DateField(auto_now_add=False,null=True,blank=True)
    mon_fri = models.CharField(max_length=300,null=True)
    saturdays = models.CharField(max_length=300,null=True)
    sundays = models.CharField(max_length=300,null=True)
    holidays = models.CharField(max_length=300,null=True)
    job_status = models.CharField(max_length=300,null=True)
    contact_lenght = models.CharField(max_length=300,null=True)
    salary = models.CharField(max_length=300,null=True)
    open_positions = models.IntegerField(null=True,blank=True)
    requirements_1 = models.TextField(blank = True,null=True)
    requirements_2 = models.TextField(blank = True,null=True)
    requirements_3 = models.TextField(blank = True,null=True)
    extra_info = models.TextField(blank = True,null=True)
    deadline = models.DateField(auto_now_add=False,null=True,blank=True)
    start_date = models.DateField(auto_now_add=False,null=True,blank=True)
    application_status = models.CharField(max_length=300,null=True,default="Open")
    views = models.IntegerField(null=True,blank=True)
    paid_promo = models.CharField(max_length=300,null=True,default="No")
    favourite = models.ManyToManyField(Employee,related_name="user_favourite",blank=True,default=None)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.job_title

class ApplicantModel(models.Model):
    User = models.ForeignKey(User,null=True, on_delete=models.CASCADE , blank=True, related_name="applicant", default=None)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    doctor_lisence = models.CharField(max_length=200,null=True)
    exp1_titl2 = models.CharField(max_length=200,null=True)
    exp1_comp2ny = models.CharField(max_length=200,null=True)
    exp1_numb2r = models.CharField(max_length=20,null=True)
    exp2_title = models.CharField(max_length=200,null=True)
    exp2_company = models.CharField(max_length=200,null=True)
    exp2_number = models.CharField(max_length=20,null=True)
    date_1 = models.DateField(auto_now_add=False,null=True,blank=True)
    date_2 = models.DateField(auto_now_add=False,null=True,blank=True)
    joblisting =  models.ForeignKey(Joblisting,null=True, on_delete=models.CASCADE , blank=True, related_name="applied_applicant", default=None)
    accepted = models.CharField(max_length=100,null=True,default="Pending")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

class JobViews(models.Model):
    views_count = models.IntegerField(null=True,blank=True)
    joblisting =  models.ForeignKey(Joblisting,null=True, on_delete=models.CASCADE , blank=True, related_name="application_count", default=None)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __int__(self):
        return self.views_count


class CandidatesModel(models.Model):
    User = models.ForeignKey(User,null=True, on_delete=models.CASCADE , blank=True, related_name="userlistings", default=None)
    listing = models.ForeignKey(Joblisting, on_delete=models.CASCADE , blank=True, related_name="candidate", default=None)
    Accepted = models.CharField(max_length=100,null=True,default="No")
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    contact = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    doctor_licence = models.CharField(max_length=200,null=True)
    exp1_title = models.CharField(max_length=200,null=True)
    exp1_company = models.CharField(max_length=200,null=True)
    exp1_contact = models.CharField(max_length=200,null=True)
    exp2_title = models.CharField(max_length=200,null=True)
    exp2_company = models.CharField(max_length=200,null=True)
    exp2_contact = models.CharField(max_length=200,null=True)
    interview_date1 = models.DateField(auto_now_add=False,null=True,blank=True)
    interview_date2 = models.DateField(auto_now_add=False,null=True,blank=True)
    admin_creator = models.ForeignKey(AgentModel,null=True, on_delete=models.CASCADE , blank=True, related_name="creator", default=None)
    accepted_date = models.DateField(auto_now_add=False,null=True,blank=True)
    interview_time = models.CharField(max_length=100,null=True,default="No")
    day = models.CharField(max_length=100,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    resume = models.FileField(blank=True,null=True,upload_to='files/resumes')

    def __int__(self):
        return self.Accepted

class FavouritesModel(models.Model):
    favourite = models.CharField(max_length=200,null=True, default="Favourite")
    User = models.ForeignKey(User,null=True, on_delete=models.CASCADE , blank=True, related_name="favouriteuser", default=None)
    listing = models.ForeignKey(Joblisting, on_delete=models.CASCADE , blank=True, related_name="userfavouritelisting", default=None)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __int__(self):
        return self.favourite

class newsLetter(models.Model):
    userName = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=350,null=True)

    def __int__(self):
        return self.userName



