from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from items.models import category,product
from .forms import SignupForm,loginForm
from django.contrib.auth import logout
# Create your views here.

def index(request):
    products=product.objects.filter(is_sold=False)[0:6]
    categories=category.objects.all()

    return render(request,'market/index.html',{'categories':categories,'products':products,})

def contact(request):
    return render(request,'market/contact.html')

def signup(request):
    if request.method=='POST':
       form=SignupForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login/')
       
    form=SignupForm()


    return render(request,'market/singup.html',{'form':form})
def login(request):
    form=loginForm()


    return render(request,'market/login.html',{'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
@login_required
def dashboard(request):
    my_products = product.objects.filter(created_by=request.user)

    context = {
        'products': my_products,
        'total_products': my_products.count(),
        'active_products': my_products.filter(is_sold=False).count(),
        'sold_products': my_products.filter(is_sold=True).count(),
    }

    return render(request, 'market/dashboard.html', context)
def browse(request):
    products = product.objects.filter(is_sold=False)
    categories = category.objects.all()

    search_query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '')

    if search_query:
        products = products.filter(name__icontains=search_query)

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'market/browse.html', {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
    })

