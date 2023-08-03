from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact
from Registration.models import Registration
from find.models import Find
from django.core.mail import send_mail

# Create your views here.
def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request,"main.html",{})



def reg_form(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request,"registration_form.html",{})

def find(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request,"find.html",{})

def about_us(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request,"about_us.html",{})

def contact(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request,"contact.html",{})

def results(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request,"results.html",{})

def save_contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject = request.POST.get('subject')
        message=request.POST.get('message')
        en = Contact(Name=name,Email=email,Subject = subject,Message=message)
        en.save()
    return render(request,'contact.html')

def save_reg(request):
    if request.method == 'POST' :
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        bday=request.POST.get('birthday')
        age=request.POST.get('age')
        
        gender=request.POST.get('gender')
        city=request.POST.get('city')
        address=request.POST.get('address')
        bgroup=request.POST.get('bloodgroup')
        state=request.POST.get('state')
        phone=request.POST.get('phone')
        aadhar=request.POST.get('aadhar')
        covid=request.POST.get('covid')
        weight=request.POST.get('weight')
        disease=request.POST.get('disease')
        verify=request.POST.get('verify')
        tn = Registration(FirstName=fname,LastName=lname,BirthDate=bday,Age=age,Gender=gender,City=city,Address=address,BloodGroup=bgroup,State=state,Phone=phone,AadharNumber=aadhar,Covid=covid,BodyWeight=weight,DISEASES=disease,Verification=verify)
        tn.save()
    return render(request,'registration_form.html')

# city = []
def save_find(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        c = request.GET.get('location')
        # city.append(c)
        # query = Registration.objects.filter(City = city)
        rn = Find(Name = name, Location = location)
        
        
    # query = Registration.objects.all()
    return render(request,'results.html')

def results(request):
    # location = save_find.location
    # city = 
    city = request.GET.get('location')
    c = city[1:]
    query = Registration.objects.filter(City__contains = c)
    return render(request,'results.html', {'query':query})



