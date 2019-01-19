from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import *


def index(request):
    olymps = QOlymp.objects.order_by('title')
    return render(request, 'olcalc/index.html', {'olymps': olymps})


def test(request):
    olymps = QOlymp.objects.order_by('title')
    return render(request, 'olcalc/test.html', {'olymps': olymps})


def blog(request):
    olymps = QOlymp.objects.order_by('title')
    return render(request, 'olcalc/blog.html', {'olymps': olymps})


def project(request):
    olymps = QOlymp.objects.order_by('title')
    return render(request, 'olcalc/project.html', {'olymps': olymps})


def search(request):
    olymps = list(QOlymp.objects.order_by('title'))
    if ('olymp_name' in request.GET and request.GET['olymp_name']) and \
            ('olymp_subject' in request.GET and request.GET['olymp_subject']):
        olymp_name = request.GET['olymp_name']
        olymp_subject = request.GET['olymp_subject']
        qmap = QMapping.objects.all().filter(olymp__title=olymp_name).filter(olymp__subject=olymp_subject)
        set_qmap = set()
        for u in qmap:
            set_qmap.add(u)
        content = {'olymp_name': olymp_name, 'olymp_subject': olymp_subject,
                   'qmap': set_qmap, 'olymps': olymps}
        return render_to_response('olcalc/index.html', content)
    else:
        return render(request, 'olcalc/index.html', {'olymps': olymps})
