from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.contrib import admin
admin.autodiscover()


from .views import NoticesView
from .views import OneNoticeView
from .views import HomePageView
from .views import AddNotice
from .views import UpdateNotice
from .views import DelNotice

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', auth(HomePageView), name="home"),
    url(r'^notices/$', auth(NoticesView.as_view()), name="notices"),
    url(r'^notices/(E[234]){1}/$', auth(NoticesView.as_view()), name="notices_year"),
    url(r"^notices/(?P<pk>\d+)$", auth(OneNoticeView.as_view()), name="notice_detail"),
    url(r"^notices/(?P<action>(add))/$", auth(AddNotice.as_view()), name="notice_add"),
    url(r"^notices/(?P<pk>\d+)/(?P<action>update)/$", auth(UpdateNotice.as_view()), name="notice_update"),
    url(r"^notices/(?P<pk>\d+)/(?P<action>delete)/$", auth(DelNotice.as_view()), name="notice_delete"),
    url(r"^login/$", "django.contrib.auth.views.login", {"template_name": "login.html"}, name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login", name="logout"),
)
