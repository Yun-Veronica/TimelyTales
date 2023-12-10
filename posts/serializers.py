from rest_framework import serializers
from .models import PostModel, TagsModel, ActionsModel, UserPostActionsModel, PostTagsModel


# import user.models as um


class PostSerializer(serializers.Serializer):
    # отвечает только за обработку данных

    post_id = serializers.IntegerField(read_only=True)  # As this is an AutoField, we'll make it read-only
    # user_id: Because it should take the value of current user that manipulates with data
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=100)
    timestamp = serializers.DateTimeField(read_only=True)  # Cause this one is written automatically
    picture = serializers.ImageField(allow_null=True, required=False)
    text = serializers.CharField(max_length=4000)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return PostModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.title = validated_data.get('title', instance.title)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    # def delete(self, instance):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.delete()
    #     instance.save()
    #     return instance


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsModel
        # This will include all fields in the model.
        # If you want to specify, you can list them.
        fields = '__all__'


class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionsModel
        # This will include all fields in the model.
        # If you want to specify, you can list them.
        fields = '__all__'


class UserPostActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostActionsModel
        # This will include all fields in the model.
        # If you want to specify, you can list them.
        fields = '__all__'


class PostTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTagsModel
        # This will include all fields in the model.
        # If you want to specify, you can list them.
        fields = '__all__'
