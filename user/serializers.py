from rest_framework import serializers
from . import models



class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)  # As this is an AutoField, we'll make it read-only
    name = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    hashed_password =  serializers.CharField(max_length=150)
    profile_picture =  serializers.ImageField(allow_null=True, required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return models.UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.hashed_password = validated_data.get('hashed_password', instance.hashed_password)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubscriptionModel
        # This will include all fields in the model.
        # If you want to specify, you can list them.
        fields = '__all__'


