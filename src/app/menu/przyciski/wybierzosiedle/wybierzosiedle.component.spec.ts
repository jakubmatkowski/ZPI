/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { WybierzosiedleComponent } from './wybierzosiedle.component';

describe('WybierzosiedleComponent', () => {
  let component: WybierzosiedleComponent;
  let fixture: ComponentFixture<WybierzosiedleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WybierzosiedleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WybierzosiedleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
