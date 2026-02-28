import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductList } from './components/product-list/product-list';
import { ProductService } from './services/product.service';
import { Category } from './models/category.model';
import { Product } from './models/product.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ProductList],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App implements OnInit {
  categories: Category[] = [];
  selectedCategoryId: number | null = null;

  constructor(private productService: ProductService) {}

  ngOnInit() {
    this.categories = this.productService.getCategories();
  }

  selectCategory(categoryId: number) {
    this.selectedCategoryId = categoryId;
  }

  clearCategory() {
    this.selectedCategoryId = null;
  }

  getProducts(): Product[] {
    return this.selectedCategoryId ? 
      this.productService.getProductsByCategory(this.selectedCategoryId) : [];
  }

  getProductCount(categoryId: number): number {
    return this.productService.getProductsByCategory(categoryId).length;
  }

  getCategoryName(categoryId: number): string {
    const category = this.categories.find(c => c.id === categoryId);
    return category ? category.name : '';
  }

  onProductDeleted(productId: number) {
    this.productService.deleteProduct(productId);
  }
}