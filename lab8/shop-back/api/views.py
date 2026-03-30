from django.http import JsonResponse, Http404
from .models import Product, Category

def category_to_dict(c: Category) -> dict:
    return {"id": c.id, "name": c.name}

def product_to_dict(p: Product) -> dict:
    return {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "count": p.count,
        "is_active": p.is_active,
        "category": p.category.id,
    }


def products_list(request):
    data = [product_to_dict(p) for p in Product.objects.all()]
    return JsonResponse(data, safe=False)

def product_detail(request, id: int):
    try:
        p = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return JsonResponse(product_to_dict(p))

def categories_list(request):
    data = [category_to_dict(c) for c in Category.objects.all()]
    return JsonResponse(data, safe=False)

def category_detail(request, id: int):
    try:
        c = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404("Category not found")
    return JsonResponse(category_to_dict(c))

def category_products(request, id: int):
    try:
        c = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404("Category not found")

    data = [product_to_dict(p) for p in c.products.all()]
    return JsonResponse(data, safe=False)