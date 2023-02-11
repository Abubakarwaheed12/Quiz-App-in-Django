from django.db import models
import uuid
import random
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True

class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name    
    
    class Meta:
        verbose_name="Categorie"
    
    
class Question(BaseModel):
    category=models.ForeignKey(Category, on_delete=models.CASCADE , related_name='category')
    question_name=models.CharField(max_length=200, null=False)
    marks=models.IntegerField(default=1)
    
    def __str__(self):
        return self.question_name
    
    def get_answer(self):
        answer_objs=list(Answer.objects.filter(question=self))
        random.shuffle(answer_objs)
        data=[]
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct':answer_obj.is_correct,
            })
        return data
    
class Answer(BaseModel):
    question=models.ForeignKey(Question, on_delete=models.CASCADE , related_name='question')
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer