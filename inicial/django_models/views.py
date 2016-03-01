from django.shortcuts import render

# Create your views here.
def employee_index(request):
    return render(request, 'template_name.html', {'something' :'dict of information'})
