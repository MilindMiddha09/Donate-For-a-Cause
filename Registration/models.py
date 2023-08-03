from django.db import models

# Create your models here.
class Registration(models.Model):
    FirstName = models.TextField(blank=False,null=True,max_length=20);
    LastName = models.TextField(blank=False,null=True,max_length=20);
    BirthDate= models.DateField(blank=True,null=True);
    
    # BirthDate.format("%d-%m-%Y")

    Phone= models.TextField(blank=True,null=True);
    #Email = models.EmailField(blank=False,null=True,max_length=20);     
    Age = models.IntegerField(blank=False);
    MALE = "Male"
    FEMALE = "Female"
    NOT_SPECIFIED = "Not Specified"
    GENDER = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (NOT_SPECIFIED, "Not Specified"),
        
    ]
    Gender = models.CharField(
        max_length=20,
        choices=GENDER,
        default=MALE,
    )

    City = models.TextField(blank=False,null=True,max_length=20);
    State = models.TextField(blank=False,null=True,max_length=20);
    Address = models.TextField(blank=False,null=True,max_length=100);
    AadharNumber = models.TextField(blank=False,null=True,max_length=20);

    BloodGroup = models.TextField(blank=False,null=True,max_length=20);
    BodyWeight = models.IntegerField(blank=False);
    YES = "Yes"
    NO = "No"
    Covid = [
        (YES, "Yes"),
        (NO, "No"),
    ]
    Covid = models.CharField(
        max_length=20,
        choices=Covid,
        default=NO,
    )
    DISEASES = models.TextField(blank=True,null=True,max_length=20);
    Verification = models.FileField(upload_to='Registration/',blank=False,null=True, max_length=250)

