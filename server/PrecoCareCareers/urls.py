from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Authentication urls start 
    path('login/', views.LoginPage,name="login"),
    path('agent/', views.AgentRegister,name="agent"),
    path('logout/', views.LogoutUser,name="logout"),
    path('employee/', views.EmployeeRegister,name="employee"),
    # Authentication urls end 

    # password reset urls start  
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="Authentication/password_reset.html"
    ), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="Authentication/password_reset_sent.html"
    ), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="Authentication/password_reset_form.html"
    ),name="password_reset_confirm"),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="Authentication/password_reset_done.html"
    ), name="password_reset_complete"),
    # password reset urls end 



    path('',views.IndexPage,name='index'),
    path('details/<int:listing_id>',views.JobDetails,name='details'),
    path('about',views.AboutPage,name='about'),
    path('favourites',views.FavouriteJobs,name='favourites'),
    path('support',views.ContactUs,name='support'),


    # admin urls 
    path('dashboard',views.Dashboard,name='dashboard'),
    path('approved',views.Approved,name='approved'),
    path('candidate/<int:candidate_id>',views.ListedCandidates,name='candidate'),
    path('profile',views.ProfilePage,name='profile'),

]

htmx_urlpatterns = [
    path('title_search/',views.TitlesSearch, name="title_search"),
    path('create/',views.CreateTitle, name="create"),
    path('subscribe/',views.NewsLetter, name="subscribe"),
]

urlpatterns += htmx_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)