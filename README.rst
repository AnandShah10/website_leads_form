===============
Concept Website Controller
===============

Description
-----------

This Odoo module creates a web page similar to the "Contact Us" page in the Odoo website module. The page, named "Leads", displays basic CRM fields such as name, partner ID, email, phone, expected revenue, and probability. At the end of the page, there is a "Submit" button. When users fill out the lead form and click on the submit button, a record is created in the CRM leads module with the filled information from the web page.

Functionality
-------------

- Creates a web page named "Leads" with CRM basic fields.
- Fields displayed on the webpage: name, partner_id, email, phone, expected_revenue, probability.
- Includes a "Submit" button at the end of the page.
- Upon clicking the "Submit" button, a record is created in the CRM leads module with the filled information.

Implementation Details
----------------------

- The module defines a template to display the lead form fields on the webpage.
- Analysis is done to understand how the "Contact Us" page in the Odoo website module is created and how values are passed at the submit button.
- A controller is defined to handle the submission of the lead form and creation of records in the CRM leads module.

Usage
-----

1. Navigate to the "Leads" page on the website.
2. Fill out the lead form fields including name, partner ID, email, phone, expected revenue, and probability.
3. Click the "Submit" button.
4. A record will be created in the CRM leads module with the filled information from the webpage.

References
----------

- This module takes reference from the "Contact Us" page of the Odoo website module.
- Analysis is done to understand the creation of the "Contact Us" page and how values are passed at the submit button.

Compatibility
-------------

- This module is compatible with Odoo version 17.0.

License
-------

GPL-3

Support
-------

For any questions, issues, or feedback regarding this module, please contact:
- shahanand1072004@gmail.com

Disclaimer
----------

This module is provided as-is, without any warranty, expressed or implied. Use at your own risk.
