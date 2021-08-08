from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


JOB_TYPE = (
    ('1', "Expert"),
    ('2', "Intermediate"),
    ('3', "Beginner"),
)

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name="Task Category")

    def __str__(self):
        return self.name
    

class Job(models.Model):

    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300, verbose_name="Task Title")
    description = RichTextField(blank=False, null=False, verbose_name="Task Description")
    tags = TaggableManager(blank=True)
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1, blank=True, verbose_name="Skill Level")
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Task Category")
    salary = models.CharField(max_length=30, verbose_name="Amount(NGN)")
    company_name = models.CharField(max_length=300, verbose_name="Business Name")
    company_description = RichTextField(blank=True, null=True, verbose_name="Business Description")
    url = models.URLField(max_length=200, blank=True)
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

 

class Applicant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Task")
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title

'''
class TaskOwner(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Task")
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title

'''
  

class BookmarkJob(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Task")
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title

# Pypaystack CustomerInfo for payment
'''
class CustomerInfo(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Full Name")
    email = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Email")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    address = models.CharField(max_length=150, verbose_name="Address")
'''
