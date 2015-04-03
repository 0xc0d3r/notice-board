# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from users.edit_views import UpdateProfilePic, UpdateContactInfo, EducationListView, UpdateSkills, AddSkill
from users.edit_views import AddArea, UpdateAreas, UpdateEducation, AddEducation, DelEducation
from users.edit_views import UpdateExperience,DelExperience,AddExperience,ExperienceListView
from users.edit_views import AchievementListView,UpdateAchievement,AddAchievement,DelAchievement
# auth url patterns
urlpatterns = patterns('',
    url(r"^contact_info/$", auth(UpdateContactInfo.as_view()), name="edit_contact_info"),
    url(r"^profile_pic/$", auth(UpdateProfilePic.as_view()), name="edit_profile_pic"),
    url(r"^education/$", auth(EducationListView.as_view()), name="education_list"),
    url(r"^education/add$", auth(AddEducation.as_view()), name="education_add"),
    url(r"^education/(?P<pk>[0-9]+)/update$", auth(UpdateEducation.as_view()), name="education_update"),
    url(r"^education/(?P<pk>[0-9]+)/delete$", auth(DelEducation.as_view()), name="education_del"),
    url(r"^experience/$", auth(ExperienceListView.as_view()), name="experience_list"),
    url(r"^experience/add$", auth(AddExperience.as_view()), name="experience_add"),
    url(r"^experience/(?P<pk>[0-9]+)/update$", auth(UpdateExperience.as_view()), name="experience_update"),
    url(r"^experience/(?P<pk>[0-9]+)/delete$", auth(DelExperience.as_view()), name="experience_del"),
    url(r"^skills/$", auth(UpdateSkills.as_view()), name="edit_skills"),
    url(r"^skills/add$", auth(AddSkill.as_view()), name="skill_add"),
    url(r"^areas/$", auth(UpdateAreas.as_view()), name="edit_areas"),
    url(r"^areas/add$", auth(AddArea.as_view()), name="area_add"),
    url(r"^achievements/$", auth(AchievementListView.as_view()), name="achievement_list"),
    url(r"^achievements/add$", auth(AddAchievement.as_view()), name="achievement_add"),
    url(r"^achievements/(?P<pk>[0-9]+)/update$", auth(UpdateAchievement.as_view()), name="achievement_update"),
    url(r"^achievements/(?P<pk>[0-9]+)/delete$", auth(DelAchievement.as_view()), name="achievement_del"),
)
 

