from django.contrib import admin
from quiz.models import Category , Question , Answer 
# Register your models here.
admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model=Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerAdmin]
    

admin.site.register(Question ,QuestionAdmin)
admin.site.register(Answer)
