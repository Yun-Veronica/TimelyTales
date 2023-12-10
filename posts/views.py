from django.forms import model_to_dict
from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

from .serializers import PostSerializer

from .models import PostModel, TagsModel, PostTagsModel
from user.models import UserModel
from .forms import PostCreationForm

# Create your views here.
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .permissions import IsAdminOrReadOnly # - if use custom access rights

class PostViewSet(viewsets.ModelViewSet):
    # define the initial query set of objects that the view will work with
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

# def get_serialized_posts():
#     post_viewset = PostViewSet()
#     queryset = post_viewset.filter_queryset(post_viewset.get_queryset())
#     serialized_data = PostSerializer(queryset, many=True).data
#     return serialized_data
#

def index(request):
    queryset = PostModel.objects.all().order_by("-timestamp")

    # Serialize the queryset using your custom serializer
    serializer = PostSerializer(queryset, many=True)
    serialized_data = serializer.data
    # request.user - get current logged in user

    return render(request, 'main.html', {'posts': serialized_data, "pk" : request.user.id,
                                                "is_authenticated": request.user.is_authenticated})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Create but don't save to the database yet
              # Get the corresponding UserModel instance
            post.user = UserModel.objects.get(user_id=request.user.id)  # Set the user to the current logged-in user
            # timestamp field will be automatically set due to auto_now_add=True in the model
            post.save()  # Save the post to the database
            return redirect('main/', pk=post.pk)
    else:
        form = PostCreationForm()

    return render(request, 'create_post.html', {'form': form})



# class PostList(generics.ListCreateAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer
#
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer


# функции
# возврат поста по его айди
# бесконечный скрол
# вывод всех значений по реакциям на пост
# изменение и редактирование поста и его удаление
# CRUD
