from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.home, name='home'),
    # url('boards/<pk>/', views.board_topics, name='board_topics'),
    url(r'board/', views.board_topics, name='board_topics'),



#     url(r'^$', views.home, name='home'),
#     url(r'^about/$', views.about, name='about'),
#     url(r'^about/company/$', views.about_company, name='about_company'),
#     url(r'^about/author/$', views.about_author, name='about_author'),
#     url(r'^about/author/vitor/$', views.about_vitor, name='about_vitor'),
#     url(r'^about/author/erica/$', views.about_erica, name='about_erica'),
#     url(r'^privacy/$', views.privacy_policy, name='privacy_policy'),
]
