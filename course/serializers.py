from rest_framework import serializers
from .models import AddContent

class AddContentSerializer(serializers.ModelSerializer):
    U_ID = serializers.IntegerField(required=False, allow_null=True)
    created_by = serializers.CharField(required=False, allow_null=True)
    content_name = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = AddContent
        fields = '__all__'