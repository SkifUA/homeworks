from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='starter.html'), name='home'),
    url(r'^signin/$', TemplateView.as_view(template_name='signin.html'), name='home'),
    url(r'^cover/$', TemplateView.as_view(template_name='cover.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
