from rest_framework import serializers
from .models import Post, Category, UserProfile, Comment 

from django.contrib.auth.models import User
from .models import UserProfile



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
        

#usr

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # পাসওয়ার্ড হ্যাশ করে ইউজার তৈরি
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # ইউজারের জন্য অটোমেটিক প্রোফাইল তৈরি
        UserProfile.objects.create(user=user)
        return user
        
        


# ...  PostSerializer এবং UserSerializer এর নিচে ...

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    # এটি নিজের ভেতরেই নিজেকে কল করবে (Recursive), যাতে রিপ্লাইগুলো দেখা যায়
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'username', 'body', 'parent', 'replies', 'created_at']

    def get_replies(self, obj):
        # যদি এই কমেন্টের কোনো রিপ্লাই থাকে, তবে সেগুলোকেও এই সিরিয়ালাইজার দিয়ে দেখাবে
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []