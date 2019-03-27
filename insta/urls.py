from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^user/(?P<username>\w{0,50})',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^edit_profile/(?P<username>\w{0,50})',views.edit_profile,name='edit_profile'),
    # url(r'^new/profile$', views.new_profile, name='new_profile'),
    # url(r'^profile/',views.image,name='posts'),
    # url(r'new/post/$',views.image,name='newpost')
 
]      
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
