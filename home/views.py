from django.shortcuts import render

# Create your views here.
def landing_page(request):
    '''
    Render the landing page.
    '''
    return render(request, "landing_page.html")

def login(request):
    '''
    Render the login page.
    '''
    return render(request, "login.html")

def register(request):
    '''
    Render the login page.
    '''
    return render(request, "signup.html")

def jobTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "jobapplicationformTemp.html")  

def formTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "formTemplate.html")  

def meetCreatars(request):
    '''
    Render the login page.
    '''
    return render(request, "meetcreaters.html")   

def jdTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "JDTemplate.html")

def brandProTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "brandprofileTemplate.html")

def creatARproTemp(request):
    '''
    Render the login page.
    '''
    return render(request, "creatARprofileTemplate.html")