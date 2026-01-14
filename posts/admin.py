from django.contrib import admin
from .models import Category, Post
from .models import UserProfile, Comment




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    
    
#usr cmnt
admin.site.register(Comment)

# প্রোফাইল অ্যাডমিন যেখানে আপনি ইউজারকে মেসেজ লিখবেন
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'admin_message']
    list_editable = ['admin_message'] # সরাসরি লিস্ট থেকেই মেসেজ এডিট করা যাবে