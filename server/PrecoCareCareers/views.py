from collections import UserList
from typing import Counter
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q


# Authentication Imports start 
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user
from django.contrib.auth.models import Group
# Authentication Imports end 

from .models import AgentModel, CandidatesModel, Employee, FavouritesModel, JobStatusModel, JobTypeModel, JobViews, Joblisting, LocationModel, ProviceModel, newsLetter


# Send Email start 
from django.core.mail import send_mail


# Create your views here.



# Authentication Views start 

@unauthenticated_user
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
            
    return render(request, "Authentication/login.html")

# Agent Register view start 
@unauthenticated_user
def AgentRegister(request):
    form = CreateUserForm()
    if request.method == 'POST' and 'create-agent' in request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name= 'agent')
            user.groups.add(group)
            AgentModel.objects.create(
                user= user,
                first_name=username,
            )
            messages.success(request,'Account was created for ' + username)
            return redirect("login")

    context = {
        'form' : form
    }
    return render(request, "Authentication/agent_register.html", context)
# Agent Register View end 

# Employee Register View start 
@unauthenticated_user
def EmployeeRegister(request):
    form = CreateUserForm()
    if request.method == 'POST' and 'create-employee' in request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Employee.objects.create(
                user= user,
                first_name=username,
            )
            messages.success(request,'Account was created for ' + username)
            return redirect("login")

    context = {
        'form' : form
    }
    return render(request, "Authentication/register.html", context)
# Employee Register view end 

def LogoutUser(request):
    logout(request)
    return redirect('login')
# Authentication Views end 



def IndexPage(request):
    locations_list = LocationModel.objects.all().order_by('location_name')
    jobtype = JobTypeModel.objects.all().order_by('job_name')
    jobstatus = JobStatusModel.objects.all().order_by('status_name')
    userAuthenticated = request.user.is_authenticated
    if userAuthenticated:
        current_user = request.user
        userListing = CandidatesModel.objects.filter(User = current_user).values('listing')
        all_listings = Joblisting.objects.exclude(id__in= userListing)
    else:
        all_listings=Joblisting.objects.all()

    # Search Filter start 
    if userAuthenticated:
        if request.method == 'POST' and 'search-filter' in request.POST:
            current_user = request.user
            userListing = CandidatesModel.objects.filter(User = current_user).values('listing')
            all_listings = Joblisting.objects.exclude(id__in= userListing)
            title = request.POST.get('jobtitle')
            if title!=None:
                titleSearch =  all_listings.filter(job_title__icontains=title)
            
            location = request.POST.get('location')
            if location!=None:
                locationSearch =  titleSearch.filter(city__icontains=location)
            
            job = request.POST.get('jobstatus')
            if job!=None:
                jobSearch =  locationSearch.filter(job_status__icontains=job)

            all_listings = jobSearch
            
            context = {
                "locations_list": locations_list,
                "jobtype": jobtype,
                "jobstatus" : jobstatus,
                "all_listings" : all_listings
            }
            return render(request, 'PrecoCareCareers/index.html', context)
    else:
        if request.method == 'POST' and 'search-filter' in request.POST:
            all_listings = Joblisting.objects.all()
            title = request.POST.get('jobtitle')
            if title!=None:
                titleSearch =  all_listings.filter(job_title__icontains=title)
            
            location = request.POST.get('location')
            if location!=None:
                locationSearch =  titleSearch.filter(city__icontains=location)
            
            job = request.POST.get('jobstatus')
            if job!=None:
                jobSearch =  locationSearch.filter(job_status__icontains=job)

            all_listings = jobSearch
            
            context = {
                "locations_list": locations_list,
                "jobtype": jobtype,
                "jobstatus" : jobstatus,
                "all_listings" : all_listings
            }
            return render(request, 'PrecoCareCareers/index.html', context)

    # Adding Listing to user favourite start 
    if request.method == 'POST' and 'add-favourite' in request.POST:
        current_user = request.user
        listing = request.POST.get('listingId')
        jobId = Joblisting.objects.get(id = listing)
        save_favourite = FavouritesModel()
        save_favourite.User = current_user
        save_favourite.listing = jobId
        save_favourite.save()
        messages.success(request,'Listing added to My Listings')
        return redirect('favourites') 


    context = {
        "locations_list": locations_list,
        "jobtype": jobtype,
        "jobstatus" : jobstatus,
        "all_listings" : all_listings
    }
    return render(request, 'PrecoCareCareers/index.html', context)

def JobDetails(request,listing_id):
    job_details = Joblisting.objects.get(id = listing_id)

    if request.method == 'POST' and 'views_count' in request.POST:
        listing_id = request.POST.get('listing_id') 
        view_count = request.POST.get('listing_count')

        # adding the clicked view to the model count  
        view_id = JobViews.objects.get(joblisting = listing_id)
        views_value = view_id.views_count + int(view_count)
        # saving the added count 
        view_id.views_count = views_value
        view_id.save()

    if request.method == 'POST' and 'submit-application' in request.POST:
        current_user = request.user
        save_candidate = CandidatesModel()
        save_candidate.User = current_user
        save_candidate.first_name = request.POST.get('firstName')
        save_candidate.last_name = request.POST.get('lastName')
        save_candidate.contact = request.POST.get('phoneNumber')
        save_candidate.email = request.POST.get('EmailAddress')
        save_candidate.doctor_licence = request.POST.get('licenseNumber')
        save_candidate.exp1_title = request.POST.get('jobtitle')
        save_candidate.exp1_company = request.POST.get('companyName')
        save_candidate.exp1_contact = request.POST.get('companyPhone')
        save_candidate.exp2_title = request.POST.get('jobtitle2')
        save_candidate.exp2_company = request.POST.get('companyName2')
        save_candidate.exp2_contact = request.POST.get('companyPhone2')
        save_candidate.interview_date1 = request.POST.get('dateone')
        save_candidate.interview_date2 = request.POST.get('datetwo')
        listing_id = request.POST.get('listing_id')
        agentId = request.POST.get('agent_id')
        agentList = AgentModel.objects.get(id = agentId)
        save_candidate.admin_creator = agentList
        save_candidate.resume = request.FILES['resumeUpload']

        # getting listing from model and adding to users listing 
        list = Joblisting.objects.get(id = listing_id)
        save_candidate.listing = list
        save_candidate.save()
        messages.success(request,'application submited')
        return redirect('favourites') 


    context = {
        "job": job_details,
    }
    return render(request, 'PrecoCareCareers/job_details.html', context)

def AboutPage(request):
    return render(request, 'PrecoCareCareers/about.html')

def FavouriteJobs(request):
    current_user = request.user
    candidateListings = CandidatesModel.objects.filter(User = current_user)
    userFavourites = FavouritesModel.objects.filter(User = current_user)

    if request.method == 'POST' and 'remove-favourite' in request.POST:
        current_user = request.user
        listing = request.POST.get('listingId')
        jobId = FavouritesModel.objects.get(id = listing)
        jobId.delete()
        messages.success(request,'Listing removed from My Listings')

    # deregister user start 
    if request.method == 'POST' and 'deregisterUser' in request.POST:
        candidateId = request.POST.get('candidateId')
        candidateList = CandidatesModel.objects.get(id = candidateId)
        candidateList.delete()
        messages.success(request,'You have deregisted from the listing')

    context = {
        "userFavourites" : userFavourites,
        "candidateListings": candidateListings,
        
    }
    return render(request, 'PrecoCareCareers/favourite.html',context)

def ContactUs(request):
    return render(request, 'PrecoCareCareers/contact.html')


