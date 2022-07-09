from django.contrib import admin

# Register your models here.
from app.models import Question, Post, Choice

admin.site.register([Question, Post, Choice])