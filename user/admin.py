from django.contrib import admin
from user import models as UserModels
from posts import models as PostModel

# Register your models here.
admin.site.register(UserModels.UserModel)
admin.site.register(UserModels.SubscriptionModel)
admin.site.register(PostModel.PostModel)
admin.site.register(PostModel.TagsModel)
admin.site.register(PostModel.ActionsModel)
admin.site.register(PostModel.PostTagsModel)
admin.site.register(PostModel.UserPostActionsModel)
