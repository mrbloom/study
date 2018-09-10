import html

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

def tutorials(request):
    return render(request, 'polls/tutorials.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def part2(request):

    text = '''<!doctype html>
    >> > from polls.models import Choice, Question  # Import the model classes we just wrote. <br>

    # No questions are in the system yet. <br>
    >> > Question.objects.all() <br>''' + html.escape(str(Question.objects.all())) + '<br>'

    text += '''# Create a new Question. <br>
    # Support for time zones is enabled in the default settings file, so <br>
    # Django expects a datetime with tzinfo for pub_date. Use timezone.now() <br>
    # instead of datetime.datetime.now() and it will do the right thing. <br>
    
    from django.utils import timezone <br>
    >> > q = Question(question_text="What's new?", pub_date=timezone.now()) <br>

    # Save the object into the database. You have to call save() explicitly. <br>
    >> > q.save() <br>
    '''
    from django.utils import timezone
    q = Question(question_text="What's new?", pub_date=timezone.now())

    # Save the object into the database. You have to call save() explicitly. <br>
    q.save()

    text += str(q)+'<br>'

    text += '''# Now it has an ID. <br>
    >> > q.id <br>''' + str(q.id) + '<br>' + '''# Access model field values via Python attributes. <br>
    >> > q.question_text <br>''' +  str(q.question_text) +    ">> > q.pub_date <br>"+str(q.pub_date) + "<br>" + '''
    # Change values by changing the attributes, then calling save(). <br>
    >> > q.question_text = "What's up?"
    >> > q.save()'''
    q.question_text = "What's up?"
    q.save()

    text +='''# objects.all() displays all the questions in the database. <br>
    >> > Question.objects.all()<br>''' + html.escape(str(Question.objects.all()))

    return HttpResponse(text)

def part3_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def part3_results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def part3_vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def part3_index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def part4_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/part4_detail.html', {'question': question})

def part4_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/part4_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:part4_results', args=(question.id,)))

def part4_results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/part4_results.html', {'question': question})

class part4_IndexView(generic.ListView):
    template_name = 'polls/part4_index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class part4_DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/part4_detail.html'


class part4_ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/part4_results.html'