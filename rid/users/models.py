from django.db import models
from auth.models import RidUser

from django.core.validators import RegexValidator

class Area(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title

class RolePermission(models.Model):
    title = models.CharField(max_length=20, unique=True)

    is_verified = models.BooleanField(
        default=False,
        verbose_name = "Is Admin Verified",
    )

    def __unicode__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(max_length=20, unique=True)
    permissions = models.ManyToManyField(RolePermission)
    
    is_verified = models.BooleanField(
        default=False,
        verbose_name = "Is Admin Verified",
    )

    
    def __unicode__(self):
        return self.title


        
class Profile(models.Model):

    phone_regex = RegexValidator(
        regex=r'^[0]?[789]{1}\d{9}$',
        message="Mobile No format error"
    )

    mobile = models.CharField(
        max_length=11,
        validators=[phone_regex],
        null=True,
        blank = True,
        verbose_name = "Mobile No",
    )

    url = models.URLField(
        max_length=40,
        null = True,
        blank = True,
        verbose_name = "Website / URL",
    )

    profile_pic = models.FileField(
        upload_to='profile_pic/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name="Profile Picture",
        default = 'profile_pic/default.jpg',
    )

    
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        blank = True,
    )

    summary = models.TextField(
        verbose_name="Summary",
        blank=True
    )

    areas = models.ManyToManyField(Area)
    skills = models.ManyToManyField(Skill)
    
    user = models.OneToOneField(RidUser, unique=True)

    def __unicode__(self):
        return unicode(self.user)


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=RidUser)

class UserRole(models.Model):

    role = models.ForeignKey(Role)

    is_verified = models.BooleanField(
        default=False,
        verbose_name = "Is Admin Verified",
    )
    
    user = models.ForeignKey(RidUser)

    def __unicode__(self):
        return unicode(self.user)
    

class Education(models.Model):

    school = models.CharField(
        verbose_name = "School / College / University",
        max_length = 128,
        null = False,
    )

    period = models.CharField(
        verbose_name = "Time Period of Education",
        max_length = 10,
        null = True,
        blank = True,
    )

    degree = models.CharField(
        verbose_name = "Degree ",
        max_length = 128,
        null = True,
        blank = True,
    )
    
    stream = models.CharField(
        verbose_name = "Field of Study",
        max_length = 10,
        null = True,
        blank = True,
    )

    grade = models.FloatField(
        verbose_name = "Grade",
        null = True,
        blank = True,
    )

    user = models.ForeignKey(RidUser)

    def __unicode__(self):
        return unicode(self.user)

    
class Experience(models.Model):
    
    organization = models.CharField(
        verbose_name = "Organization Name",
        max_length = 128,
        null = True,
        blank = True,
    )

    title = models.CharField(
        verbose_name = "Title or Position",
        max_length = 128,
        null = True,
        blank = True,
    )

    location = models.CharField(
        verbose_name = "Location",
        max_length = 128,
        null = True,
        blank = True,
    )

    period = models.CharField(
        verbose_name = "Time Period",
        max_length = 128,
        null = True,
        blank = True,
    )

    description = models.TextField(
        verbose_name = "Description",
        null = True,
        blank = True,
    )
    
    user = models.ForeignKey(RidUser)
    def __unicode__(self):
        return unicode(self.user)

    
class Achievement(models.Model):

    issuer = models.CharField(
        verbose_name = "Issuing Organization",
        max_length = 128,
        null = True,
        blank = True,
    )

    title = models.CharField(
        verbose_name = "Title or Position",
        max_length = 128,
        null = True,
        blank = True,
    )

    location = models.CharField(
        verbose_name = "Location",
        max_length = 128,
        null = True,
        blank = True,
    )

    period = models.CharField(
        verbose_name = "Time Period",
        max_length = 128,
        null = True,
        blank = True,
    )

    description = models.TextField(
        verbose_name = "Description",
        null = True,
        blank = True,
    )
    
    user = models.ForeignKey(RidUser)

    def __unicode__(self):
        return unicode(self.user)
