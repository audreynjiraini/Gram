from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^register/', views.register, name='register'),
    url('^$', views.index, name = 'index'),
    url(r'^profile/$', views.create_profile, name = 'create-profile'),
    url(r'^post/', views.new_post, name = 'new-post'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^comments/$', views.comments, name = 'comments'),
    url(r'^myprofile/$', views.myprofile, name = 'myprofile'),
    # url(r'^photos/$', views.photos, name = 'photos'),
    url(r'^single/(?P<image_id>\d+)/$', views.single, name = 'single'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)