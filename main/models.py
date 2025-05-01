from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class PersonalInfo(models.Model):
    name = models.CharField('Name',max_length=50)
    img = models.ImageField('Image',upload_to='Images')
    img2 = models.ImageField('Image_2',upload_to='Images',null=True)
    about = models.TextField('About')
    birthday = models.DateField('Birthday')
    address = models.CharField('Address',max_length=255)
    email = models.EmailField('Email')
    phone = PhoneNumberField('Phone')
    complete_projects = models.IntegerField('Projects')
    github = models.URLField('GitHub')
    facebook = models.URLField('Facebook')
    instagram = models.URLField('Instagram')
    linkedin = models.URLField('LinkedIn')
    skill1 = models.CharField('Skill1',max_length=100)
    skill2 = models.CharField('Skill2',max_length=100)
    skill3 = models.CharField('Skill3',max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Personal Info'
        verbose_name_plural = 'Personal Infos'

class Education(models.Model):
    start_year = models.IntegerField('Start Year')
    end_year = models.IntegerField('End Year')
    degree_univer = models.CharField('Degree and University',max_length=255)
    faculty = models.CharField('Faculty',max_length=255)
    description = models.TextField('Description')

    def __str__(self):
        return self.degree_univer
    
    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

class Experience(models.Model):
    start_year = models.IntegerField('Start Year')
    end_year = models.IntegerField('End Year')
    experience = models.CharField('Experience',max_length=255)
    univer = models.CharField('Univer',max_length=255)
    description = models.TextField('Description')

    def __str__(self):
        return self.experience
    
    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

class Skills_Diagram(models.Model):
    skill_name = models.CharField('Skill Name',max_length=255)
    knowledge = models.IntegerField('Knowledge in percents')

    def __str__(self):
        return self.skill_name
    
    class Meta:
        verbose_name = 'Diagram_Skill'
        verbose_name_plural = 'Diagram_Skills'

class Skills(models.Model):
    skill_name = models.CharField('Skill Name',max_length=255)
    knowledge = models.IntegerField('Knowledge in percents')

    def __str__(self):
        return self.skill_name
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

class Services(models.Model):
    logo_class = models.CharField('Logo Class',max_length=255)
    service = models.CharField('Service',max_length=255)
    description = models.TextField('Description')

    def __str__(self):
        return self.service
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Projects(models.Model):
    img = models.ImageField('Image')
    project = models.CharField('Project Name',max_length=255)
    services = models.CharField('Services',max_length=255)

    def __str__(self):
        return self.project

    class Meta:
        verbose_name = 'Ptoject'
        verbose_name_plural = 'Projects' 

class ContactModel(models.Model):
    name = models.CharField('Name',max_length=50)
    email = models.EmailField('Email') 
    subject = models.CharField('Subject',max_length=255) 
    message = models.TextField('Message')     

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages' 

class Footer_info(models.Model):
    about = models.TextField('About')
    
    def __str__(self):
        return 'Footer'
    
class QRmodel(models.Model):
    qr_img = models.ImageField('Image',upload_to='Images')
    

class VisitorIP(models.Model):
    ip_address = models.GenericIPAddressField("ip")
    timestamp = models.DateTimeField("time")

    def __str__(self):
        return f'{self.ip_address}'
    
class VisitorJustEnterIP(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField('time')
    os = models.CharField(max_length=100, blank=True)
    browser = models.CharField(max_length=100, blank=True)
    device = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.device}'