from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Patient,User,PatientProposedTreatment,DentistProfile,Referral,TreatmentRequestFile,ImageUploadAdmin
from django.contrib.auth.forms import UserCreationForm
from .forms import DentistProfileForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# Basic Pages
def index(request):
    context={
        'index':'active',
    }
    return render(request,'index.html',context)

def about(request):
    context={
        'about':'active',
    }
    return render(request,'about.html',context)

def blog(request):
    context={
        'blog':'active',
    }
    return render(request,'blog.html',context)

def blogdetail(request):
    context={
        'blog':'active',
    }
    return render(request,'blogdetail.html',context)

def contact(request):
    context={
        'contact':'active',
    }
    return render(request,'contact.html',context)

def dentists(request):
    context={
        'dentists':'active',
    }
    return render(request,'dentists.html',context)


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    if request.user.is_superuser:
        #Patients
        totalpatientscount=Patient.objects.count()
        #Referrals
        reftotalcount=Referral.objects.count()
    else:
        #Patients
        totalpatientscount=Patient.objects.filter(Dentist=request.user).count()
        #Referrals
        reftotalcount=Referral.objects.filter(Dentist=request.user).count()
    context={
        'dashboard':'active',
        'totalpatientscount':totalpatientscount,
        'reftotalcount':reftotalcount,
    }
    return render(request,'dashboard.html',context)

# Patients
@login_required(login_url='login')
def patients(request):
    if request.user.is_superuser:
        mypatients=Patient.objects.order_by("PatientName")
    else:
        mypatients=Patient.objects.filter(Dentist=request.user).order_by("PatientName")
    context={
        'patients':'active',
        'mypatients':mypatients,
    }

    return render(request,'patients.html',context)

@login_required(login_url='login')
def dentists(request):
    dentists=User.objects.order_by("first_name")
    context={
        'dentists':'active',
        'dentists':dentists,
    }
    return render(request,'dentists.html',context)

@login_required(login_url='login')
def addnewpatient(request):
    treatmentrequestfile=TreatmentRequestFile.objects.order_by('-id')[:1]
    if request.method=="POST":
        Dentist=request.user
        PatientName=request.POST.get('PatientName')
        PatientSurname=request.POST.get('PatientSurname')
        Clinic=request.POST.get('Clinic')
        TreatmentRequest=request.FILES.get('TreatmentRequest',default="images/Logo2.png")
        OralScanUpper=request.FILES.get('OralScanUpper',default="images/Logo2.png")
        OralScanLower=request.FILES.get('OralScanLower',default="images/Logo2.png")
        Image1=request.FILES.get('Image1',default="images/Logo2.png")
        Image2=request.FILES.get('Image2',default="images/Logo2.png")
        Image3=request.FILES.get('Image3',default="images/Logo2.png")
        ThreeDViewRequest=request.POST.get('ThreeDViewRequest',default="No")
        ArrangeCollection=request.POST.get('ArrangeCollection',default="NO")
        Status=request.POST.get('Status',default="In Progress")
        DentistNote=request.POST.get('DentistNote')
        AdminNote=request.POST.get('AdminNote',default="Not Added")
        patient=Patient(Dentist=Dentist,PatientName=PatientName,PatientSurname=PatientSurname,Clinic=Clinic,TreatmentRequest=TreatmentRequest,OralScanUpper=OralScanUpper,OralScanLower=OralScanLower,Image1=Image1,Image2=Image2,Image3=Image3,ThreeDViewRequest=ThreeDViewRequest,ArrangeCollection=ArrangeCollection,Status=Status,DentistNote=DentistNote,AdminNote=AdminNote)
        patient.save()
        messages.success(request,"Patient added successfully!")

    context={
        'dentists':'active',
        'treatmentrequestfile':treatmentrequestfile,
    }
    return render(request,'addnewpatient.html',context)

