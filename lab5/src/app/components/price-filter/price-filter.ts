import { Component, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-price-filter',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './price-filter.html',
  styleUrls: ['./price-filter.css']
})
export class PriceFilterComponent {
  minPrice: number | null = null;
  maxPrice: number | null = null;
  @Output() filterChange = new EventEmitter<{min: number | null, max: number | null}>();

  onMinPriceChange(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.minPrice = value ? Number(value) : null;
  }

  onMaxPriceChange(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.maxPrice = value ? Number(value) : null;
  }

  applyFilter() {
    this.filterChange.emit({min: this.minPrice, max: this.maxPrice});
  }

  resetFilter() {
    this.minPrice = null;
    this.maxPrice = null;
    this.filterChange.emit({min: null, max: null});
  }
}