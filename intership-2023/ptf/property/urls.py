from django.contrib import admin
from django.urls import path,include
from . import views
from property.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('create_project/',login_required(ProjectCreationView.as_view()),name='create_project'),
    path('create_project1/',login_required(ProjectCreation1View.as_view()),name='create_project1'),
    # path('add_property/',login_required(AddpropertyView.as_view()),name='properties'),
    path('list_project/',login_required(ProjectListView.as_view()),name='project_list'),
    path('list_project2/',login_required(ProjectList2View.as_view()),name='project_list2'),
     path('list_project3/',login_required(ProjectList3View.as_view()),name='project_list3'),
    # path('list_property/',login_required(PropertyListView.as_view()),name='property_list'),
    path('list_project1/',login_required(ProjectList1View.as_view()),name='project_list1'),
    path('delete_project/<int:pk>',login_required(ProjectDeleteView.as_view()),name='delete_project'),
    path('delete_project1/<int:pk>',login_required(ProjectDeleteView1.as_view()),name='delete_project1'),
    path('update_project/<int:pk>',login_required(ProjectUpdateView.as_view()),name='update_project'),
    path('update_project1/<int:pk>',login_required(ProjectUpdateView1.as_view()),name='update_project1'),
    path('detail_project/<int:pk>',login_required(ProjectDetailView.as_view()),name='detail_project'),
    path('detail_project1/<int:pk>',login_required(ProjectDetailView1.as_view()),name='detail_project1'),
    path('create_project_team/',Create_Project_team.as_view(),name='create_project_team'),
    path('list_project_team/',ProjectTeamListView.as_view(),name='project_team_list'),
    path('list_project_team1/<int:pk>',ProjectTeamByProject.as_view(),name='project_team_list1'),
]
 

