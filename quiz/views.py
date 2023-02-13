from django.shortcuts import render , HttpResponse , redirect
from quiz.models import Category , Question , Answer
from django.http import JsonResponse
import random
# Create your views here.

def home(request):
    category=Category.objects.all()
    
    if request.GET.get('cat_name'):
        cn=request.GET.get('cat_name')
        return redirect(f'quiz/?cat_name={cn}')
        
    context={
        'category':category,
    }
    return render(request, 'index.html', context)

# Quiz 
def quiz(request):
    category=request.GET.get('cat_name')
    questions=Question.objects.filter(category__category_name__icontains=category)[:10]
    print(questions)
    if request.method=='POST':
        total_marks=10
        
        
        obtained=0
        for question in Question.objects.all():
            ansId=request.POST.get(f'ansId-{question.uid}')
            b=Answer.objects.filter(uid=ansId) 
            print(ansId)
            for a in b:
                if a.is_correct==True:
                    obtained+=1
        print(obtained)
        
        context={
            'total':total_marks,
            'obtained':obtained,
        }
        
        return render(request, 'result.html' , context)

    context={
        'questions':questions,
    }
    return render(request, 'quiz.html', context)

# Make Api
def get_quiz(request):
    try:
        question_objs=Question.objects.all()
        if request.GET.get('cat_name'):
            question_objs=question_objs.filter(category__category_name__icontains=request.GET.get('cat_name'))
        question_objs=list(question_objs)
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