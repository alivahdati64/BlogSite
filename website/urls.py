from django.urls import path
from website.views import *

app_name='website'  #url

urlpatterns = [
    # path('home',index_view),
    path('',index_view, name='index'),
    path('about',about_view, name='about'),
    path('contact',contact_view, name='contact'),
    path('test',test_view, name='test'),
    path('newsletter',newsletter_view, name='newsletter')
]