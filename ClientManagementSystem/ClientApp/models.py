from django.db import models


class ClientModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    dateofjoining = models.DateField()
    STATUS_CHOICES = [('onboarded', 'Onboarded'),('not_onboarded', 'Not Onboarded'),]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    DOMAIN_CHOICES = [('sass', 'SaaS'),('ecommerce', 'E-Commerce'),('crm', 'CRM'),('erp', 'ERP'),('finance', 'Finance'),]
    projectdomain = models.CharField(max_length=20, choices=DOMAIN_CHOICES)
