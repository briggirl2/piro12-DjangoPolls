from django.contrib import admin

from polls.models import Question, Choice


# admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
