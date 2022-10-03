from django.urls import path
from iteration3 import views
urlpatterns = [
    path('', views.login, name='iteration3/login'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('guide/', views.guide, name='guide'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('community/', views.community, name='community'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('diary/', views.diary, name='diary'),
    path('ajax/load_portion/', views.load_portion, name='ajax_load_portion'),
    path('ajax/load_description/', views.load_description, name='ajax_load_description'),
    path('iteration2/', views.test, name='iteration2'),
    path('create_view/', views.create_view, name='create_view'),
    path('list_view/', views.list_view, name='list_view'),
    path('entry_view/', views.entry_view, name='entry_view'),
    path('please_login/', views.please_login, name='please_login'),
    # path('add_diary/', views.add_diary, name='add_diary'),
    path('carb_chart/', views.carb_chart, name='carb_chart'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('tips/', views.tips, name='tips'),
]