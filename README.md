Welcome,

This system is an intra-net imagining of a medical warehouse's stock management system. With records for Stock, Customers, Sales and Users(Staff). 

The User acceptance criteria is for three groups of users(Staff); Clerks, Supervisors and Managers to be able to perform any variation of CRUD activities on Stock, Sales and Customers data according to the rights assigned to those three groups. 
The rights being:
- **Clerks** can create and update Sales records with only View rights to other Models.
- **Supervisors** possess only view rights.
- **Managers** posess create, update and delete rights on all the Models.

## User Experience(UX)
### User Stories
* Anonymous/Unregistered/First time User
    * As an anonymous user I should not be able to view any content without logging in
    * As an anonymous user I should be able to register for an account on the system.

* Clerk Goals
    * As a Clerk I expect to be able to add a new sale and modify and existing sale.
    * As a Clerk I expect to be able to view the Stock in the System
    * As a Clerk I expect to be able to view the Customers in the System
    * As a Cleark I expect to be able to view the Suppliers in the System

* Supervisor/Manager Goals
    * As a Supervisor I expect to be able to add, modify and delete existing sales records.
    * As a Supervisor I expect to be able to add, modify and delete existing Customers.
    * As a Supervisor I expect to be able to add, modify and delete existing Stock.
    * As a Supervisor I expect to be able to add, modify and delete existing suppliers.
    * As a Supervisor I expect to be able to view, modify and delete existing system users/staff.

### Design
* Colour Scheme
    * The main colours used are black and white, a white background with a black navigation bar. With the default Bootstrap buttons and colours used.

* Typography
    *

* Imagery
    * The site contains a solo image which is the company logo in the top left hand corner of the navigation bar

## Features
* Responsive on all device sizes

## Schema
There are four major models used.
**Stock** - Fields are name, unit_price and quality. Stores records of the stock in the warehouse.
**Sales** - Fields are customer, drug, quantity. Stores records of sales made which updates the related stock quantity value.
**Customer** - Fields are names, address, phone_number. Stores records of Customers to whom the drugs are sold. 
**User** - This is not explicitly defined. I extend the default Django user model.

## Technologies Used
### Languages Used
* Python
* HTML5
* CSS3

### Frameworks, Libraries & Programs Used
* Bootstrap was used to assist with the responsiveness and styling of the website.
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* GitHub is used to store the projects code after being pushed from Git.

The system is a Django system hosted on heroku over a Postgres database with SQLite used for initial testing.

## Testing
SQLite has been used for initial testing
The

