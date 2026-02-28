import { Component, Input, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-wishlist-button',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './wishlist-button.html',
  styleUrls: ['./wishlist-button.css']
})
export class WishlistButton implements OnInit {
  @Input() product!: Product;
  isInWishlist = false;

  ngOnInit() {
    // Проверяем localStorage
    const wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
    this.isInWishlist = wishlist.some((p: Product) => p.id === this.product.id);
  }

  toggleWishlist() {
    let wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
    
    if (this.isInWishlist) {
      wishlist = wishlist.filter((p: Product) => p.id !== this.product.id);
    } else {
      wishlist.push(this.product);
    }
    
    localStorage.setItem('wishlist', JSON.stringify(wishlist));
    this.isInWishlist = !this.isInWishlist;
  }
}