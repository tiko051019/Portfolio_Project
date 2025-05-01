from Portfolio_Project.settings import EMAIL_HOST_USER
from django.contrib.sites.models import Site
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

                                # 16.16.217.17/portfolio/
                                #           ||
                                #           \/
        download_url = f'http://{'192.168.10.15:8000/'}{reverse("cv")}'    #<---change to real link?????????????????????????????????????
        
                                #<--- Change debug to False also 

        qr_image = qrcode.make(download_url)
        qr_image_path = 'media/resume_qr.png'
        qr_image.save(qr_image_path)
        qr_model = QRmodel.objects.create(qr_img ='resume_qr.png')

        user_agent_str = get_client_ip_divice(request)
        user_agent = parse(user_agent_str)

        device = {
            "is_mobile": user_agent.is_mobile,
            "is_tablet": user_agent.is_tablet,
            "is_pc": user_agent.is_pc,
            "os": user_agent.os.family,         # e.g. 'iOS', 'Windows'
            "browser": user_agent.browser.family,  # e.g. 'Safari', 'Chrome'
            "device": user_agent.device.family     # e.g. 'iPhone'
        }
        ip = get_client_ip(request)

        print(device)

        if not VisitorJustEnterIP.objects.filter(            
            ip_address=ip,
            os=user_agent.os.family,
            browser=user_agent.browser.family,
            device=user_agent.device.family).exists():

            VisitorJustEnterIP.objects.create(
            ip_address=ip,
            timestamp = timezone.now(),
            os=user_agent.os.family,
            browser=user_agent.browser.family,
            device=user_agent.device.family)
        
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

                                # 16.16.217.17/portfolio/
                                #           ||
                                #           \/
        download_url = f'http://{'192.168.15.135:8000'}{reverse("cv")}'    #<---change to real link?????????????????????????????????????
        
                                #<--- Change debug to False also 

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

        if form.is_valid() and not VisitorIP.objects.filter(ip_address=ip).exists():

            VisitorIP.objects.create(ip_address = ip,timestamp = timezone.now())

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
            if VisitorIP.objects.filter(ip_address=ip).exists():
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
    return render(request,'cv.html')











