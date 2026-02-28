import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';
import { WishlistButton } from '../wishlist-button/wishlist-button';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule, WishlistButton],
  templateUrl: './product-item.html',
  styleUrls: ['./product-item.css']
})
export class ProductItem {
  @Input() product!: Product;
  @Output() delete = new EventEmitter<void>();

  encodeURIComponent = encodeURIComponent;
  Math = Math;

  onLike() {
    this.product.likes++;
  }

  onDelete() {
    if (confirm('Удалить этот товар?')) {
      this.delete.emit();
    }
  }

  onImageError(event: any) {
    event.target.src = 'https://via.placeholder.com/400x400?text=Product+Image';
  }
}