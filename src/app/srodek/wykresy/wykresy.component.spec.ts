/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { WykresyComponent } from './wykresy.component';

describe('WykresyComponent', () => {
  let component: WykresyComponent;
  let fixture: ComponentFixture<WykresyComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WykresyComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WykresyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
