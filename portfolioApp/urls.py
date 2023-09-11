from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Admin Panel Title
admin.site.site_header="UKALIGNERS Admin Login"
admin.site.site_title="UKALIGNERS Administration"

urlpatterns = [

    #Basic Pages
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blogdetail', views.blogdetail, name='blogdetail'),
    path('contact/', views.contact, name='contact'),
    path('dentists', views.dentists, name='dentists'),
    #Dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    #Dentists pages
    path('dentists', views.dentists, name='dentists'),
    #Patients pages
    path('patients', views.patients, name='patients'),
    path('addnewpatient', views.addnewpatient, name='addnewpatient'),
    path('patientdetail/<int:id>/', views.patientdetail, name='patientdetail'),
    #Referrals Pages
    path('referrals', views.referrals, name='referrals'),
    path('addnewreferral', views.addnewreferral, name='addnewreferral'),
    path('referraldetail/<int:id>/', views.referraldetail, name='referraldetail'),
    #Accounts pages
    path('login', views.loginuser, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutuser, name='logout'),
    
    #cdeditor
    path('ckeditor',include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
