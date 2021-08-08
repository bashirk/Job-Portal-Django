from django.contrib.auth.models import AbstractUser, User
from django.db import models

from account.managers import CustomUserManager

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),

)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(null=True, unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)
    phone_number = models.CharField(default="Phone Number", max_length=20, verbose_name="Phone Number")
    address = models.CharField(default="Address", max_length=150, verbose_name="Address")
    #added employee salary
    emp_salary = models.FloatField(default=0.0, max_length=30, verbose_name="Rate Per Task (₦)", blank=True, null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_len_name(self):
        return self.first_name + ' ' + self.last_name

    def get_first_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name[0] + '.'

    def get_emp_salary(self):
        return self.emp_salary

    def get_emp_salary_total(self):
        return self.emp_salary + (self.emp_salary*0.1)

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    objects = CustomUserManager()
