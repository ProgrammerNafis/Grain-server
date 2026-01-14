from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import status
from .serializers import UserSerializer

from rest_framework.permissions import AllowAny




class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
 



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    
    # সার্চ এবং ফিল্টারিং ব্যাকএন্ড যুক্ত করা হলো
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # কোন কোন ফিল্ডে সার্চ হবে (টাইটেল এবং কন্টেন্ট)
    search_fields = ['title']
    
    # কোন ফিল্ড দিয়ে ফিল্টার হবে (ক্যাটাগরি)
    filterset_fields = ['category']
    
    
    
#usr


class UserDashboard(APIView):
    permission_classes = [IsAuthenticated] # শুধু লগইন করা ইউজার ঢুকতে পারবে

    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "bio": profile.bio,
            "admin_message": profile.admin_message, # অ্যাডমিন মেসেজ
            "profile_pic": request.build_absolute_uri(profile.profile_pic.url) if profile.profile_pic else None
        })
        
        
        
#reg

class RegisterUser(APIView):
    permission_classes = [AllowAny] # যে কেউ অ্যাকাউন্ট খুলতে পারবে

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)