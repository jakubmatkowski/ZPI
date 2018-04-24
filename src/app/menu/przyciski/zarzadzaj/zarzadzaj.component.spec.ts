/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { ZarzadzajComponent } from './zarzadzaj.component';

describe('ZarzadzajComponent', () => {
  let component: ZarzadzajComponent;
  let fixture: ComponentFixture<ZarzadzajComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ZarzadzajComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ZarzadzajComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
