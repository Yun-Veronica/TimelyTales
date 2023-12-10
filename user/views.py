from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, viewsets
from .models import UserModel, SubscriptionModel
from .serializers import UserSerializer, SubscriptionSerializer
from .forms import UserRegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return render(request, 'page.html')
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class SubscriptionList(generics.ListCreateAPIView):
    queryset = SubscriptionModel.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionModel.objects.all()
    serializer_class = SubscriptionSerializer


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.hashed_password = make_password(form.cleaned_data['hashed_password'])
            user.save()
            return redirect('/main/')  # Замените 'success' на имя вашего URL-шаблона для успешной регистрации
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})


@login_required
def user_profile(request, pk):
    current_user = request.user
    if current_user.is_authenticated:

        # Serialize the queryset using your custom serializer
        # current_user = UserModel.objects.get(user_id=request.user.id)
        # Using get_object_or_404 to handle the case where the UserModel instance does not exist
        current_user = get_object_or_404(UserModel, user_id=request.user.id)
        serializer = UserSerializer(current_user, many=False)
        serialized_data = serializer.data
        # request.user - get current logged in user

        return render(request, 'profile.html', {'user': serialized_data, "pk": request.user.id,
                                                "is_authenticated": request.user.is_authenticated})
    else:
        # Handle the case where there is no authenticated user
        return HttpResponse("User is not authenticated")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'user/{request.user.id}/profile')  # Redirect to the main page after login
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('main/')
# функции
# регистрация
# аутентификация
# реакции
# профиль пользователя
# написание поста
# изменение профиля
# удаление профиля
# взаимодействие с постом
# CRUD
