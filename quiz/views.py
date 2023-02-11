from django.shortcuts import render , HttpResponse
from quiz.models import Category , Question , Answer
from django.http import JsonResponse
import random
# Create your views here.

def home(request):
    return render(request, 'index.html')

# Male Api

def get_quiz(request):
    try:
        question_objs=list(Question.objects.all())
        random.shuffle(question_objs)
        data=[]
        for question_obj in question_objs:
            data.append({
                'category':question_obj.category.category_name,
                'question':question_obj.question_name,
                'marks':question_obj.marks,
                'Answer':question_obj.get_answer()
            })
        print(data)
        payload={'status':True , 'data':data}
        
        return JsonResponse(payload)
        
    except Exception as e :
        print(e)
    return HttpResponse('Some Thing Went Wrong')