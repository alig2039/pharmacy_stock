Welcome,

This system is an imagining of a medical warehouse's stock management system. With records for Stock, Customers, Sales and Users.

The User acceptance criteria is for three groups of users; Clerks, Supervisors and Managers to be able to perform any variation of CRUD activities on Stock, Sales and Customers data according to the rights assigned to those three groups. 
The rights being:
- **Clerks** can create and update Sales records with only View rights to other Models.
- **Supervisors** possess only view rights.
- **Managers** posess create, update and delete rights on all the Models.

## Schema
There are four major models used.
**Stock** - Fields are name, unit_price and quality. Stores records of the stock in the warehouse.
**Sales** - Fields are customer, drug, quantity. Stores records of sales made which updates the related stock quantity value.
**Customer** - Fields are names, address, phone_number. Stores records of Customers to whom the drugs are sold. 
**User** - This is not explicitly defined. I extend the default Django user model.

## Technologies Used
The system is a Django system hosted on heroku over a Postgres database with SQLite used for initial testing.

## Testing

