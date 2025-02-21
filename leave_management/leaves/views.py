from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer, LeaveStatusUpdateSerializer
from .permissions import IsAdminOrOwner

class LeavePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class LeaveRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LeavePagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['employee', 'status']
    ordering_fields = ['start_date']
    
    def get_queryset(self):
        if self.request.user.employee.role == 'Admin':
            return LeaveRequest.objects.all()
        return LeaveRequest.objects.filter(employee=self.request.user.employee)
    def perform_create(self, serializer):
        

        serializer.save(employee=self.request.user.employee)
class LeaveRequestUpadateView(generics.UpdateAPIView):
    queryset = LeaveRequest.objects.all() 
    serializer_class = LeaveStatusUpdateSerializer 
    permission_classes = [IsAdminOrOwner]
    throttle_classes = [UserRateThrottle]
    
        
        
        
    