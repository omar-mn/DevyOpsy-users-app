from rest_framework import serializers 
from .models import user
from rest_framework import serializers

class Profile(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = user
        fields = ('full_name', 'username' , 'first_name' , 'last_name' , 'profileImage' , 'profile_banner' , 'bio')
        read_only_fields = ('email', 'full_name')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.username
