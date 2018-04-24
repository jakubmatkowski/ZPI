/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { StopkaComponent } from './stopka.component';

describe('StopkaComponent', () => {
  let component: StopkaComponent;
  let fixture: ComponentFixture<StopkaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StopkaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StopkaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
