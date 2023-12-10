from django.db import models


# Create your models here.

class UserModel(models.Model):
    """
    Model, representing User
    """

    # Fields
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, help_text="Enter name")
    username = models.CharField(max_length=20, help_text="Enter username (Unique)", unique=True)
    email = models.EmailField()
    hashed_password = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to="user_profile_pictures/", null=True)

    # # Metadata
    # class Meta:
    #     ordering = ["-my_field_name"]

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.username


class SubscriptionModel(models.Model):
    """
    Model, representing Subscriber
    """

    # Fields
    subscription_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(UserModel, related_name='author', on_delete=models.CASCADE)
    subscriber = models.ForeignKey(UserModel, related_name='subscriber', on_delete=models.CASCADE)


    # # Metadata
    # class Meta:
    #     ordering = ["-my_field_name"]


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return (self.subscription_id, self.subscriber_id, self.author_id)

# Usage example
# # Create a new record using the model's constructor.
# a_record = MyModelName(my_field_name="Instance #1")
#
# # Save the object into the database.
# a_record.save()
# # Access model field values using Python attributes.
# print(a_record.id) #should return 1 for the first record.
# print(a_record.my_field_name) # should print 'Instance #1'
#
# # Change record by modifying the fields, then calling save().
# a_record.my_field_name="New Instance Name"
# a_record.save()


# Get all records of the model as QuerySet object
# all_books = Book.objects.all()

# Filtering objects of model
# all_books = Book.objects.filter(title__contains='wild')
