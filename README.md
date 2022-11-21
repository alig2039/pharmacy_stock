Welcome,

<img src="https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1668849841/Screenshot_2022-11-19_121142_zpaphl.jpg">

This system is an intra-net imagining of a medical warehouse's stock management system. With records for Stock, Customers, Sales and Users(Staff). 

The User acceptance criteria is for three groups of users(Staff); Clerks and Supervisors/Managers to be able to perform any variation of CRUD activities on Stock, Sales and Customers data according to the rights assigned to those three groups. 
The rights being:
- **Clerks** can create and update Sales records with only View rights to other Models.
- **Supervisors** possess only view rights.
- **Managers** posess create, update and delete rights on all the Models.

## User Experience(UX)
### User Stories
* Anonymous/Unregistered/First time User
    * As an anonymous user I want to be able to register for an account on the system so that i can perform the tasks my role requires.

* Clerk Goals
    * As a Clerk I want to add a new sale and modify existing sales records.
    * As a Clerk I want to view the Stock in the System so that I am able to know which items are in stock before i can add a sales record.
    * As a Clerk I want to view the Customers in the System so that I am able to know which Customers can buy product.
    * As a Clerk I expect to be able to view the Suppliers in the System so that i am able to know Suppliers from whom the product comes.

* Supervisor/Manager Goals
    * As a Supervisor I want to add, modify and delete existing sales records.
    * As a Supervisor I want to add, modify and delete existing Customers so that they can be available for selection when adding new Sales records.
    * As a Supervisor I want to add, modify and delete existing Stock so that Sales are made according to accurately existing stock.
    * As a Supervisor I want to add, modify and delete existing suppliers so that new stock records can be added.
    * As a Supervisor I want be able to activate newly registered users and assign the right groups and rights to them. I want to also be able to delete or deactivate user accounts of staff no longer with the company.

    ## Authetication / Managerial Login
* The manager will be given the first login credentials that have been created through Django and from then onwards he can allocate rights to the different users. These credentials will also be provided to the examiner for easier access.

### Design

<img src="https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1668849840/Screenshot_2022-11-19_121417_l8z9yi.jpg">
<img src="https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1668849841/Screenshot_2022-11-19_121938_tm694g.jpg">
<img src="https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1668849841/Screenshot_2022-11-19_122103_id4klp.jpg">
<img src="https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1668849841/Screenshot_2022-11-19_121238_sre8yp.jpg">

* Colour Scheme
    * The theme is dominantly white with blue links, logo and buttons to create contrast.

* Imagery
    * The site contains a solo image which is the company logo.

## Wireframes
* List/table [page](https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1668847841/list_page.drawio_zmjcgc.png)
* Item Details. Similar to List page as a table is used without the Add Item button at the bottom [page](https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1668847841/item_detail.drawio_hfhkwc.png)
* Form Page. Also applicable to item modify/update pages [design](https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1668847841/form_page.drawio_g34gpv.png)

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
* [Python](https://www.python.org/)
* [HTML5](https://html.com/html5/)
* CSS3

### Frameworks, Libraries & Programs Used
* [Django](http://www.djangoproject.com/) was used to build the site.
* [Bootstrap](https://getbootstrap.com/) was used to assist with the responsiveness and styling of the website.
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) is used to store the projects code after being pushed from Git.
* [Heroku](heroku.com) used as a host.

## Testing
### Testing User stories
* Anonymous/Unregistered/First time User
    * As an anonymous user I want to be able to register for an account on the system so that i can perform the tasks my role requires. A new user is taken to the login form to log into the system. A link to 'Create You own account' is at the bottom of the login form which would take you to the Registration form. After submitting this form, a manager has to log in and activate the account and assign the necessary permissions before that user can log in.

* Clerk Goals
    * As a Clerk I want to add a new sale and modify existing sales records. At the bottom of the Sales page, showing a table with a list of sales, there is a "Add New Sale" button that takes a user to the Add Sale form if they have the right permissions for it. Adding a new sale automatically reduces the stock count based on the quantity of the sale.
    * As a Clerk I want to view the Stock in the System so that I am able to know which items are in stock before i can add a sales record. This can be viewed from the Stock page that shows a table with stock in the system. A clerk should not have the rights to add, modify or delete stock so those options are not available to this user. 
    * As a Clerk I want to view the Customers in the System so that I am able to know which Customers can buy product. This can be viewed from the Customers page that shows a table with the customers added to the system. A clerk does not have the rights to add, modify or delete stock so those options are not available to this user.
    * As a Clerk I expect to be able to view the Suppliers in the System so that i am able to know Suppliers from whom the product comes. This can be viewed from the Suppliers page that shows a table with the Suppliers added to the system. A clerk does not have the rights to add, modify or delete suppliers so those options are not available to this user.

* Supervisor/Manager Goals
    * As a Supervisor I want to add, modify and delete existing sales records. The sales page shows a table with a list of sales entries. The bottom of the page has a button that allows a user to add a new Sales record. The Update and Delete links are on the right of each item row on the table, following these links takes the user to forms where updates can be done or where the record can be deleted.
    * As a Supervisor I want to add, modify and delete existing Customers so that they can be available for selection when adding new Sales records. The Customers page shows a table with a list of customers. The bottom of the page has a button that allows a user to add a new customer. The Update and Delete links are on the right of each item row on the table, following these links takes the user to forms where updates can be done or where the record can be deleted.
    * As a Supervisor I want to add, modify and delete existing Stock so that Sales are made according to accurately existing stock. The Stock page shows a table with a list of stock entries. The bottom of the page has a button that allows a user to add a new stock record. The Update and Delete links are on the right of each item row on the table, following these links takes the user to forms where updates can be done or where the record can be deleted.
    * As a Supervisor I want to add, modify and delete existing suppliers so that new stock records can be added. The Suppliers page shows a table with a list of suppliers. The bottom of the page has a button that allows a user to add a new supplier. The Update and Delete links are on the right of each item row on the table, following these links takes the user to forms where updates can be done or where the record can be deleted.
    * As a Supervisor I want be able to activate newly registered users and assign the right groups and rights to them. I want to also be able to delete or deactivate user accounts of staff no longer with the company. The staff page has a table showing a list of all the users. For each record there is an Update or Delete link at the right of the row. Following the Update links takes the user to a page that inherits from Django's default user management page, this allows the manager to activate and assign groups and permissions to the user. Clicking the delete link takes the manager to a page where that user can be deleted.

### Further Testing
<img src+"https://res.cloudinary.com/allan-gerald-sserwanga/image/upload/v1669007458/tests_kofxdu.jpg">

* Automated testing of models and views was written into a tests.py file. Results above.
* The site was tested on Google chrome and Ms Edge browsers.
* A local SQLite database is used for testing data and values with a Postgres database used in production

## Deployment
The project was developed and deployed to Heroku using the following steps.
* Cloned the Heroku django starter template following this [guide](https://devcenter.heroku.com/articles/getting-started-with-python)
* Created a Github repository, added it as a remote and pushed to this repository.
* Modified the Heroku template to suite my needs. Based on the user stories and general idea of what the intention of the system was, a stock manager app was created and models required for customers, suppliers, staff and stock were created. Views were created based on Django class based views with the default Create, Update, View and Delete views used to give CRUD functionality. This was complimented by custom calculations such as that which reduces the stock count at every sale. User management and access control was also implmeneted by extending the default Django auth model and views incluing the login and user registrations views.
* Styling was assisted by the Bootstrap HTML theme used.

## Credits
### Acknowledgements
* My Mentor Celestine for continuous helpful feedback.




