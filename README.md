# QA Automation Portfolio

This repository contains original automation scripts created for
public demo applications using Selenium, Cypress, and Postman.

All scripts are written for portfolio demonstration purposes only
and do not include proprietary systems or employer-owned code.

---

## Demo Sources
- UI Demo App: https://www.saucedemo.com
- API Demo: https://reqres.in

---

## Selenium Automation (Python)

### Prerequisites
- Python 3.x
- Google Chrome
- Selenium installed:
  - `pip install selenium`

### How to Run
1. Navigate to the selenium folder:
   - `cd selenium`

2. Run the test:
   - `python test_login_saucedemo.py`

### Example
- Automated login test for Sauce Demo:
  - `selenium/test_login_saucedemo.py`

---

## Cypress Automation (JavaScript)

### Prerequisites
- Node.js installed
- Cypress installed:
  - `npm install cypress --save-dev`

### How to Run
- Open Cypress Test Runner:
  - `npx cypress open`
- Or run headless:
  - `npx cypress run`

### Example
- Cypress login test:
  - `cypress/saucedemo_login.cy.js`

---

## API Testing (Postman)

### Collection
- `api-testing/reqres-postman-collection.json`

### How to Run
1. Open Postman
2. Import the collection JSON
3. Run requests individually or using Collection Runner
4. Verify assertions pass in the **Tests** tab
