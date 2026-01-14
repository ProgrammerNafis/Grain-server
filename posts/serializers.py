from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    final_image = serializers.ReadOnlyField(source='get_image')

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'category', 'category_name', 'content', 'final_image', 'created_at']