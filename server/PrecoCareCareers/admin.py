import email
from django.contrib import admin

from .models import AgentModel, ApplicantModel, CandidatesModel, Employee, FavouritesModel, JobStatusModel, JobTypeModel, JobViews, Joblisting, LocationModel, ProviceModel, newsLetter

# Register your models here.

class locacationModelAdmin(admin.ModelAdmin):
    list_display = (
        'location_name', 'date_created'
    )

class JobTypeModelAdmin(admin.ModelAdmin):
    list_display = (
        'job_name', 'date_created'
    )

class JobStatusModelAdmin(admin.ModelAdmin):
    list_display = (
        'status_name', 'date_created'
    )

class ProviceModelAdmin(admin.ModelAdmin):
    list_display = (
        'province_name', 'date_created'
    )

class JoblistingAdmin(admin.ModelAdmin):
    list_display = (
        'job_title','company','city','agent'
    )

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name','last_name','email','date_created'
    )

class ApplicantModelAdmin(admin.ModelAdmin):
    list_display = (
        'User', 'first_name','last_name','email', 'joblisting','accepted','date_created'
    )

class JobviewsCountAdmin(admin.ModelAdmin):
    list_display = (
        'views_count','joblisting','date_created'
    )

class CandidatesModelAdmin(admin.ModelAdmin):
    list_display = (
        'first_name','last_name','listing','Accepted'
    )

class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'userName', 'email'
    )

# class FavouritesAdmin(admin.ModelAdmin):
#     list_display = (
#         'User','Listing','date_created'
#     )

admin.site.register(LocationModel,locacationModelAdmin)
admin.site.register(JobTypeModel,JobTypeModelAdmin)
admin.site.register(JobStatusModel,JobStatusModelAdmin)
admin.site.register(ProviceModel,ProviceModelAdmin)
admin.site.register(Joblisting,JoblistingAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ApplicantModel,ApplicantModelAdmin)
admin.site.register(JobViews,JobviewsCountAdmin)
admin.site.register(CandidatesModel,CandidatesModelAdmin)
admin.site.register(FavouritesModel)
admin.site.register(newsLetter,NewsletterAdmin)

# Authentication models start 
class AgentModelAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name','last_name','email', 'verified','date_created'
    )

admin.site.register(AgentModel,AgentModelAdmin)

