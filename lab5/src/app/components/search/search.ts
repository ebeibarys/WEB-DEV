import { Component, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './search.html',
  styleUrls: ['./search.css']
})
export class SearchComponent {
  searchTerm: string = '';
  @Output() search = new EventEmitter<string>();

  onSearchInput(event: Event) {
    this.searchTerm = (event.target as HTMLInputElement).value;
  }

  onSearch() {
    this.search.emit(this.searchTerm);
  }
}