const { defineConfig } = require("cypress");
const cucumber = require("cypress-cucumber-preprocessor").default;

module.exports = defineConfig({
  projectId: "eiv1yu",
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
      on("file:preprocessor", cucumber());
    },
    specPattern: "cypress/integration/examples/*.js",
    reporter: "mochawesome",
    env: {
      url: "http://the-internet.herokuapp.com/",
    },
  },
});
