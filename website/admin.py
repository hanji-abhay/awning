from django.contrib import admin
from .models import Feedback, ContactQuery
# Register your models here.
@admin.register(ContactQuery)
class ContactQueryAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "phone", "email", "message")
    ordering = ("-created_at",)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "rating", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "phone", "message")
    ordering = ("-created_at",)