# Admin Dashboard start 
@allowed_user(allowed_roles=['agent'])
def Dashboard(request):
    current_user = request.user
    locations_list = LocationModel.objects.all().order_by('location_name')
    provice_list = ProviceModel.objects.all().order_by('province_name')
    jobstatus = JobStatusModel.objects.all().order_by('status_name')
    user_list = AgentModel.objects.get(user= current_user)
    agentOpenListing = Joblisting.objects.filter( Q(agent=user_list) & Q(application_status= "Open"))
    agentClosedListing = Joblisting.objects.filter( Q(agent=user_list) & Q(application_status= "Closed"))
    job_count = JobViews.objects.all()
    candidates = CandidatesModel.objects.all()
    


    if request.method == 'POST' and 'submit-listing' in request.POST:
        agent  = AgentModel.objects.get(user=current_user)
        create_job = Joblisting()
        create_job.User = current_user
        create_job.agent = agent
        create_job.job_title = request.POST.get('job_title') 
        create_job.company = request.POST.get('companyName') 
        create_job.city = request.POST.get('city')
        create_job.province = request.POST.get('province')
        create_job.start_date = request.POST.get('startdate')
        create_job.end_date = request.POST.get('enddate')
        create_job.mon_fri = request.POST.get('weekday')
        create_job.saturdays = request.POST.get('saturday')
        create_job.sundays = request.POST.get('Sunday')
        create_job.holidays = request.POST.get('holidays')
        create_job.job_status = request.POST.get('jobStatus')
        create_job.contact_lenght = request.POST.get('Contract')
        create_job.salary = request.POST.get('salary')
        create_job.open_positions = request.POST.get('positions')
        create_job.requirements_1 = request.POST.get('Requirements1')
        create_job.requirements_2 = request.POST.get('Requirements2')
        create_job.requirements_3 = request.POST.get('Requirements3')
        create_job.extra_info = request.POST.get('extra_info')
        create_job.deadline = request.POST.get('deadline')
        create_job.start_date = request.POST.get('applicantstart')
        create_job.save()

        # creating a view count for the created job listing start 
        create_view_count = JobViews()
        create_view_count.joblisting = create_job
        create_view_count.views_count = int(0)
        create_view_count.save()
        # creating a view count for the created job listing end
        messages.success(request,'New Listing Created')

    if request.method == 'POST' and 'update-Listing' in request.POST:
        jobID = request.POST.get('jobID')
        applicantId = Joblisting.objects.get(id = jobID)  
        applicantId.application_status = request.POST.get('applicantionStatus')
        applicantId.job_title = request.POST.get('job_title') 
        applicantId.company = request.POST.get('companyName') 
        applicantId.city = request.POST.get('city')
        applicantId.province = request.POST.get('province')
        start_date = request.POST.get('updatestartdate')
        if start_date:
            applicantId.start_date = start_date
        else:
            pass
        end_date = request.POST.get('updateEndDate')
        if end_date:
            applicantId.end_date = end_date
        else:
            pass
        applicantId.mon_fri = request.POST.get('weekday')
        applicantId.saturdays = request.POST.get('saturday')
        applicantId.sundays = request.POST.get('Sunday')
        applicantId.holidays = request.POST.get('holidays')
        applicantId.job_status = request.POST.get('jobStatus')
        applicantId.contact_lenght = request.POST.get('Contract')
        applicantId.salary = request.POST.get('salary')
        applicantId.open_positions = request.POST.get('positions')
        applicantId.requirements_1 = request.POST.get('Requirements1')
        applicantId.requirements_2 = request.POST.get('Requirements2')
        applicantId.requirements_3 = request.POST.get('Requirements3')
        applicantId.extra_info = request.POST.get('extra_info')
        deadline = request.POST.get('deadline')
        if deadline:
            applicantId.deadline = deadline
        else:
            pass
        applicantStart = request.POST.get('applicantstart')
        if applicantStart:
            applicantId.start_date = applicantStart
        else:
            pass
        applicantId.save()
        messages.success(request,'Listing Updated')   



    # Deleting Open listings Start 
    if request.method == 'POST' and 'deleteOpenListing' in request.POST:
        jobID = request.POST.get('jobID')
        applicantId = Joblisting.objects.get(id = jobID)
        applicantId.delete()
        messages.success(request,'Listing has been deleted')


    # Re-opening the closed listing start 
    if request.method == 'POST' and 'ReOpenListing' in request.POST:
        listingID = request.POST.get('closedAppId')
        closedListingId = Joblisting.objects.get(id = listingID)  
        closedListingId.application_status = request.POST.get('closedapplStatus')
        closedListingId.save()
        messages.success(request,'Listing has been reopened')

    # Deleting the closed listing start 
    if request.method == 'POST' and 'deleteClosedAppl' in request.POST:
        listingID = request.POST.get('closedAppId')
        deleteListing = Joblisting.objects.get(id = listingID)
        deleteListing.delete()
        messages.success(request,'Listing has been deleted')
        


    context = {
        "locations_list": locations_list,
        "provice_list" : provice_list,
        "jobstatus" : jobstatus,
        "agent_listings": agentOpenListing,
        "agentClosedListing" : agentClosedListing,
        "job_count" :job_count,
        "candidates" : candidates,


    }
    return render(request, 'PrecoCareCareers/dashboard.html', context)


