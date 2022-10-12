class LoginPage {
  // method to enter user name
  enterUsername() {
    return cy.get("#username");
  }

  // method to enter password
  enterPassword() {
    return cy.get("#password");
  }

  // method to click login
  clickLogin() {
    return cy.get(".radius");
  }
}
export default LoginPage;
