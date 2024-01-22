from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class StepsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = stepsModel
        fields = ['id', 'model_name', 'Status', 'user']        

class ImgTitleStructuralWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = imgTitleStructuralWork
        fields = ['id', 'title', 'img', 'stepsmodel']

    def validate(self, data):
        # Access the associated stepsModel instance
        steps_model_instance = data['stepsmodel']

        # Check if the model_name is 'project_start'
        if steps_model_instance.model_name == stepsModel.PROJECT_START:
            raise serializers.ValidationError("Cannot upload image and title for Project Start step.")
        
        return data
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Include other fields you want to expose