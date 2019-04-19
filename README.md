[![Build Status](https://travis-ci.org/Huckcity/milestone-project-five.svg?branch=master)](https://travis-ci.org/Huckcity/milestone-project-five)

# Unicorn Attractor

## Overview

Unicorn Attractor is all about the new wave of internet. It turns out there's a whole world of comedy surrounding it's development, and we can be a part of that by helping the developers track their progress and log any issues we find. This website's user functionality will allow you to create tickets and fund feature development.

### How does it work?

The UA website is a standard issue tracker system, with added functionality for contributing to development of new feature requests.
The users are able to post their own tickets, and vote on existing tickets, as well as contribute to the cost of development on feature requests.
Users can add contributions to their cart, and checkout via secure card payment with Stripe payment gateway.

## Live Demo

[Visit Unicorn Attractor Demo](https://milestone-project-five.herokuapp.com/)

Admin Login: admin

Admin Password: qwer1234


Standard User: newuser

Password: asdf

Also feel free to register another account. 

## Features

- Overview
    - The website allows users to register an account via the signup page. Registered users are then allowed to log tickets, which can be either `bug reports` or `feature requests`.
    - Users can also view other users tickets, and in the case of bugs they can upvote these bugs to indicate that they also have the issue, or in the case of feature requests they can contribute to the overall cost of development for that feature.
    - Payments are handled via the `Stripe` payment gateway for secure checkout.

- Accounts
    - Users are encouraged to register for an account via the Registration page. 
    - Once registered, a user may log in to their account with the username and password provided.
    - If a user forgets their password, they can reset is via the `Reset Password` page, which will send an email providing a link to reset the password
    - Each user has a personalised `Dashboard` which will display that users logged tickets, along with any comments that user has made on existing tickets.
    - The dashboard also facilitates the user to update their profile information such as name and email address. 
    - The user has a cart, which will track and hold any contributions the user wishes to make to feature requests
    - The user can log out at any time, though this will empty any items currently in the cart

- Tickets
    - Users can only edit their own submissions, and staff/admins can edit any ticket
    - All tickets have a comment section where users can post and relevant information or discussion on the ticket.

- Bugs
    - Bug tickets can be added by any registered user
    - Bug reports require a title, decription and optionally a URL to the place they found the bug, or an image of the bug if a screenshot was taken for example
    - Bugs are tracked and any user can upvote a bug to indicate that they also have the issue
    - A bug can only be upvoted once by each user, to keep an accurate overview of the number of users suffereing from a given issue
    - An administrator can edit the bug, and set the status to reflect it's current state i.e. Pending, In Progress or Complete



- Features
    - Feature Request tickets build on the same model as Bug Report tickets, with a field for setting the development cost also
    - Users can contribute to the development cost by inserting an amount to contribute, and adding the item to the cart
    - The features contribution progress is automatically tracked and updated in a progress bar as users contribute
    - Users receive a discount relating to the number of previous contributions made at a rate of 1.5% up to a maximum of 30%

- Blog
    - Users can create blog posts with any content they feel relevant
    - Users can comment on blog posts

- Stats
    - Statistics are presented through a number of graphs to keep users up to date on the activity on the site such as number of tickets per day, comments per day, average feature progress etc. 

- Cart
    - Users can add contributions to the cart from a feature request page
    - The items are stored and persist across the site, but are cleared upon logout
    - The user can view the cart, update any contribution values, and remove items from the cart
    - The user can checkout via the cart view, using the Stripe Payment Service


## Technologies used

- Frontend
    - HTML5
    - CSS3
    - Javascript
    - jQuery
    - Bootstrap 4
    - Font Awesome Icons
    - DC/D3 JS Graphs

- Backend
    - Python
    - Django 2.2
    - PostGreSQL
    - Stripe
    - Amazon AWS S3 Storage

## Testing

### Responsive testing and code validation

Cross browser testing has been performed to the best of my ability with available devices. The site is responsive and employs clean markup. 
The stats page is responsive on page load only, as it calculates based on container size at runtime, efforts were made to correct this but it will remain a stretch goal for now.

In terms of browser compatibility and display, I am relatively happy with the sites performance across multiple devices as follows:

- Desktop 24" 1920x1080 display
- Macbook Pro 15"
- iPad 4 9.7"
- Xiaomi Air 13" (Ubuntu)
- Honor Play 6.3"

### Automated testing

The automated testing on this project was implemented with Django's `unittest` module. There are limitless tests one could run on such a project, and I had to leave the remaining tests as a stretch goal, but have encluded enough to demonstrate a good working knowledge of the process.

- PAGES
    - Test Home page displays correctly via HTML status code 200
    - Test Register page displays correctly via HTML status code 200
    - Test Login page displays correctly via HTML status code 200

- Accounts
    - Test user login form with good credentials
    - Test user login form with bad credentials
    - Test user registration form with good credentials
    - Test user registration form with no email
    - Test user registration form with mismatched passwords

- Tickets
    - Test a user can create a ticket of type Bug Report
    - Test a user can create a ticket of type Feature Request
    - Test a ticket cannot be created without a default type
    - Test a ticket created will have the default status of Pending

All tests are automated and run via Travis Continuos Integration service. Due to the nature of TravisCI, many extra commits were required to debug it, from version compatibility issues such as the Django module 'six' being incompatible with certain Django versions to TravisCI themselves having a poor integration of the S3 'boto' module, which is set silently in the background of project setup.

Tests all pass and are tracked successfully on the Github page for this project.

Each apps tests are help in its own `tests.py` file and are run collectively with `python manage.py test`

# Manual Testing

This project has been through extensive manual testing all throughout it's development. A brief outline of manual tests performed:
- Tested all links from all pages
- Tested all forms for required field validation
- Tested all pages that require login to view
- Cart items stored across site, and cleared upon logout
- Cart items updateable and removeable
- Checkout figures charged correctly, and discounts applied correctly


## Deployment

In order to deploy the project you can follow these steps: 

### Local Deployment

The following assumes you have git and python preinstalled and configured to run terminal commands.

1. Make the directory you want to use and cd into it

![alt text](https://i.gyazo.com/d9449f9444563ee72fa21631c4ad1d0d.png)

2. Clone the repo into your directory

![alt text](https://i.gyazo.com/7c2de735df31fbaeab1c51fa7377a04d.png)

3. Change into project directory

![alt text](https://i.gyazo.com/87781ed35faff3603c6b3676e094c94d.png)

4. Create your virtual environment

![alt text](https://i.gyazo.com/9c9d80cae3cc11f61c05189654d6d7fa.png)

5. Start virtual environment

![alt text](https://i.gyazo.com/272a4fda3255b866e9900a29b2381983.png)

6. Install the dependencies from requirements.txt

![alt text](https://i.gyazo.com/62d93a2daf85062d74bbda9330200ed9.png)

7. Set up environment vars:

Create a local file in the root directory and set the following vars to your details
If you leave the DATABASE_URL commented, the database will use SQLite by default, which is preferred for dev deployment

- os.environ.setdefault("SECRET_KEY", "")
- os.environ.setdefault("SENDGRID_API_KEY", "")
- os.environ.setdefault("SENDGRID_USERNAME", "")
- os.environ.setdefault("SENDGRID_PASSWORD", "")
- os.environ.setdefault("AWS_STORAGE_BUCKET_NAME", "")
- os.environ.setdefault("AWS_ACCESS_KEY_ID", "")
- os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "")
- os.environ.setdefault("STRIPE_PUBLISHABLE_KEY", "")
- os.environ.setdefault("STRIPE_SECRET_KEY", "")
- #os.environ.setdefault("DATABASE_URL", ""

8. Make database migrations / migrate

![alt text](https://i.gyazo.com/4dff71ad331ff45933182b2ea93be894.png)

9. Collect static

![alt text](https://i.gyazo.com/597cfb225a01338688b30570a76ad9c4.png)

10. If you want to use the site with some preloaded data, this step is optional. If you don't perform this step, you will need to create a super user in order to log
in. You can do this with `python manage.py createsuperuser` and enter the requested details

```python
python manage.py shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
quit()
python manage.py loaddata db.json
```

![alt text](https://i.gyazo.com/b43459fb26f61908e111a86d7eb61f28.png)

11. Edit `settings.py` and set `DEBUG = True` for local testing

12. You shoud now be able to run the project with `python manage.py runserver`

To continue deployment on to Heroku, follow these steps:




Git init, add heroku app as remote

![alt text](https://i.gyazo.com/1b47ec221a5c2c364ebe3de0c5f61e6b.png)

then git commit -m "Initial commit"
git push heroku master

set secret key and disable_collectstatic

![alt text](https://i.gyazo.com/1199df45687bf466ba3d6a4e1dbcf9fc.png)

Update allowed hosts and set DEBUG = False

create super user on heroku

![alt text](https://i.gyazo.com/d91d262c26bda83f6b527501ab8b1e7e.png)


At this point, the app should be deployed successfully to Heroku, although without configuring an S3 storage bucket you will have no static files. These steps are outside the scope of this readme. See https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html for more info.

