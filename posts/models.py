from django.db import models
from user.models import UserModel


# don't ever name your foreign fields something_id. That something is enough.
# Django is meant to make things easy from the user's perspective and the _id suffix
# means you're thinking of the database layer


# Create your models here.

class PostModel(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text="Enter post tittle", unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="post_pictures/", null=True)
    text = models.CharField(max_length=4000)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        # return self.title
        return {"title": self.title, "user": self.user, "post_id": self.post_id, "timestamp": self.timestamp,
                "picture": self.picture, "text": self.text}


class TagsModel(models.Model):
    """
    Model, representing tags
    """

    # Fields

    tag_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50)

    # # Metadata
    # class Meta:
    #     ordering = ["-my_field_name"]

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return (self.tag_id, self.text)


class ActionsModel(models.Model):
    action_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=8)  # Like, Dislike, Save, Star(rating)


class UserPostActionsModel(models.Model):
    interaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    action_id = models.ForeignKey(ActionsModel, on_delete=models.CASCADE)


class PostTagsModel(models.Model):
    post_tag_id = models.AutoField(primary_key=True)
    tag = models.ForeignKey(TagsModel, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
