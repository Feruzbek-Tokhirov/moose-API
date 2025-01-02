from django.contrib import admin
from .models import Contact, About, Article, Comment


class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "create_date", "is_published")


admin.site.register(Contact, ContactAdmin)
admin.site.register(About)
admin.site.register(Article)
admin.site.register(Comment)
