import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { MonitorujComponent } from './menu/przyciski/monitoruj/monitoruj.component';
import { OknomonitorujComponent } from './menu/przyciski/monitoruj/oknomonitoruj/oknomonitoruj.component';
import { PrzyciskiComponent } from './menu/przyciski/przyciski.component';
import { OknoosiedleComponent } from './menu/przyciski/wybierzosiedle/oknoosiedle/oknoosiedle.component';
import { WybierzosiedleComponent } from './menu/przyciski/wybierzosiedle/wybierzosiedle.component';
import { OknozarzadzajComponent } from './menu/przyciski/zarzadzaj/oknozarzadzaj/oknozarzadzaj.component';
import { ZarzadzajComponent } from './menu/przyciski/zarzadzaj/zarzadzaj.component';
import { PrzyciskzalogujComponent } from './menu/rejestracja/przyciskzaloguj/przyciskzaloguj.component';
import { PrzyciskzarejestrujComponent } from './menu/rejestracja/przyciskzarejestruj/przyciskzarejestruj.component';
import { RejestracjaComponent } from './menu/rejestracja/rejestracja.component';
import { SrodekComponent } from './srodek/srodek.component';
import { StopkaComponent } from './srodek/stopka/stopka.component';
import { WykresyComponent } from './srodek/wykresy/wykresy.component';
import { TestoweComponent } from './testowe/testowe.component';

const routes: Routes = [
  { path: '/wybraneosiedla', component: OknoosiedleComponent },
  { path: '**',   component: OknomonitorujComponent },
];

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
    OknoosiedleComponent,
    OknomonitorujComponent,
    OknozarzadzajComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
      ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }