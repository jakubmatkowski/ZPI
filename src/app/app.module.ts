import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { SrodekComponent } from './srodek/srodek.component';
import { TestoweComponent } from './testowe/testowe.component';
import { PrzyciskiComponent } from './menu/przyciski/przyciski.component';
import { WybierzosiedleComponent } from './menu/przyciski/wybierzosiedle/wybierzosiedle.component';
import { MonitorujComponent } from './menu/przyciski/monitoruj/monitoruj.component';
import { ZarzadzajComponent } from './menu/przyciski/zarzadzaj/zarzadzaj.component';
import { StopkaComponent } from './srodek/stopka/stopka.component';
import { WykresyComponent } from './srodek/wykresy/wykresy.component';
import { RejestracjaComponent } from './menu/rejestracja/rejestracja.component';
import { PrzyciskzarejestrujComponent } from './menu/rejestracja/przyciskzarejestruj/przyciskzarejestruj.component';
import { PrzyciskzalogujComponent } from './menu/rejestracja/przyciskzaloguj/przyciskzaloguj.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    SrodekComponent,
    TestoweComponent,
    PrzyciskiComponent,
    WybierzosiedleComponent,
    MonitorujComponent,
    ZarzadzajComponent,
    StopkaComponent,
    WykresyComponent,
    RejestracjaComponent,
    PrzyciskzarejestrujComponent,
    PrzyciskzalogujComponent,
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
