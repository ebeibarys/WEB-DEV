import { TestBed } from '@angular/core/testing';
import { App } from './app';
import { ProductService } from './services/product.service';

describe('App', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
      providers: [ProductService] // Provide the real service
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should have categories', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    fixture.detectChanges(); // This triggers ngOnInit
    expect(app.categories.length).toBe(4);
  });

  it('should have a header with logo', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    const logo = compiled.querySelector('.logo');
    expect(logo?.textContent).toContain('Kaspi.kz');
  });

  it('should show welcome message when no category selected', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    const welcomeMessage = compiled.querySelector('.welcome-message');
    expect(welcomeMessage).toBeTruthy();
    expect(welcomeMessage?.textContent).toContain('Добро пожаловать');
  });

  it('should select category when clicked', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    fixture.detectChanges();
    
    // Initially no category selected
    expect(app.selectedCategoryId).toBeNull();
    
    // Select a category
    app.selectCategory(1);
    expect(app.selectedCategoryId).toBe(1);
  });
});