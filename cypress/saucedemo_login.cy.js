// Cypress Login Test for Sauce Demo
// Application: https://www.saucedemo.com
// Purpose: Portfolio demonstration using a public demo application

describe("Sauce Demo - Login", () => {
  it("logs in with valid credentials", () => {
    cy.visit("https://www.saucedemo.com/");

    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();

    cy.url().should("include", "/inventory.html");
    cy.contains("Products").should("be.visible");
  });
});
