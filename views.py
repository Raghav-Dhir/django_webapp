from django.shortcuts import render
from django.http import HttpResponse
from SecondApp.models import Users
from . import forms


# Create your views here.
def index(request):
    return HttpResponse('Go to /users')


def users(request):
    user_list = Users.objects.order_by('first_name')
    userss = {'user_record': user_list}
    return render(request, 'SecondApp/index.html', context=userss)


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request, 'SecondApp/form_page.html', {'form': form})

