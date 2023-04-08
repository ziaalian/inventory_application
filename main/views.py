from .models import Product,Category
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm
from django.utils.text import slugify
import uuid




#add product view
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Save the product and retrieve the slug value
            product = form.save(commit=False)
            slug = slugify(product.name)
            if Product.objects.filter(slug=slug).exists():
                # if slug already exists, add a random string to the end
                slug = slugify(product.name) + '-' + str(uuid.uuid4())[:8]
            product.slug = slug
            product.save()

            # Redirect to the product list with the appropriate slug parameter
            
            return redirect('search')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})





#list view
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        # if no category slug is specified, show all products
        products = products.all()
    return render(request,
                  'list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})




def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'dashboard.html', {"results":results})

    return render(request, 'dashboard.html')


