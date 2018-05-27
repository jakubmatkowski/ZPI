/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { OknomonitorujComponent } from './oknomonitoruj.component';

describe('OknomonitorujComponent', () => {
  let component: OknomonitorujComponent;
  let fixture: ComponentFixture<OknomonitorujComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OknomonitorujComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OknomonitorujComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
