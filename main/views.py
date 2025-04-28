from Portfolio_Project.settings import EMAIL_HOST_USER
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.core.mail import EmailMessage
from django.conf import settings
from .models import *
from .forms import *

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


def profile(request):
    return render(request, 'your_template.html', {
        'MEDIA_URL': settings.MEDIA_URL,
    })



def Page404(request):
    return render(request,'404.html')                            