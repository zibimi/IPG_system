from django.conf.urls import patterns, include, url
from django.contrib import admin
from recruit import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^login/$', views.login),
    (r'^logout/$', views.logout),
    (r'^requisition/$', views.requisitionlist),
    (r'^candidate/$', views.partylist),
    (r'^submittal/$', views.submittallist),
#	(r'^timesheet/$', views.timesheetlist),
	
    (r'^add_party/$', views.add_party),
    (r'^add_submittal/$', views.add_submittal),
    (r'^add_requisition/$', views.add_requisition),
	
    (r'^get_recruiter/$', views.get_recruiter),
    (r'^get_candidate/$', views.get_candidate),
    (r'^get_requisition/$', views.get_requisition),
    (r'^get_skill/$', views.get_skill),
    (r'^get_party_skill/$', views.get_party_skill),
    (r'^get_submittal_tarck/$', views.get_submittal_tarck),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
#(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
#(r'^media-admin/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.MEDIA_ROOT, '..', settings.ADMIN_MEDIA_PREFIX)}),     
    url(r'^admin/', include(admin.site.urls)),
#url(r'^admin/', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)
