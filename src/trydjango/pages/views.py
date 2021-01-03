from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") #string of html code
    return render(request, "home.html",{})

def contact_view(request,*args, **kwargs):
    return render(request, "contact.html",{})

def about_view(request,*args, **kwargs):
    my_context = {
        "title":"This is about us",
        "this_is_true": True,
        "my_number":1234,
        "my_list":[123,54,78,99,'Abc']
    }


    return render(request, "about.html",my_context)

def social_view(*args, **kwargs):
    return HttpResponse("<h1>Social Page<h1>")    
