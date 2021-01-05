from django.shortcuts import render
from .models import Product

from .forms import ProductForm, RawProductForm
# Create your views here.

def product_create_view(request):
    my_form = RawProductForm()

    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #the data are good
            print(my_form.cleaned_data)
        else:
            print(my_forms.errors)    


    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)



""" raw html form
def product_create_view(request):
    #print(request.GET)
    #print(request.POST)
    my_new_title = request.POST.get('title')
    print(my_new_title)
    # Products.objects.create(title=my_new_title)
    context = {}
    return render(request, "products/product_create.html", context) """

""" def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context) """


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    
    '''inefficient way
    context = {
        'title':obj.title,
        'description':obj.description,
    }
    '''
    context = {
        'object':obj
    }
    return render(request, "products/product_detail.html", context)