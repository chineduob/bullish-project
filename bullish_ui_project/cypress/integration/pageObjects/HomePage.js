class HomePage {
  // method to click the form authentication button
  getFormAuthButton() {
    return cy.get("a[href*='login']");
  }
}
export default HomePage;
