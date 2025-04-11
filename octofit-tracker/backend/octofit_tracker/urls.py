from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('api/teams/', views.TeamListCreateView.as_view(), name='team-list-create'),
    path('api/activities/', views.ActivityListCreateView.as_view(), name='activity-list-create'),
    path('api/leaderboard/', views.LeaderboardListView.as_view(), name='leaderboard-list'),
    path('api/workouts/', views.WorkoutListCreateView.as_view(), name='workout-list-create'),
    path('', views.api_root, name='api-root'),
]