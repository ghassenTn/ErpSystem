from django.shortcuts import render , redirect
# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User ,Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .serializers import UserSerializer , GroupSerializer
from .models import Message , Order , Product
from .forms import MessageForm

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()  # Fetch all users, you might want to add some filtering or other logic
    serializer = UserSerializer(users, many=True)  # Serialize users data
    return Response(serializer.data)

@api_view(['GET'])
def get_groups(request):
    groups = Group.objects.all()
    serialiser = GroupSerializer(groups,many=True)
    return Response(serialiser.data)
class LoginAPI(APIView):
    def post(self, request):
        # Retrieve the entered username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authentication successful
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            # Authentication failed
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# views.py
def chat(request):
    messages = Message.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.save()
            return redirect('chat')

    return render(request, 'chat/chat.html', {'messages': messages, 'form': form})

'''def client_register(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Save the data to the database
                # Redirect or perform other actions upon successful registration
            except IntegrityError:
                form.add_error('email', 'This email is already registered.')  # Add error message to form
    else:
        form = ClientRegistrationForm()

    return render(request, 'register.html', {'form': form})'''


def index(request):
    product = Product.objects.all()
    return render(request, 'index.html',{'product': product})
# Create your views here.
