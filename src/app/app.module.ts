import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { SrodekComponent } from './srodek/srodek.component';
import { TestoweComponent } from './testowe/testowe.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    SrodekComponent,
    TestoweComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
