from django.shortcuts import render

# Create your views here.
def table_of_universeties(request):
    return render(request, 'olcalc/table_of_universeties.html', {})