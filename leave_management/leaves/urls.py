from django.urls import path
from .views import LeaveRequestListCreateView,LeaveRequestUpadateView

urlpatterns = [
    path('Leaves/',
LeaveRequestListCreateView.as_view(),
name='leave-list-create'),
    path('leave/<int:pk>/',LeaveRequestUpdateView.as_view(),
name='leave-update')   
]
