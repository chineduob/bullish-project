/// <reference types="Cypress" />
import { Given, When, Then, And } from "cypress-cucumber-preprocessor/steps";
import HomePage from "../../../pageObjects/HomePage";
import LandingPage from "../../../pageObjects/landingPage";
import LoginPage from "../../../pageObjects/loginPage";

const hompage = new HomePage();
const loginPage = new LoginPage();
const landingPage = new LandingPage();

Given("User launches the landing page", () => {
  cy.visit(Cypress.env("url"));
});

When("User should be able to click the form authentication link"),
  function () {
    hompage.getFormAuthButton().click();
  };

Then("user is able to enter a username"),
  function () {
    loginPage.enterUsername().type(data.username);
  };

And("user is able to enter a password to authenticate"),
  function () {
    loginPage.enterPassword().type(data.password);
  };

And("user is able to click the login button"),
  () => {
    loginPage.clickLogin().click();
  };

Then("verify user logs into the appropriate page"),
  () => {
    landingPage
      .assertLoggedInMessage()
      .should("contain.text", "You logged into a secure area!");
  };

And("verify the body text context on the target page"),
  () => {
    landingPage.assertBodyMessage().should("contain.text", "Secure Area");
  };
