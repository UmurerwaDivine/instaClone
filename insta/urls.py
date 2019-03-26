from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url('^$',views.index,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^new/profile$', views.new_profile, name='new_profile'),
    # url(r'^profile/',views.image,name='posts'),
    url(r'new/post/(\d+)$',views.image,name='image')
 
]      
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
