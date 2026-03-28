import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from api.models import Category, Product

# Create categories
categories = [
    Category(name='Смартфоны'),
    Category(name='Ноутбуки'),
    Category(name='Наушники'),
    Category(name='Планшеты'),
]

for cat in categories:
    cat.save()
    print(f'Created category: {cat.name}')

# Get categories
smartphones = Category.objects.get(name='Смартфоны')
laptops = Category.objects.get(name='Ноутбуки')
headphones = Category.objects.get(name='Наушники')
tablets = Category.objects.get(name='Планшеты')

# Create products
products_data = [
    # Smartphones
    {'name': 'iPhone 15 Pro Max', 'price': 699990, 'description': 'Флагманский смартфон Apple', 'count': 15, 'category': smartphones},
    {'name': 'Samsung Galaxy S24 Ultra', 'price': 599990, 'description': 'Флагман Samsung с S Pen', 'count': 12, 'category': smartphones},
    {'name': 'Xiaomi 14 Ultra', 'price': 449990, 'description': 'Флагман Xiaomi с камерой Leica', 'count': 8, 'category': smartphones},
    
    # Laptops
    {'name': 'MacBook Pro 14" M3', 'price': 999990, 'description': 'Ноутбук Apple с чипом M3', 'count': 5, 'category': laptops},
    {'name': 'ASUS ROG Strix G16', 'price': 649990, 'description': 'Игровой ноутбук с RTX 4060', 'count': 6, 'category': laptops},
    
    # Headphones
    {'name': 'AirPods Pro 2', 'price': 109990, 'description': 'Беспроводные наушники Apple', 'count': 20, 'category': headphones},
    {'name': 'Sony WH-1000XM5', 'price': 149990, 'description': 'Премиум наушники', 'count': 15, 'category': headphones},
    
    # Tablets
    {'name': 'iPad Pro 12.9" M2', 'price': 649990, 'description': 'Мощный планшет Apple', 'count': 8, 'category': tablets},
    {'name': 'Samsung Tab S9 Ultra', 'price': 549990, 'description': 'Планшет премиум-класса', 'count': 6, 'category': tablets},
]

for p in products_data:
    product = Product.objects.create(**p)
    print(f'Created product: {product.name}')

print(f'\nTotal categories: {Category.objects.count()}')
print(f'Total products: {Product.objects.count()}')