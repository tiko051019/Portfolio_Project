from Portfolio_Project.settings import EMAIL_HOST_USER
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.core.mail import EmailMessage
from django.http import FileResponse
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from user_agents import parse
from .models import *
from .utils import *
from .forms import *
import qrcode
import os

class PortfolioListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        personal_info = PersonalInfo.objects.get()
        education = Education.objects.all()
        experience = Experience.objects.all()
        skills = Skills.objects.all()
        skills_diagram = Skills_Diagram.objects.all()
        services = Services.objects.all()
        projects = Projects.objects.all()
        footer_info = Footer_info.objects.get()

        download_url = f'{request.scheme}://{request.get_host()}{reverse("cv")}'
        print(download_url)   
                

        qr_image = qrcode.make(download_url)
        qr_image_path = 'media/resume_qr.png'
        qr_image.save(qr_image_path)
        qr_model = QRmodel.objects.create(qr_img ='resume_qr.png')



        ipv4 = get_client_ipv4(request)
        user_agent_str = get_client_ipv4_divice(request) 
        user_agent = parse(user_agent_str)

        ip_public = show_ip(request)
        geolocation = get_geo_location(ip_public)

        device_type = user_agent.device.family
        if device_type == "Other":
            if user_agent.is_pc:
                device_type = "PC"
            elif user_agent.is_mobile:
                device_type = "Mobile"
            elif user_agent.is_tablet:
                device_type = "Tablet"

        if not VisitorData.objects.filter(
        ipv4=ipv4,
        ipv6=geolocation.get("ip"), 
        os=user_agent.os.family,
        browser=user_agent.browser.family,
        device=device_type,
        hostname=geolocation.get("hostname"),
        city=geolocation.get("city"),
        region=geolocation.get("region"),
        country=geolocation.get("country"),
        loc=geolocation.get("loc"),
        org=geolocation.get("org")).exists():
        
            VisitorData.objects.create(
            ipv4=ipv4,
            ipv6=geolocation.get("ip"), 
            os=user_agent.os.family,
            browser=user_agent.browser.family,
            device=device_type,
            hostname=geolocation.get("hostname"),
            city=geolocation.get("city"),
            region=geolocation.get("region"),
            country=geolocation.get("country"),
            loc=geolocation.get("loc"),
            org=geolocation.get("org"),
            timestamp=timezone.now())

        #-------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------
        
        context = {
            'personal_info':personal_info,
            'education':education,
            'experience':experience,
            'skills':skills,
            'skills_diagram':skills_diagram,
            'services':services,
            'projects':projects,
            'footer_info':footer_info,
            'qr_model': qr_model
        }

        return render(request,self.template_name,context)

    def post(self,request):

        personal_info = PersonalInfo.objects.get()
        education = Education.objects.all()
        experience = Experience.objects.all()
        skills = Skills.objects.all()
        skills_diagram = Skills_Diagram.objects.all()
        services = Services.objects.all()
        projects = Projects.objects.all()
        footer_info = Footer_info.objects.get()

        form = ContactMessageForm(request.POST)


        download_url = f'{request.get_host()}{reverse("cv")}'    

        qr_image = qrcode.make(download_url)
        qr_image_path = 'media/resume_qr.png'
        qr_image.save(qr_image_path)

        qr_model = QRmodel.objects.create(qr_img ='resume_qr.png')

        context = {
            'personal_info':personal_info,
            'education':education,
            'experience':experience,
            'skills':skills,
            'skills_diagram':skills_diagram,
            'services':services,
            'projects':projects,
            'footer_info':footer_info,
            'qr_model': qr_model

        }

        ip = get_client_ip(request)

        if form.is_valid() and not VisitorWriterIP.objects.filter(ip_address=ip).exists():

            VisitorWriterIP.objects.create(ip_address = ip,timestamp = timezone.now())

            form.save()
            email = EmailMessage(
                subject = f'Admininstrative unswer to {request.POST.get('name')}',
                body = "I'll contact you soon",
                from_email=EMAIL_HOST_USER,
                to = [request.POST.get('email')]
            )
            email.send()

            email2 = EmailMessage(
                subject = f'{request.POST.get('name')} Wrote you',
                body = f"{request.POST.get('email')}\n{request.POST.get('subject')}\n{request.POST.get('message')}",
                from_email=EMAIL_HOST_USER,
                to = [EMAIL_HOST_USER]
            )
            email2.send()
            
            return redirect('portfolio')

        else:
            if VisitorWriterIP.objects.filter(ip_address=ip).exists():
                context['message'] = 'You can send message only once. If you have more questions please write directly'
                return render(request,'index.html',context)
            else:
                context['message'] = form.errors

                return render(request,'index.html',context)



def download_resume(request):
    file_path = os.path.join('static', 'files', 'Tigran_Abrahamyan_CV.pdf')
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response


def Page404(request):
    return render(request,'404.html')   


def cv(request):
    cv = PersonalInfo.objects.get()
    return render(request,'cv.html',{'cv':cv})











