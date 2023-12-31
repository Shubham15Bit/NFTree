from django.urls import path
from . import views

urlpatterns = [
    path('projectlist/', views.ProjectInfoList.as_view(), name='project-list'),
    path('create/', views.ProjectInfoCreate.as_view(), name='project-create'),
    path('update/<int:pk>/', views.ProjectInfoUpdate.as_view(), name='project-update'),
    path('user/<int:user_id>/', views.UserProjectsList.as_view(), name='user-projects'),
    # PlantImage views
    path('plant_images/create/', views.PlantImageCreate.as_view(), name='plant-image-create'),
    path('plant_images/<int:pk>/update/', views.PlantImageUpdate.as_view(), name='plant-image-update'),
    path('plant_images/', views.PlantImageList.as_view(), name='plant-image-list'),
    path('<int:project_id>/plant_images/', views.PlantImageList.as_view(), name='project-plant-image-list'),
    path('projectlistup/', views.ProjectInfoCreateList.as_view(), name='project-list'), 
    #Tranaction and report views
    path('transaction/', views.TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transaction/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('project-report/', views.ProjectReportListCreateView.as_view(), name='project-report-list-create'),
    path('project-report/<int:pk>/', views.ProjectReportDetailView.as_view(), name='project-report-detail'),
]
