from django.shortcuts import render 
#from django.http import HttpResponse
# Create your views here.
from .forms import EmployeeForm
from .models import Employee


def index(request):
    context = {}
    form = EmployeeForm()
    emp  = Employee.objects.all()
    context["score"] = emp
    context["title"] = "home" 
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                a = EmployeeForm(request.POST)
            else:
                score = Employee.objects.get(eid = pk)
                a = EmployeeForm(request.POST, instance=score)
            a.save()
            a = EmployeeForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            score = Employee.objects.get(eid = pk)
            score.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            score = Employee.objects.get(eid = pk)
            form= EmployeeForm(instance=score)
    context["form"] = form
    return render(request, "index.html", context)
    
