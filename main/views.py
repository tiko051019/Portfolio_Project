from Portfolio_Project.settings import EMAIL_HOST_USER
from django.contrib.sites.models import Site
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.core.mail import EmailMessage
from django.http import FileResponse
from django.conf import settings
from django.urls import reverse
from .models import *
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
        download_url = f'http://{'192.168.15.135:8000'}{reverse("cv")}'    #<---change to real link?????????????????????????????????????
        
                                #<--- Change debug to False also 

        qr_image = qrcode.make(download_url)
        qr_image_path = 'media/resume_qr.png'
        qr_image.save(qr_image_path)

        qr_model = QRmodel.objects.create(qr_img='resume_qr.png')


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
        user_email = ContactModel.objects.all()
        emaill = request.POST.get('email')
        ls = []
        for i in user_email:
            ls.append(i.email)
        context = {
            'personal_info':personal_info,
            'education':education,
            'experience':experience,
            'skills':skills,
            'skills_diagram':skills_diagram,
            'services':services,
            'projects':projects,
            'footer_info':footer_info
        }
        if form.is_valid() and emaill not in ls:
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
            if emaill in ls:
                context['message'] = "You can't send more than one message with same email"
                return render(request,'index.html',context)
            else:
                context['message'] = form.errors

                render(request,'index.html',context)


def download_resume(request):
    file_path = os.path.join('static', 'files', 'Tigran_Abrahamyan_CV.pdf')
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response


def Page404(request):
    return render(request,'404.html')   


def cv(request):
    return render(request,'cv.html')











