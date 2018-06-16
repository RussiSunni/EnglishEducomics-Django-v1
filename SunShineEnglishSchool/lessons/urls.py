from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),

    url('welcome', views.welcome, name='welcome'),


    url(r'^home_screen', views.home_screen, name='home_screen'),
    url('achievements', views.achievements, name='achievements'),
    url('useful_vocabulary', views.useful_vocabulary, name='useful_vocabulary'),
    url('travelling_Fish_people_quest', views.travelling_Fish_people_quest, name='travelling_Fish_people_quest'),
    url('travelling', views.travelling, name='travelling'),

    url('quests', views.quests, name='quests'),
    url('fish_person_hello', views.fish_person_hello, name='fish_person_hello'),
    url('thisway', views.thisway, name='thisway'),
    url('outside_Fish_people_quest', views.outside_Fish_people_quest, name='outside_Fish_people_quest'),
    url('outside', views.outside, name='outside'),
    url('map_screen', views.map_screen, name='map_screen'),
    url('Fisherhaven', views.Fisherhaven, name='Fisherhaven'),
    url('Fish_people_quest', views.Fish_people_quest, name='Fish_people_quest'),

]