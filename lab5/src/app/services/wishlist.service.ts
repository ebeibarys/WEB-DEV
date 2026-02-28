import { Injectable } from '@angular/core';
import { Product } from '../models/product.model';

@Injectable({
  providedIn: 'root'
})
export class WishlistService {
  private wishlist: Product[] = [];

  constructor() {
    // Загружаем из localStorage при инициализации
    const saved = localStorage.getItem('wishlist');
    if (saved) {
      this.wishlist = JSON.parse(saved);
    }
  }

  private saveToStorage() {
    localStorage.setItem('wishlist', JSON.stringify(this.wishlist));
  }

  addToWishlist(product: Product) {
    if (!this.isInWishlist(product.id)) {
      this.wishlist.push(product);
      this.saveToStorage();
    }
  }

  removeFromWishlist(productId: number) {
    this.wishlist = this.wishlist.filter(p => p.id !== productId);
    this.saveToStorage();
  }

  isInWishlist(productId: number): boolean {
    return this.wishlist.some(p => p.id === productId);
  }

  getWishlist(): Product[] {
    return this.wishlist;
  }

  getWishlistCount(): number {
    return this.wishlist.length;
  }

  clearWishlist() {
    this.wishlist = [];
    this.saveToStorage();
  }
}