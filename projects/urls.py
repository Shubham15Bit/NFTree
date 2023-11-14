from django.urls import path
from . import views

urlpatterns = [
    path('projectlist/', views.ProjectInfoList.as_view(), name='project-list'),
    path('create/', views.ProjectInfoCreate.as_view(), name='project-create'),
    path('update/<int:pk>/', views.ProjectInfoUpdate.as_view(), name='project-update'),
    path('user/<int:user_id>/', views.UserProjectsList.as_view(), name='user-projects'),
]
