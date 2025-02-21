from rest_framework import serializers
from.models import LeaveRequest, Employee

class LeaverequestSerialzer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = "__all__"
        read_only_fileds = ['employee','status']
        
        def validate_leave_type(self,value):
            allowed_types = ['sick_leave','causal_leave','paid_leave']
            if value not in allowed_types:
                raise
            serializers.ValidationError("invaklid leave trype")
            return value
        class LeaveStatusUpdateSerializer(serializers.ModelSerializer):
            class Meta:
                model = LeaveRequest
                fields = ['status']
            def validate(self,value):
                if  value not in ['approved','rejected']:
                    raise
                serializers.ValidationError("invalid status update.")
                return value
            
        
            
        
    
    