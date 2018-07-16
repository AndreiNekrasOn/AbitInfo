from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Olymp, Speciality, Faculty, University, Subject




def index(request):
    subjects = Subject.objects.order_by('title')
    olymps = Olymp.objects.order_by('title')
    return render(request, 'olcalc/index.html', {'subjects': subjects, 'olymps': olymps})

def test(request):
    subjects = Subject.objects.order_by('title')
    olymps = Olymp.objects.order_by('title')
    return render(request, 'olcalc/test.html', {'subjects': subjects, 'olymps': olymps})
##tutorial \/ \/ \/
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        olymps = Olymp.objects.filter(title__icontains=q)
        return render_to_response('olcalc/test.html', {'olymps': olymps, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')