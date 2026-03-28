from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Category, Product


def api_root(request):
    """Welcome endpoint with API documentation"""
    return JsonResponse({
        'message': 'Shop API',
        'endpoints': {
            'products': '/api/products/',
            'product_detail': '/api/products/<id>/',
            'categories': '/api/categories/',
            'category_detail': '/api/categories/<id>/',
            'category_products': '/api/categories/<id>/products/',
        }
    })


def products_list(request):
    """List all products"""
    products = Product.objects.all()
    data = [
        {
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id,
            'category_name': p.category.name,
        }
        for p in products
    ]
    return JsonResponse(data, safe=False)


def product_detail(request, id):
    """Get one product by ID"""
    product = get_object_or_404(Product, id=id)
    data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category_id': product.category.id,
        'category_name': product.category.name,
    }
    return JsonResponse(data)


def categories_list(request):
    """List all categories"""
    categories = Category.objects.all()
    data = [
        {
            'id': c.id,
            'name': c.name,
            'product_count': c.products.count(),
        }
        for c in categories
    ]
    return JsonResponse(data, safe=False)


def category_detail(request, id):
    """Get one category by ID"""
    category = get_object_or_404(Category, id=id)
    data = {
        'id': category.id,
        'name': category.name,
        'product_count': category.products.count(),
    }
    return JsonResponse(data)


def category_products(request, id):
    """List products by category"""
    category = get_object_or_404(Category, id=id)
    products = category.products.filter(is_active=True)
    data = [
        {
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id,
            'category_name': p.category.name,
        }
        for p in products
    ]
    return JsonResponse(data, safe=False)