from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.contrib import messages


from users.models import Profile, Education, Skill, Area,Experience,Achievement
from auth.models import RidUser
from users.edit_forms import ProfilePicForm, ContactInfoForm, SkillsForm, AddSkillForm
from users.edit_forms import AreasForm, AddAreaForm, EducationForm,ExperienceForm,AchievementForm,SummaryForm

class UpdateProfilePic(UpdateView):
    model = Profile
    template_name = "users/edit/profile_pic.html"
    form_class = ProfilePicForm
   
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        messages.success(self.request,'Profile Pic Updated successfully')
        return reverse('edit_profile_pic', kwargs={'slug':self.object.user})

class UpdateContactInfo(UpdateView):
    model = Profile
    template_name = "users/edit/contact_info.html"
    form_class = ContactInfoForm
   
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        messages.success(self.request,'Contact Info Updated successfully')
        return reverse('edit_contact_info', kwargs={'slug':self.object.user})

class UpdateSkills(UpdateView):
    model = Profile
    template_name = "users/edit/skills.html"
    form_class = SkillsForm
   
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        messages.success(self.request,'Skills Updated successfully')
        return reverse('edit_skills', kwargs={'slug':self.object.user})
        
class AddSkill(CreateView):
    model = Skill
    form_class = AddSkillForm
    template_name = "users/edit/skill_add.html"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'New Skill added successfully')
        return super(AddSkill, self).form_valid(form)

    def get_success_url(self):
        return reverse('edit_skills', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass


class UpdateAreas(UpdateView):
    model = Area
    template_name = "users/edit/areas.html"
    form_class = AreasForm
   
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        messages.success(self.request,'Areas Updated successfully')
        return reverse('edit_areas', kwargs={'slug':self.object.user})

class AddArea(CreateView):
    model = Area
    form_class = AddAreaForm
    template_name = "users/edit/area_add.html"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'New Area added successfully')
        return super(AddArea, self).form_valid(form)

    def get_success_url(self):
        return reverse('edit_areas', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass

#Education views start here


class EducationListView(ListView):
    model = Education
    template_name = "users/edit/education_list.html"

    def get_queryset(self):
         return Education.objects.filter(user=self.request.user).order_by("-id")
         
    def get_context_data(self, **kwargs):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
        context = super(EducationListView, self).get_context_data(**kwargs)
        return context
    
class UpdateEducation(UpdateView):
    model = Education
    template_name = "users/edit/education_form.html"
    form_class = EducationForm


    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Education.objects.get(id=self.kwargs['pk']).user.rid):
		raise PermissionDenied("Not allwoed to Edit others Education Details")
                
        return Education.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.success(self.request,'Education #%d updated successfully ' % int(self.kwargs['pk']))
        return reverse('education_list', kwargs={'slug':self.request.user})
    
class AddEducation(CreateView):
    model = Education
    template_name = "users/edit/education_form.html"
    form_class = EducationForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        form.save()
        return super(AddEducation, self).form_valid(form)

    def get_success_url(self): 
        messages.success(self.request,'New Education added successfully ')
        return reverse('education_list', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass

class DelEducation(DeleteView):
    model = Education
    template_name = "users/edit/education_del.html"
    
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Education.objects.get(id=self.kwargs['pk']).user.rid):
		raise PermissionDenied("Not allwoed to Edit others Education Details")
                
        return Education.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.warning(self.request,'Education #%d deleted successfully ' % int(self.kwargs['pk']))
        return reverse('education_list', kwargs={'slug':self.request.user})
        


#Experience views starts here

class ExperienceListView(ListView):
    model = Experience
    template_name = "users/edit/experience_list.html"

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user).order_by("-id")

    def get_context_data(self,**kwargs):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
        context = super(ExperienceListView, self).get_context_data(**kwargs)
        return context


class UpdateExperience(UpdateView):
    model = Experience
    template_name = "users/edit/experience_form.html"
    form_class = ExperienceForm


    def get_object(self, queryset=None):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Experience.objects.get(id=self.kwargs['pk']).user.rid):
            raise PermissionDenied("Not allwoed to Edit others Experience Details")
                
        return Experience.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.success(self.request,'Experience #%d updated successfully ' % int(self.kwargs['pk']))
        return reverse('experience_list', kwargs={'slug':self.request.user})
    
class AddExperience(CreateView):
    model = Experience
    template_name = "users/edit/experience_form.html"
    form_class = ExperienceForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        form.save()
        return super(AddExperience, self).form_valid(form)

    def get_success_url(self): 
        messages.success(self.request,'New Experience added successfully ')
        return reverse('experience_list', kwargs={'slug':self.request.user})

    def get_initial(self):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
        pass

class DelExperience(DeleteView):
    model = Experience
    template_name = "users/edit/experience_del.html"
    
    def get_object(self, queryset=None):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Experience.objects.get(id=self.kwargs['pk']).user.rid):
            raise PermissionDenied("Not allwoed to Edit others Experience Details")
                
        return Experience.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.warning(self.request,'Experience #%d deleted successfully ' % int(self.kwargs['pk']))
        return reverse('experience_list', kwargs={'slug':self.request.user})


#Achievement views starts here

class AchievementListView(ListView):
    model = Achievement
    template_name = "users/edit/achievement_list.html"

    def get_queryset(self):
        return Achievement.objects.filter(user=self.request.user).order_by("-id")

    def get_context_data(self,**kwargs):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
        context = super(AchievementListView, self).get_context_data(**kwargs)
        return context


class UpdateAchievement(UpdateView):
    model = Achievement
    template_name = "users/edit/achievement_form.html"
    form_class = AchievementForm


    def get_object(self, queryset=None):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Achievement.objects.get(id=self.kwargs['pk']).user.rid):
            raise PermissionDenied("Not allwoed to Edit others Achievement Details")
                
        return Achievement.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.success(self.request,'Achievement #%d updated successfully ' % int(self.kwargs['pk']))
        return reverse('achievement_list', kwargs={'slug':self.request.user})
    
class AddAchievement(CreateView):
    model = Achievement
    template_name = "users/edit/achievement_form.html"
    form_class = AchievementForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        form.save()
        return super(AddAchievement, self).form_valid(form)

    def get_success_url(self): 
        messages.success(self.request,'New Achievement added successfully ')
        return reverse('achievement_list', kwargs={'slug':self.request.user})

    def get_initial(self):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
        pass

class DelAchievement(DeleteView):
    model = Achievement
    template_name = "users/edit/achievement_del.html"
    
    def get_object(self, queryset=None):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Achievement.objects.get(id=self.kwargs['pk']).user.rid):
            raise PermissionDenied("Not allwoed to Edit others Achievement Details")
                
        return Achievement.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.warning(self.request,'Achievement #%d deleted successfully ' % int(self.kwargs['pk']))
        return reverse('achievement_list', kwargs={'slug':self.request.user})


#Summary views starts here


class UpdateSummary(UpdateView):
    model = Profile
    template_name = "users/edit/summary.html"
    form_class = SummaryForm


    def get_object(self, queryset=None):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
                
        return Profile.objects.get(user=RidUser.objects.get(rid=self.request.user.rid))
    
    def get_success_url(self):
        messages.success(self.request,'Summary updated successfully ')
        return reverse('summary_update', kwargs={'slug':self.request.user})

