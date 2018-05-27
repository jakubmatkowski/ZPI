/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { OknozarzadzajComponent } from './oknozarzadzaj.component';

describe('OknozarzadzajComponent', () => {
  let component: OknozarzadzajComponent;
  let fixture: ComponentFixture<OknozarzadzajComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OknozarzadzajComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OknozarzadzajComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
