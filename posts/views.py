from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer

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