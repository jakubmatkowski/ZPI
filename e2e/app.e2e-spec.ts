import { ZPIPage } from './app.po';

describe('zpi App', function() {
  let page: ZPIPage;

  beforeEach(() => {
    page = new ZPIPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
