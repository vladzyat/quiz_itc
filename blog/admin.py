from django.contrib import admin
from .models import Quiz, Question, Answer
# Register your models here.


class AnswerInLine(admin.TabularInline):
    fk_name = 'question'
    model = Answer
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [AnswerInLine]
    list_display_links = ['title']
    search_fields = ['title']

admin.site.register(Answer)
admin.site.register(Quiz)