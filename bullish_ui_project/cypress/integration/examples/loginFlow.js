/// <reference types="Cypress" />
import HomePage from "../pageObjects/HomePage";
import LandingPage from "../pageObjects/landingPage";
import LoginPage from "../pageObjects/loginPage";

describe("Implement workflow for the login feature", () => {
  let data;
  before(function () {
    cy.fixture("example").then(function (fdata) {
      data = fdata;
    });
  });
  it("Test the  Login in workflow", () => {
    const hompage = new HomePage();
    const loginPage = new LoginPage();
    const landingPage = new LandingPage();

    // launch the main application
    cy.visit(Cypress.env("url"));

    // click the form authentication link
    hompage.getFormAuthButton().click();

    // enter username
    loginPage.enterUsername().type(data.username);

    // enter password
    loginPage.enterPassword().type(data.password);

    //click the login
    loginPage.clickLogin().click();

    // assert the login message
    landingPage
      .assertLoggedInMessage()
      .should("contain.text", "You logged into a secure area!");

    // assert the page body
    landingPage.assertBodyMessage().should("contain.text", "Secure Area");
  });
});
