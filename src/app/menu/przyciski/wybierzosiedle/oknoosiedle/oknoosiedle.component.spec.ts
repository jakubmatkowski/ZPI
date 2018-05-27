/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { OknoosiedleComponent } from './oknoosiedle.component';

describe('OknoosiedleComponent', () => {
  let component: OknoosiedleComponent;
  let fixture: ComponentFixture<OknoosiedleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OknoosiedleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OknoosiedleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
