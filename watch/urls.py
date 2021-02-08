 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url('register/',views.sign_up, name='register'),
    url('profile/',views.profile, name='profile'),
    url('contacts/',views.contacts, name='contactlist'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)