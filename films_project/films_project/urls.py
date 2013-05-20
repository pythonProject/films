from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from films_app import views
from films_project import settings
import django
from django.conf.urls.static import static
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('films_app.views',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^test_project/', include('test_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (u"^upload/$", views.RequiresLogin(views.UploadForm)),
    (u"^createAccount/$", 'CreateUser'),
    (u"^thanks/$", 'Thanks'),
    (u"^login/$", 'LoginView'),
    (u"^logged_in/$", views.RequiresLogin(views.Logged_in)),
    (u"^login_ajax/", views.LoginAjax),
    (u"^uploaded/$", views.uploaded),
    (u"^watching/$", views.watching),
    (u"^like/$", views.like),
    (u"^shortSearch/$", views.shortSearch),
    (u"^chat/$", views.Chat),
    (u"^", 'Index'),
)

#urlpatterns += patterns('',
#    url(r'^media/(?P<path>.*)$', django.views.static.serve, {
#        'document_root': settings.MEDIA_ROOT,
#        }),
#)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)