/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { PrzyciskzalogujComponent } from './przyciskzaloguj.component';

describe('PrzyciskzalogujComponent', () => {
  let component: PrzyciskzalogujComponent;
  let fixture: ComponentFixture<PrzyciskzalogujComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PrzyciskzalogujComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PrzyciskzalogujComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
