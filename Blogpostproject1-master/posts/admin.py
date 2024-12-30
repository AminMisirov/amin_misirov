from django.contrib import admin

from .models import Author, Category, Post, Message

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at', 'is_read')  # Sütunlar
    list_filter = ('is_read', 'sent_at')  # Filtr sahələri
    search_fields = ('name', 'email', 'message')  # Axtarış üçün sahələr

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('-is_read', '-sent_at')  # Oxunmamışlar üstə olsun

    # Mesajı açarkən avtomatik is_read aktiv edilsin
    def change_view(self, request, object_id, form_url='', extra_context=None):
        message = self.get_object(request, object_id)
        if message and not message.is_read:
            message.is_read = True
            message.save()
        return super().change_view(request, object_id, form_url, extra_context)