@allowed_user(allowed_roles=['agent'])
def ListedCandidates(request,candidate_id):
    candidate_resume = CandidatesModel.objects.get(id = candidate_id)

    if request.method == 'POST' and 'applicant_status' in request.POST:
        applicant = CandidatesModel.objects.get(id = candidate_id)
        applicant.Accepted = request.POST.get('status')

        date_status = request.POST.get('interviewDate')
        if date_status:  
            applicant.accepted_date = request.POST.get('interviewDate')
            applicant.interview_time = request.POST.get('timeslot')
            applicant.day = request.POST.get('day')
        
        if date_status:
            candidateName = applicant.first_name
            candidateEmail = applicant.email
            candidatePosition = request.POST.get('positon')
            candidateCompany = request.POST.get('company')

            subject  = 'PrecoCare Careers Update'   
            msg = 'Hello' + ' ' + candidateName + ' ' + 'your job application for' + ' ' + candidatePosition + ' ' + 'position with' + ' ' + candidateCompany + ' ' + 'has been accepted for an Interview, Interview Date : ' + ' ' + applicant.accepted_date + ' ' + ', interview time : ' +   ' ' + applicant.interview_time + ' ' + applicant.day +  ' ' + ', please contact institution for more infomation.Thank you for choosing PrecoCare Careers.'
            to_email = candidateEmail
            send_mail(
                subject,
                msg,
                'precocare@gmail.com',
                [to_email]
            )
        else:
            candidateName = applicant.first_name
            candidateEmail = applicant.email
            candidatePosition = request.POST.get('positon')
            candidateCompany = request.POST.get('company')

            subject  = 'PrecoCare Careers Update'   
            msg = 'Hello' + ' ' + candidateName + ' ' + 'your job application for' + ' ' + candidatePosition + ' ' + 'position with' + ' ' + candidateCompany + ' ' + 'has been' + ' ' + applicant.Accepted + ' ' + 'please contact institution for more infomation.Thank you for choosing PrecoCare Careers.'
            to_email = candidateEmail
            send_mail(
                subject,
                msg,
                'precocare@gmail.com',
                [to_email]
            )

        applicant.save()
        messages.success(request,'Candidate Status Updated')
        return redirect('approved') 



    context = {
        "candidate" : candidate_resume
    }
    return render(request, "Admin/listing_details.html",context)


@allowed_user(allowed_roles=['agent'])
def Approved(request):
    current_user = request.user
    listing_agent = AgentModel.objects.get(user = current_user)
    candidatesInterviews = CandidatesModel.objects.filter( Q(admin_creator=listing_agent) & Q(Accepted= "Interview") )
    candidatesApproved = CandidatesModel.objects.filter( Q(admin_creator=listing_agent) & Q(Accepted= "Accept") )
    locations_list = LocationModel.objects.all().order_by('location_name')
    provice_list = ProviceModel.objects.all().order_by('province_name')


    context = {
        "candidatesInterviews" : candidatesInterviews,
        "candidatesApproved": candidatesApproved,
        "locations_list": locations_list,
        "provice_list" : provice_list
    }
    
    return render(request, 'PrecoCareCareers/approved.html',context)


@allowed_user(allowed_roles=['agent'])
def ProfilePage(request):
    current_user = request.user
    profile = AgentModel.objects.get(user = current_user)

    if request.method == 'POST' and 'EditSubmit' in request.POST:
        agentid = request.POST.get('AgentId')
        agentEdit = AgentModel.objects.get(id = agentid)
        agentEdit.first_name = request.POST.get('firstName')
        agentEdit.last_name = request.POST.get('lastName')
        agentEdit.save()
        messages.success(request,'Profile successfully updated')

    if request.method == 'POST' and 'DeleteAgent' in request.POST:
        agentid = request.POST.get('AgentId')
        agentEdit = AgentModel.objects.get(id = agentid)
        agentEdit.delete()
        current_user = request.user
        current_user.delete()
        messages.success(request,'Profile successfully Deleted')
        return redirect('index')
        


    context = {
        "profile" : profile
    }
    return render(request,"Admin/profile.html",context)




# Job titles search component start HTMX START

def TitlesSearch(request):
    searchResult = request.POST.get('title')
    titles = JobTypeModel.objects.filter(job_name__icontains= searchResult)

    context = {
        "titles" : titles
    }
    
    return render(request,'partials/titles.html',context)

def CreateTitle(request):
    getTitle = request.POST.get('title')
    
    create = JobTypeModel()
    create.job_name = getTitle
    create.save()

    print(getTitle)
    return render(request,'partials/create_title.html')

def NewsLetter(request):
    username = request.POST.get('NameNewsletter')
    getEmail = request.POST.get('EmailNewsletter') 

    subcribe = newsLetter()
    subcribe.userName =  username 
    subcribe.email = getEmail
    subcribe.save()
    
    return render(request ,'partials/subscribe.html')

# Job titles search component end   HTMX END 



# Admin Dashboard end 
