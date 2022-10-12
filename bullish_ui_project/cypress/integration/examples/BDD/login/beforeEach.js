// this is used to bring in the Data from the fixture directory

let data;
beforeEach(function () {
  cy.fixture("example").then(function (fdata) {
    data = fdata;
  });
});
