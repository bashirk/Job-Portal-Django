from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth

from jobapp.models import *
from ckeditor.widgets import CKEditorWidget

from account.models import User


    

class JobForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Task Title :"
        self.fields['location'].label = "Task Location :"
        self.fields['salary'].label = "Amount(NGN) :"
        self.fields['description'].label = "Task Description :"
        self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Task Deadline :"
        self.fields['company_name'].label = "Business Name :"
        self.fields['url'].label = "Website :"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg: Design logo for a logistics company',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg: Lagos',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': 'NGN800 - NGN12000',
            }
        )
        self.fields['tags'].widget.attrs.update(
            {
                'placeholder': 'Use comma separated. eg: Python, JavaScript ',
            }
        )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
                
            }
        )        
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Company Name',
            }
        )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )


    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "tags",
            "last_date",
            "company_name",
            "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            pass
            # raise forms.ValidationError("Skill Level is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            pass
            # raise forms.ValidationError("category is required")
        return category


    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)
        if commit:
            user.save()
        return job




class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['job']

class JobBookmarkForm(forms.ModelForm):
    class Meta:
        model = BookmarkJob
        fields = ['job']



class JobEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Task Title :"
        self.fields['location'].label = "Task Location :"
        self.fields['salary'].label = "Amount(NGN) :"
        self.fields['description'].label = "Task Description :"
        # self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Task Deadline :"
        self.fields['company_name'].label = "Business Name :"
        self.fields['url'].label = "Website :"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Software Developer',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : Lagos',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': 'NGN800 - NGN120O0',
            }
        )
        # self.fields['tags'].widget.attrs.update(
        #     {
        #         'placeholder': 'Use comma separated. eg: Python, JavaScript ',
        #     }
        # )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
            }
        )        
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Company Name',
            }
        )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )    

    
        last_date = forms.CharField(widget=forms.TextInput(attrs={
                    'placeholder': 'Service Name',
                    'class' : 'datetimepicker1'
                }))

    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "last_date",
            "company_name",
            "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            pass
            # raise forms.ValidationError("Skill Level is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            pass
            # raise forms.ValidationError("category is required")
        return category


    def save(self, commit=True):
        job = super(JobEditForm, self).save(commit=False)
        if commit:
            user.save()
        return job

# Paystack CustomerInfo for payment
class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
