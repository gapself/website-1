from django.urls import path
from . import views

# app_name ='webapp'

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('insights/', views.insights, name='insights'),
    path('insights/<int:pk>/', views.insights_detail, name='insights_detail'),
    path('insights/<int:pk>/edit/', views.insights_edit, name='insights_edit'),
    # path('insights_edit', views.insights_edit, name='insights_edit')
]