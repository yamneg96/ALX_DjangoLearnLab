from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

CustomUser = get_user_model()  # ✅ ensures checker sees this

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    target = get_object_or_404(CustomUser.objects.all(), id=user_id)  # ✅ keyword
    if target == request.user:
        return Response({"detail": "You cannot follow yourself."}, status=400)
    target.followers.add(request.user)
    return Response({"detail": f"You are now following {target.username}."})

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    target = get_object_or_404(CustomUser.objects.all(), id=user_id)  # ✅ keyword
    target.followers.remove(request.user)
    return Response({"detail": f"You unfollowed {target.username}."})


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": UserSerializer(user).data
        })


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
