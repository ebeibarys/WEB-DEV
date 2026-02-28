import { Injectable } from '@angular/core';
import { Product } from '../models/product.model';

export interface CartItem {
  product: Product;
  quantity: number;
}

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private cart: CartItem[] = [];

  constructor() {
    // Загружаем из localStorage при инициализации
    const saved = localStorage.getItem('cart');
    if (saved) {
      this.cart = JSON.parse(saved);
    }
  }

  private saveToStorage() {
    localStorage.setItem('cart', JSON.stringify(this.cart));
  }

  addToCart(product: Product, quantity: number = 1) {
    const existing = this.cart.find(item => item.product.id === product.id);
    if (existing) {
      existing.quantity += quantity;
    } else {
      this.cart.push({ product, quantity });
    }
    this.saveToStorage();
  }

  removeFromCart(productId: number) {
    this.cart = this.cart.filter(item => item.product.id !== productId);
    this.saveToStorage();
  }

  updateQuantity(productId: number, quantity: number) {
    const item = this.cart.find(item => item.product.id === productId);
    if (item) {
      item.quantity = quantity;
      this.saveToStorage();
    }
  }

  getCart(): CartItem[] {
    return this.cart;
  }

  getTotalPrice(): number {
    return this.cart.reduce((sum, item) => sum + (item.product.price * item.quantity), 0);
  }

  getTotalItems(): number {
    return this.cart.reduce((sum, item) => sum + item.quantity, 0);
  }

  clearCart() {
    this.cart = [];
    this.saveToStorage();
  }
}