@login_required(login_url='login')
def patientdetail(request,id):
    patient=Patient.objects.get(id=id)
    proposed=PatientProposedTreatment.objects.filter(Patient=patient).order_by('-id')[:1]
    adminuploads=ImageUploadAdmin.objects.filter(Patient=patient).order_by('-id')[:1]
    if "Proposed" in request.POST:
        ProposedTreatment=request.FILES.get('ProposedTreatment',default="images/Logo2.png")
        Invoice=request.FILES.get('Invoice',default="images/Logo2.png")
        ThreeDViewProposed=request.FILES.get('ThreeDViewProposed',default="images/Logo2.png")
        InternalStatus=request.POST.get('InternalStatus',default="On")
        Proposed=PatientProposedTreatment(ProposedTreatment=ProposedTreatment,Invoice=Invoice,ThreeDViewProposed=ThreeDViewProposed,Patient=patient,user=request.user)
        Proposed.save()
        patient.Admin=request.POST.get('Note')
        patient.save()

    if "UploadImages" in request.POST:
        Image1=request.FILES.get('Image1',default="images/Logo2.png")
        Image2=request.FILES.get('Image2',default="images/Logo2.png")
        Image3=request.FILES.get('Image3',default="images/Logo2.png")
        imageupload=ImageUploadAdmin(Image1=Image1,Image2=Image2,Image3=Image3,Patient=patient,user=request.user)
        imageupload.save()

    if "SubmitStatus" in request.POST:
        patient.Status=request.POST.get('Status')
        patient.save()

    if "SubmitInternalStatus" in request.POST:
        patient.InternalStatus=request.POST.get('InternalStatus')
        patient.save()

    if "SubmitNote" in request.POST:
        if request.user.is_superuser:
            patient.AdminNote=request.POST.get('AdminNote')
            patient.save()
        else:
            patient.DentistNote=request.POST.get('DentistNote')
            patient.save()


    context={
        'patient':patient,
        'proposed':proposed,
        'adminuploads':adminuploads,
    }
    return render(request, 'patientdetail.html', context)

# Referrals
@login_required(login_url='login')
def referrals(request):
    if request.user.is_superuser:
        myreferrals=Referral.objects.order_by("PatientName")
    else:
        myreferrals=Referral.objects.filter(Dentist=request.user).order_by("PatientName")
    context={
        'referral':'active',
        'myreferrals':myreferrals,
    }

    return render(request,'referrals.html',context)

@login_required(login_url='login')
def addnewreferral(request):
    if request.method=="POST":
        Dentist=request.user
        PatientName=request.POST.get('PatientName')
        PatientPhone=request.POST.get('PatientPhone')
        PatientEmail=request.POST.get('PatientEmail')
        ReferralReason=request.POST.get('ReferralReason')
        Status=request.POST.get('Status',default="In Progress")
        referral=Referral(Dentist=Dentist,PatientName=PatientName,PatientPhone=PatientPhone,PatientEmail=PatientEmail,ReferralReason=ReferralReason,Status=Status)
        referral.save()
        messages.success(request,"Referral added successfully!")

    context={
        'referral':'active'
    }
    return render(request,'addnewreferral.html',context)

@login_required(login_url='login')
def referraldetail(request,id):
    referral=Referral.objects.get(id=id)
    
    if "SubmitStatus" in request.POST:
        referral.Status=request.POST.get('Status')
        referral.save()

    context={
        'referral':referral,
    }
    return render(request, 'referraldetail.html', context)


# Account
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method=='POST':
            username= request.POST.get('username')
            password= request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Incorrect Username or Password!")
        context={

        }
        return render(request,'login.html',context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)

            profile_form=DentistProfileForm(request.POST)
            
            if form.is_valid() and profile_form.is_valid():
                user=form.save()
                
                profile=profile_form.save(commit=False)
                profile.user=user
                profile.save()

                user=form.cleaned_data.get("username")
                messages.error(request,"Registration Successful")
                return redirect('login')
        else:
            form=CreateUserForm()
            profile_form=DentistProfileForm()
        context={
            'form':form,
            'profile_form':profile_form,
        }
        return render(request,'signup.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

    return render(request,'login.html',context)