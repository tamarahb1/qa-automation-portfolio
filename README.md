# QA Automation Portfolio

## How to Run (Selenium)

### Prerequisites
- Python 3.x installed
- Google Chrome installed
- Selenium installed:
  - `pip install selenium`

### Run the test
From the `selenium` folder, run:
- `python test_login_saucedemo.py`

> Note: This is a portfolio demonstration using a public demo site.

## Selenium Examples
- Automated login test for Sauce Demo:
  - `selenium/test_login_saucedemo.py`

## How to Run (Cypress)

### Prerequisites
- Node.js installed
- Cypress installed:
  - `npm install cypress --save-dev`

### Run Cypress
- Open Cypress runner:
  - `npx cypress open`
- Or run headless:
  - `npx cypress run`

Test file:
- `cypress/saucedemo_login.cy.js`

## API Testing (Postman)

### Collection
- `api-testing/reqres-postman-collection.json`

### How to run
1. Download and open Postman
2. Import the collection JSON
3. Run requests individually, or use Collection Runner
4. Verify tests pass in the **Tests** tab output

This repository contains original automation scripts created for
public demo applications using tools such as Selenium, Cypress,
and Postman.

All scripts are written for portfolio demonstration purposes and
do not include proprietary systems or employer-owned code.
