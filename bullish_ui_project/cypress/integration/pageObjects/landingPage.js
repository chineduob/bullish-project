class LandingPage {
  // method to assert
  assertLoggedInMessage() {
    return cy.get("#flash");
  }

  // method to assert body text
  assertBodyMessage() {
    return cy.get("h2");
  }
}
export default LandingPage;
