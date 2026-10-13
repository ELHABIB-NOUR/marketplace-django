from django.shortcuts import render,get_object_or_404,redirect
from .models import product
from django.contrib.auth.decorators import login_required
from .forms import newproduct
# Create your views here.
def detail(request,pk):
    Product=get_object_or_404(product,pk=pk)
    related_products=product.objects.filter(category=Product.category,is_sold=False).exclude(pk=pk)[0:3] 
    return render(request,'items/detail.html',{
        'product':Product,
        'RP':related_products
    })

@login_required
def newp(request):
    if request.method=='POST':
       form=newproduct(request.POST,request.FILES)
       

       if form.is_valid():
            p=form.save(commit=False)
            p.created_by=request.user
            p.save()
            return redirect('items:detail',pk=p.id)
    else:   
       form=newproduct()

    return render(request,'items/form.html',{
                  'form':form})

@login_required
def delete_product(request, product_id):
    product_to_delete = get_object_or_404(
        product,
        id=product_id,
        created_by=request.user
    )
    product_to_delete.delete()
    return redirect('index')


@login_required
def purchase_product(request, product_id):
    product_to_purchase = get_object_or_404(product, id=product_id)

    if not product_to_purchase.is_sold:
        product_to_purchase.is_sold = True
        product_to_purchase.save()

    return redirect('index')