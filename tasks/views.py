from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, RequestContext

from .models import Day, Task
from .forms import DayForm, TaskForm


def index(request):
    day_list = Day.objects.all().order_by('day')
    return render(request, 'tasks/index.html', {'day_list':day_list})

def detail(request, day_id):
    day = get_object_or_404(Day, pk = day_id)
    return render(request, 'tasks/detail.html', {'day': day})

def add_day(request):

    if request.method == "POST":
        day = Day.objects.filter(day = request.POST['day'])
        if day.exists():
            return render(request, 'tasks/redir.html', {'day': day[0]})
        else:    
            dform = DayForm(request.POST, instance=Day())
            if dform.is_valid():
                new_day = dform.save()
                for k in request.POST:
                    if not k.endswith('-task_text'):
                        continue
                    cf = TaskForm(request.POST, prefix=k.replace('-task_text', ''), instance=Task())
                    if not cf.is_valid():
                        continue
                    if not cf.cleaned_data['task_text']:
                        continue
                    new_task = cf.save(commit=False)
                    new_task.day = new_day
                    new_task.save()
                return HttpResponseRedirect('/')
    else:
        dform = DayForm(instance=Day())
        tforms = [TaskForm(prefix=str(x), instance=Task()) for x in range(0,5)]
    return render_to_response('tasks/add_day.html', {'day_form': dform, 'task_forms': tforms}, context_instance=RequestContext(request))

def edit_day(request, day_id):
    day = get_object_or_404(Day, pk = day_id)
    day_form = DayForm(request.POST or None, instance=day)
    tforms = [TaskForm(request.POST or None, prefix=str(i), instance=t) for i, t in enumerate(day.task_set.all())]
    num_tasks = len(tforms)
    for k in request.POST:
        if not k.endswith('-task_text') or int(k.replace('-task_text', ''))< num_tasks:
            continue
        cf = TaskForm(request.POST, prefix=k.replace('-task_text', ''), instance=Task())  
        tforms.append(cf)  
    if day_form.is_valid():
        day_form.save()
        for t in tforms:
            new_task = t.save(commit=False)
            new_task.day = day
            new_task.save()
        return HttpResponseRedirect('/')
    return render(request, 'tasks/edit.html', {'day_form': day_form, 'task_forms':tforms})


