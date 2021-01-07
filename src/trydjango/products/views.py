from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from .forms import ProductForm, RawProductForm
# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request,my_id):
    obj=get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()  
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

def product_list_view(request):
    queryset = Product.objects.all() #list of objects
    context={
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_detail_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    
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

def product_delete_view(request,my_id):
    obj = get_object_or_404(Product, id = my_id)
    #POST delete request
    if request.method == "POST":
        print('confirming delete')
        obj.delete()
        return redirect('../../../product/')
    context={
        "object":obj

    }
    return render(request, "products/product_delete.html", context)



def dynamic_lookup_view(request, my_id):
    #obj = Product.objects.get(id=my_id)
    #obj = get_object_or_404(Product, id = my_id) => one of possibilities
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
        
    context={
        "object":obj

    }
    return render(request, "products/product_detail.html", context)




def render_initial_data(request):
    initial_data = {
        'title': "my awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance = obj)
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

"""for form with using raw django
def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #the data are good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_forms.errors)    

    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)
"""


""" raw html form
def product_create_view(request):
    #print(request.GET)
    #print(request.POST)
    my_new_title = request.POST.get('title')
    print(my_new_title)
    # Products.objects.create(title=my_new_title)
    context = {}
    return render(request, "products/product_create.html", context) """



