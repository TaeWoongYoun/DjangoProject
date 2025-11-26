from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})


def question_create(request):
    if request.method == 'POST':  # 요청이 POST방식이면
        form = QuestionForm(request.POST)  # POST 내용으로 QuestionForm()을 호출하여 form을 만듬
        if form.is_valid():  # 폼이 유효하다면, 아래 설명보기
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정
            question.save()  # 데이터를 실제로 저장
            return redirect('pybo:index')  # pybo:index로 이동함, 실주소는 …/pybo/
    else:  # 요청이 GET방식이면(POST방식이 아니면)
        form = QuestionForm()  # 인수 없이 QuestionForm()을 호출, GET 방식

    context = {'form': form}  # 위에서 선택된 form이 context의 ‘form’이 됨
    return render(request, 'pybo/question_form.html', context)
    # context의 form을 question_form.html템플릿으로 변형
    # 결국 선택된 QuestionForm을 question_form.html템플릿으로 변형

# Create your views here.

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":  # POST 방식이라면,
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:  # GET 방식이면(POST 방식이 아니라면)
        return HttpResponseNotAllowed('Only POST is possible.')  # ‘POST만 가능합니다' 오류 발생

    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)