/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { TestoweComponent } from './testowe.component';

describe('TestoweComponent', () => {
  let component: TestoweComponent;
  let fixture: ComponentFixture<TestoweComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TestoweComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TestoweComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
