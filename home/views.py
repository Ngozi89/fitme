from django.shortcuts import render


# Home page
def home(request):
    '''
    A view to render the home page
    '''
    return render(request, 'home/index.html')

# About page
def about_page(request):
    '''A view to Renders About us page '''
    return render(request, 'home/about.html')

# Membership page
def membership_page(request):
    ''' Renders membership page '''
    return render(request, 'home/membership.html')


def tips_page(request):
    ''' Renders training tips page '''
    return render(request, 'home/tips.html')


def support_page(request):
    ''' Renders customer support page '''
    return render(request, 'home/support.html')    


def privacy_page(request):
    ''' Renders privacy policy page '''
    return render(request, 'home/privacy.html')