from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class DentistProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Phone= models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.user)
    

class Patient(models.Model):
    Dentist=models.ForeignKey(User,on_delete=models.CASCADE)
    PatientName=models.CharField(max_length=100)
    PatientSurname=models.CharField(max_length=100,null=True)
    Clinic=models.CharField(max_length=300)
    TreatmentRequest=models.FileField(null=True)
    OralScanUpper=models.FileField(null=True)
    OralScanLower=models.FileField(null=True)
    Image1=models.ImageField(null=True)
    Image2=models.ImageField(null=True)
    Image3=models.ImageField(null=True)
    ThreeDViewRequest=models.CharField(max_length=20,null=True)
    ArrangeCollection=models.CharField(max_length=20,null=True)
    DentistNote=models.TextField(default="Not Added")
    AdminNote=models.TextField(default="Not Added")
    Status=models.CharField(max_length=20,default="Pending",null=True,choices=(("Accept","Accept"),("Review","Review"),("Decline","Decline")
    ))
    InternalStatus=models.TextField(null=True,default="On")
    Date=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + "  |  " + self.PatientName + "  |  " + str(self.Date) 
    
class PatientProposedTreatment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    ProposedTreatment=models.FileField(null=True)
    ThreeDViewProposed=models.FileField(null=True)
    Invoice=models.FileField(null=True)
    Time=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.Patient) + " | " + self.user.username + " | " + str(self.Time)

class ImageUploadAdmin(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    Image1=models.FileField()
    Image2=models.FileField()
    Image3=models.FileField()
    Time=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.Patient) + " | " + self.user.username + " | " + str(self.Time)


class Referral(models.Model):
    Dentist=models.ForeignKey(User,on_delete=models.CASCADE)
    PatientName=models.CharField(max_length=50)
    PatientPhone=models.CharField(max_length=20)
    PatientEmail=models.CharField(max_length=40)
    ReferralReason=models.CharField(max_length=60,default="Consultation",null=True,choices=(("Consultation","Consultation"),("Implant","Implant"),("Orthodontics","Orthodontics"),("Root Canal Treatment","Root Canal Treatment"),("Implant","Crown and Veneers")
    ))
    Status=models.CharField(max_length=40,default="In Progress",null=True,choices=(("Inprogress","Inprogress"),("Accepted","Accepted"),("TC","TC"),("Declined","Declined")
    ))
    Date=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + "  |  " + self.PatientName + "  |  " + str(self.Date) 

class TreatmentRequestFile(models.Model):
    File=models.FileField()
    

# class Post(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     Title=models.CharField(max_length=150)
#     slug = models.SlugField(unique=True,null=True,blank=True)
#     Meta_Tags = models.CharField(max_length=200,)
#     Description=models.TextField()
#     Category=models.CharField(max_length=50)
#     Body=RichTextUploadingField()
#     Date=models.DateField(auto_now_add=True)   
#     Views=models.IntegerField(default=0,null=True)
#     Likes=models.IntegerField(default=0,null=True)
#     Dis_Likes=models.IntegerField(default=0,null=True)
#     CommentsCounts=models.IntegerField(default=0,null=True)
#     def __str__(self):
#         return self.Title + " | " + str(self.Date)

# def createslug(instance,new_slug=None):
#     slug=slugify(instance.Title)
#     if new_slug is not None:
#         slug=new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists=qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug,qs.first().id)
#         return createslug(instance,new_slug=new_slug)
#     return slug
# def pre_save_post_receiver(sender,instance,*args, **kwargs):
#     if not instance.slug:
#         instance.slug=createslug(instance)
# pre_save.connect(pre_save_post_receiver,Post)

# class Comment(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     Post=models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
#     Body=models.TextField(null=True)
#     Time=models.DateTimeField(auto_now_add=True,null=True)
#     def __str__(self):
#         return str(self.Post) + " | "  + self.Body + " | " + self.user.username + " | " + str(self.Time)        
