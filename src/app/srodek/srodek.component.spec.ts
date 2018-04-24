/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { SrodekComponent } from './srodek.component';

describe('SrodekComponent', () => {
  let component: SrodekComponent;
  let fixture: ComponentFixture<SrodekComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SrodekComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SrodekComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
