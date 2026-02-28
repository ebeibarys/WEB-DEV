import { Injectable } from '@angular/core';
import { Product } from '../models/product.model';
import { Category } from '../models/category.model';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private categories: Category[] = [
    { id: 1, name: 'Смартфоны', icon: '📱' },
    { id: 2, name: 'Ноутбуки', icon: '💻' },
    { id: 3, name: 'Наушники', icon: '🎧' },
    { id: 4, name: 'Планшеты', icon: '📟' }
  ];

  private products: Product[] = [
  // Смартфоны (5 шт)
  {
    id: 1,
    name: 'iPhone 15 Pro Max 256GB',
    description: 'Флагманский смартфон Apple с титановым корпусом, процессор A17 Pro, 256GB памяти',
    price: 699990,
    rating: 4.9,
    images: ['https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400&h=400&fit=crop'],
    link: 'https://kaspi.kz/shop/p/apple-iphone-15-pro-max-256gb-seryi-113138420/',
    categoryId: 1,
    likes: 0
  },
  {
    id: 2,
    name: 'Samsung Galaxy S24 Ultra 256GB',
    description: 'Флагман Samsung с S Pen, 200MP камера, титановый корпус',
    price: 599990,
    rating: 4.8,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/h7c/h38/84963297329182.png?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/samsung-galaxy-s24-ultra-5g-256gb-seryi-116043556/',
    categoryId: 1,
    likes: 0
  },
  {
    id: 3,
    name: 'Xiaomi 14 Ultra 512GB',
    description: 'Флагман Xiaomi с камерой Leica, 512GB памяти',
    price: 449990,
    rating: 4.7,
    images: ['https://tse3.mm.bing.net/th/id/OIP.u0SVzYi_iH1bEGPUMO5IzQHaEI?rs=1&pid=ImgDetMain&o=7&rm=3'],
    link: 'https://kaspi.kz/shop/p/xiaomi-14-ultra-16-gb-512-gb-chernyi-podarok-118320518/',
    categoryId: 1,
    likes: 0
  },
  {
    id: 4,
    name: 'Google Pixel 8 Pro 128GB',
    description: 'Флагман Google с лучшей камерой и чистым Android',
    price: 399990,
    rating: 4.7,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/hd1/hc9/84326216630302.jpg?format=gallery-large'],
    link: 'https://kaspi.kz/shop/p/google-pixel-8-pro-12-gb-128-gb-chernyi-114017043/',
    categoryId: 1,
    likes: 0
  },
  {
    id: 5,
    name: 'OnePlus 12 512GB',
    description: 'Флагман OnePlus с быстрой зарядкой и мощным процессором',
    price: 349990,
    rating: 4.6,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/p48/pa8/54233333.png?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/oneplus-nord-5-12-gb-512-gb-seryi-142846291/?c=750000000',
    categoryId: 1,
    likes: 0
  },
  
  // Ноутбуки (5 шт)
  {
    id: 6,
    name: 'MacBook Pro 14" M3',
    description: 'Ноутбук Apple с чипом M3, 16GB RAM, 512GB SSD',
    price: 999990,
    rating: 4.9,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/p32/p89/17666424.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/apple-macbook-pro-14-2024-14-2-16-gb-ssd-512-gb-macos-mw2u3ru-a-132088460/?c=750000000',
    categoryId: 2,
    likes: 0
  },
  {
    id: 7,
    name: 'ASUS ROG Strix G16',
    description: 'Игровой ноутбук с Ryzen 9, RTX 4060, 16GB RAM',
    price: 649990,
    rating: 4.8,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/p8d/pbb/42525232.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/asus-rog-strix-g16-16-16-gb-ssd-1024-gb-bez-os-90nr0nj7-m001j0-139735259/?c=750000000',
    categoryId: 2,
    likes: 0
  },
  {
    id: 8,
    name: 'Lenovo Legion 5 Pro',
    description: 'Игровой ноутбук с Ryzen 7, RTX 5060, 16GB RAM',
    price: 549990,
    rating: 4.7,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/p67/p81/62644075.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/lenovo-legion-pro-5-16-16-gb-ssd-1000-gb-bez-os-83lt0005rk-145169184/?c=750000000',
    categoryId: 2,
    likes: 0
  },
  {
    id: 9,
    name: 'HP Victus 16',
    description: 'Игровой ноутбук с Ryzen 5, RTX 3050, 16GB RAM',
    price: 399990,
    rating: 4.6,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/h25/hcc/85983814680606.png?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/hp-victus-15-6-16-gb-ssd-512-gb-dos-15-fb2027ci-a19gqea-119250104/?c=750000000',
    categoryId: 2,
    likes: 0
  },
  {
    id: 10,
    name: 'Acer Aspire 5',
    description: 'Тонкий и легкий ноутбук для работы и учебы',
    price: 249990,
    rating: 4.5,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/p76/p0f/55291864.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/acer-aspire-5-spin-14-14-16-gb-ssd-1000-gb-win-11-pro-nx-khter-002w-143152048/?c=750000000',
    categoryId: 2,
    likes: 0
  },
  
  // Наушники (5 шт)
  {
    id: 11,
    name: 'AirPods Pro 2',
    description: 'Беспроводные наушники Apple с шумоподавлением',
    price: 109990,
    rating: 4.9,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/ha3/h07/84108189630494.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/naushniki-apple-airpods-pro-2nd-generation-with-wireless-magsafe-charging-case-belyi-113677582/?c=750000000',
    categoryId: 3,
    likes: 0
  },
  {
    id: 12,
    name: 'Sony WH-1000XM5',
    description: 'Премиум наушники с лучшим шумоподавлением',
    price: 149990,
    rating: 4.9,
    images: ['https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=400&h=400&fit=crop'],
    link: 'https://kaspi.kz/shop/p/naushniki-sony-wh-1000xm5-chernyi-105259822/?c=750000000',
    categoryId: 3,
    likes: 0
  },
  {
    id: 13,
    name: 'JBL Tune 510BT',
    description: 'Беспроводные наушники с хорошим звуком',
    price: 24990,
    rating: 4.7,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/hef/h29/64030233788446.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/naushniki-jbl-tune-510bt-chernyi-101420081/?c=750000000',
    categoryId: 3,
    likes: 0
  },
  {
    id: 14,
    name: 'Samsung Buds2 Pro',
    description: 'Наушники Samsung с 24-bit звуком',
    price: 69990,
    rating: 4.8,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/h1b/hb0/64157509746718.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/naushniki-samsung-galaxy-buds-2-zelenyi-102046357/?c=750000000',
    categoryId: 3,
    likes: 0
  },
  {
    id: 15,
    name: 'Marshall Major IV',
    description: 'Стильные наушники с батареей на 80+ часов',
    price: 59990,
    rating: 4.8,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/pf3/pc1/17680136.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/naushniki-marshall-major-iv-chernyi-102138144/?c=750000000',
    categoryId: 3,
    likes: 0
  },
  
  // Планшеты (5 шт)
  {
    id: 16,
    name: 'iPad Pro 12.9" M2',
    description: 'Мощный планшет Apple с дисплеем XDR',
    price: 649990,
    rating: 4.9,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/h0c/h0e/64900017389598.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/apple-ipad-pro-12-9-2022-wi-fi-12-9-djuim-8-gb-128-gb-seryi-107277956/?c=750000000',
    categoryId: 4,
    likes: 0
  },
  {
    id: 17,
    name: 'Samsung Tab S9 Ultra',
    description: 'Планшет премиум-класса с S Pen',
    price: 549990,
    rating: 4.8,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/h02/h6e/82770436030494.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/samsung-galaxy-tab-s9-sm-x716bzaas-11-djuim-8-gb-128-gb-grafit-112488621/?c=750000000',
    categoryId: 4,
    likes: 0
  },
  {
    id: 18,
    name: 'Xiaomi Pad 6',
    description: 'Отличный планшет для работы и развлечений',
    price: 149990,
    rating: 4.7,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/h32/hdc/82729741582366.jpg?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/xiaomi-pad-6-11-djuim-8-gb-256-gb-seryi-112453226/?c=750000000',
    categoryId: 4,
    likes: 0
  },
  {
    id: 19,
    name: 'iPad Air 11',
    description: 'iPad Air с чипом M3, универсальный выбор',
    price: 299990,
    rating: 4.8,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/pae/pf8/37020299.png?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/apple-ipad-air-11-2025-wi-fi-11-djuim-8-gb-128-gb-fioletovyi-138202498/?c=750000000',
    categoryId: 4,
    likes: 0
  },
  {
    id: 20,
    name: 'Samsung Galaxy Tab S11 Ultra',
    description: 'Планшет с OLED-экраном и мощным звуком',
    price: 179990,
    rating: 4.6,
    images: ['https://resources.cdn-kaspi.kz/img/m/p/pfd/p2b/69034256.png?format=gallery-medium'],
    link: 'https://kaspi.kz/shop/p/samsung-galaxy-tab-s11-ultra-14-6-djuim-12-gb-256-gb-serebristyi-146913673/?c=750000000',
    categoryId: 4,
    likes: 0
  }
];

  getCategories(): Category[] {
    return this.categories;
  }

  getProductsByCategory(categoryId: number): Product[] {
    return this.products.filter(p => p.categoryId === categoryId);
  }

  deleteProduct(productId: number): void {
    const index = this.products.findIndex(p => p.id === productId);
    if (index !== -1) {
      this.products.splice(index, 1);
    }
  }

  likeProduct(productId: number): void {
    const product = this.products.find(p => p.id === productId);
    if (product) {
      product.likes++;
    }
  }
}