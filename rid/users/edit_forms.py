from django import forms
from users.models import Profile,Skill, Area, Education, Experience
from django.forms.widgets import CheckboxSelectMultiple  

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        #exclude = ("mobile","url","email","summary","skills","areas",)
	fields = ['profile_pic']
        widgets = {
           'profile_pic' : forms.FileInput(attrs={'id':'attachmentName','style' : 'display:none;',}),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
	fields = ['url','email','mobile']
        widgets = {
           'url' : forms.URLInput(attrs={'placeholder':'Enter your website / blog url'}),
           'email' : forms.EmailInput(attrs={'placeholder':'Enter your email address '}),
           'mobile' : forms.TextInput(attrs={'placeholder':'Enter your mobile number', 'style':'max-length:11'}),
        }

class AddSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fileds = ['title',]
        widget = {
            'title' : forms.TextInput(attrs={'placeholder':'Enter your title',}),
        }

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Profile
	fields = ['skills',]

    def __init__(self, *args, **kwargs):

        super(SkillsForm, self).__init__(*args, **kwargs)

        self.fields["skills"].widget = CheckboxSelectMultiple()
        self.fields["skills"].queryset = Skill.objects.all() 


class AddAreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fileds = ['title',]
        widget = {
            'title' : forms.TextInput(attrs={'placeholder':'Enter your title',}),
        }

class AreasForm(forms.ModelForm):
    class Meta:
        model = Profile
	fields = ['areas',]

    def __init__(self, *args, **kwargs):

        super(AreasForm, self).__init__(*args, **kwargs)

        self.fields['areas'].widget = CheckboxSelectMultiple()
        self.fields["areas"].queryset = Area.objects.all() 

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ("user",)
        fileds = ['school','period','degree','stream','grade']
        
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ("user",)
        fields=['organization','title','location','period','description']