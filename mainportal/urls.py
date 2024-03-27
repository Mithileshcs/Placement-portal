from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register_user, name='register'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('add_record/', views.add_record, name='add_record'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('apply/<int:company_id>/', views.apply_for_job, name='apply_for_job'),

]