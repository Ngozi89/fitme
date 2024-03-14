from django.shortcuts import render
from django.http import HttpResponse
from .forms import MemberForm
from .models import Member


# Home page
def home(request):
    '''
    A view to render the home page
    '''
    return render(request, 'home/index.html')

# Membership page
def membership(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['memb_name']
            email = form.cleaned_data['memb_email']

            memb = Member.objects.create(memb_name=name, memb_email=email)

            memb.save()
            return HttpResponse("Congratulation on your fitness journey")
    form = MemberForm()
    return render(request, 'home/membership.html', {'form': form})

# About page
def about_page(request):
    '''A view to Renders About us page '''
    return render(request, 'home/about.html')


def tips_page(request):
    ''' Renders training tips page '''
    return render(request, 'home/tips.html')


def support_page(request):
    ''' Renders customer support page '''
    return render(request, 'home/support.html')    


def privacy_page(request):
    ''' Renders privacy policy page '''
    return render(request, 'home/privacy.html')