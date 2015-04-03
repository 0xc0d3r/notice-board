
# importing django url patterns modules
from django.conf.urls import patterns, include, url
#from django.contrib.auth.decorators import login_required as auth
from .views import basic,university_info,contact_info,summary,education,areas,roles,skills,achievements,experiences,profile_pic


# auth url patterns
urlpatterns = patterns('',
    url(r'^basic_info/$', basic, name="api_basic_info"),
    url(r'^university_info/$', university_info, name="api_university_info"),
    url(r'^contact_info/$', contact_info, name="api_contact_info"),
    url(r'^profile_pic/$', profile_pic, name="api_profile_pic"),
    url(r'^summary/$', summary, name="api_summary"),
    url(r'^education/$', education, name="api_education_info"),
    url(r'^areas/$', areas, name="api_areas_info"),
    url(r'^roles/$', roles ,name="api_roles_info"),
    url(r'^skills/$', skills ,name="api_skills_info"),
    url(r'^achievements/$', achievements, name="api_achievements_info"),
    url(r'^experiences/$', experiences, name="api_experiences_info"),
)
 

