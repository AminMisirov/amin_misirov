from django.contrib import admin
from .models import Author, Category, Post, Tag, Message

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')  # Başlıq və məzmunu göstər
    search_fields = ('title', 'content')  # Axtarış funksiyası
    filter_horizontal = ('tags',)  # Taglar üçün seçim paneli

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)  # Post modelini admin panelinə qeydiyyatdan keçiririk

# Tag modelini qeydiyyatdan keçiririk
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_posts')  # description da göstərilsin
    search_fields = ['name']

    def get_posts(self, obj):
        return ", ".join([post.title for post in obj.posts.all()])
    get_posts.short_description = 'Posts'

admin.site.register(Tag, TagAdmin)

# Message modelini admin panelinə qeydiyyatdan keçiririk
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at', 'is_read')  # Sütunlar
    list_filter = ('is_read', 'sent_at')  # Filtr sahələri
    search_fields = ('name', 'email', 'message')  # Axtarış üçün sahələr

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('-is_read', '-sent_at')  # Oxunmamışlar üstə olsun

    # Mesajı açarkən avtomatik `is_read` aktiv edilsin
    def change_view(self, request, object_id, form_url='', extra_context=None):
        message = self.get_object(request, object_id)
        if message and not message.is_read:
            message.is_read = True
            message.save()
        return super().change_view(request, object_id, form_url, extra_context)
