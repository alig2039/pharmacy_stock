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
    * As a Cleark I expect to be able to view the Suppliers in the System so that i am able to know Suppliers from whom the product comes.

* Supervisor/Manager Goals
    * As a Supervisor I want to add, modify and delete existing sales records.
    * As a Supervisor I want to add, modify and delete existing Customers so that they can be available for selection when adding new Sales records.
    * As a Supervisor I want to add, modify and delete existing Stock so that Sales are made according to accurately existing stock.
    * As a Supervisor I want to add, modify and delete existing suppliers so that new stock records can be added.
    * As a Supervisor I want be able to activate newly registered users and assign the right groups and rights to them. I want to also be able to delete or deactivate user accounts of staff nolonger with the company.

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
* Automated testing of URLs and URL names has been implemented and successfully carried out using the Django testing module.
* User stories were tested to support the View and CRUD functionality imeplemented and expected for every user and every user group

### Further Testing
* The site was tested on Google chrome and Ms Edge browsers.
* A local SQLite database is used for testing data and values with a Postgres database used in production

## Deployment
The project was developed and deployed to Heroku using the following steps.
* Cloned the Heroku django starter template following this [guide](https://devcenter.heroku.com/articles/getting-started-with-python)
* Created a Github repository, added it as a remote and pushed to this repository.
* Modified the Heroku template to suite my needs.

## Credits
### Acknowledgements
* My Mentor Celestine for continuous helpful feedback.




