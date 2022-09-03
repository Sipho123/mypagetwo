from logging import RootLogger
from operator import concat
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
#from django.conf import settings

# Create your views here.


#def get_in_touch(request):
    #if request.method=="POST":
        #contact=Contact()
        #name = request.POST.get('name')
        #email = request.POST.get('email')
        #massage = request.POST.get('massage')
        #subject = request.POST.get('subject')
        #contact.name=name
        #contact.email=email
        #contact.massage=massage
        #contact.subject=subject
        #contact.save()
    
        #return HttpResponse("<h1>THANKS FOR CONTACTING US</h1>")
    #return render(request,'get_in_touch/get_in_touch.html')

    
def get_in_touch(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        subject = request.POST.get('subject')
        last_name = request.POST.get('last-name')
        company_name = request.POST.get('company-name')
        role = request.POST.get('role')
        phone_number = request.POST.get('phone-number')
        # send an email
        #send_mail(
        #    name, #subject
        #    massage, #msg
         #   email, #from email
         #   ['buyilemgwezani@gmail.com'],# To Email
        #)
    
        return render(request,'get_in_touch/get_in_touch.html', {'name': name})
    else: 
        return render(request, 'get_in_touch/get_in_touch.html', {})

def consultation(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        subject = request.POST.get('subject')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company-name')
        role = request.POST.get('role')
        phone_number = request.POST.get('phone-number')
        address = request.POST.get('address')
        schadule = request.POST.get('schadule')
        time = request.POST.get('time')
        date = request.POST.get('date')

        # send an email
#        Consunltation = 'Date: " + date + " Time: " + time + " Name: " + name + " Last_name: " + last_name + " Company_name: " + company_name + " Role: " + role + " Phone_number: " + phone_number + " Address: " + address + " Email: " + email + "  Massage: " +  massage "'
#        send_mail(
#            'Consultation Request', #Subject
#            consultation, #massage
#            email, #from email
#            ['buyilemgwezani@gmail.com'],# To Email
#        )

    
        return render(request, 'get_in_touch/consultation.html', {
            
            'date' : date,
            'time' : time,
            'name' : name,
            'last_name' : last_name,
            'company_name' : company_name,
            'role' : role,
            'phone_number': phone_number,
            'subject' : subject,
            'email' : email,
            'address' : address,
            'massage' : massage,
        })
    
    else: 
        return render(request, 'get_in_touch/consultation.html', {})

                
                
                
                        
