from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    
    final_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'category', 'category_name', 'content', 'final_image', 'created_at']

    def get_final_image(self, obj):
        request = self.context.get('request')

        if obj.image_file:
            image_url = obj.image_file.url
            if request is not None:
                return request.build_absolute_uri(image_url)
            return image_url

        return obj.image_url if obj.image_url else "https://via.placeholder.com/400"
        