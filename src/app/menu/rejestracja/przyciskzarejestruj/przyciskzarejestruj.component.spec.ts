/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { PrzyciskzarejestrujComponent } from './przyciskzarejestruj.component';

describe('PrzyciskzarejestrujComponent', () => {
  let component: PrzyciskzarejestrujComponent;
  let fixture: ComponentFixture<PrzyciskzarejestrujComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PrzyciskzarejestrujComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PrzyciskzarejestrujComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
