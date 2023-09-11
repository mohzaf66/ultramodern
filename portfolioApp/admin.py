from django.contrib import admin
from .models import Patient,PatientProposedTreatment,DentistProfile,Referral,TreatmentRequestFile,ImageUploadAdmin
# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientProposedTreatment)
admin.site.register(DentistProfile)
admin.site.register(Referral)
admin.site.register(TreatmentRequestFile)
admin.site.register(ImageUploadAdmin)
# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Querie)
# admin.site.register(Answer)