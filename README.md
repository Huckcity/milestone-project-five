[![Build Status](https://travis-ci.org/Huckcity/milestone-project-five.svg?branch=master)](https://travis-ci.org/Huckcity/milestone-project-five)

# Unicorn Attractor

## Overview

Unicorn Attractor is all about the new wave of internet. It turns out there's a whole world of comedy surrounding it's development, and we can be a part of that by helping the developers track their progress and log any issues we find. This website's user functionality will allow you to create tickets and fund feature development.

### How does it work?

The UA website is a standard issue tracker system, with added functionality for contributing to development of new feature requests.
The users are able to post their own tickets, and vote on existing tickets, as well as contribute to the cost of development on feature requests.
Users can add contributions to their cart, and checkout via secure card payment with Stripe payment gateway.

## Live Demo

[Visit Unicorn Attractor Demo](https://milestone-project-five.herokuapp.com/).

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

- Bugs
    - Bug tickets can be added by any registered user
    - Bug reports require a title, decription and optionally a URL to the place they found the bug, or an image of the bug if a screenshot was taken for example
    - Bugs are tracked and any user can upvote a bug to indicate that they also have the issue
    - A bug can only be upvoted once by each user, to keep an accurate overview of the number of users suffereing from a given issue
    - An administrator can edit the bug, and set the status to reflect it's current state i.e. Pending, In Progress or Complete
    - Users can comment on any bug reports with relevant comments and information


- Features
    - Feature Request tickets build on the same model as Bug Report tickets, with a field for setting the development cost also
    - Users can contribute to the development cost by inserting an amount to contribute, and adding the item to the cart
    - The features contribution progress is automatically tracked and updated in a progress bar as users contribute
    - Users receive a discount relating to the number of previous contributions made at a rate of 1.5% up to a maximum of 30%
    - All tickets have a comment section where users can post and relevant information or discussion on the ticket.

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



### Automated testing

- Accounts
    - Test user login form with good credentials
    - Test user login form with bad credentials
    - Test user registration form with good credentials
    - Test user registration form with no email
    - Test user registration form with mismatched passwords

- 

### Manual testing
<details>
<summary>Click to see details</summary>
<br />

I conducted manual tests on a number of features on the website - these are documented below.

#### Authorisation

I tested the security aspect of my project, which means users who have not met certain conditions will not be able to access some restricted areas of the site. This mainly concerns the Profile, Log Out and Checkout pages. When a user tries to reach any of those pages while not logged in they will get redirected back to the Log In page and so any potential errors are avoided.

This is achieved by using a `@login_required` decorator at the head of each relevant view in *accounts/views.py* as well as *checkout/views.py*, which will check whether a user is logged in before taking them to any of those pages.

#### Navigation

I tested the navigation aspect of my website to make sure that all the links provided take the user exactly where they are supposed to. A major part of this is the navigation bar at the top of every page. The *Products* drop-down menu functions correctly as part of this. Additionally, the **Breadcrumbs** feature also works well.

All of the above has also been tested on smaller screen devices and I can confirm that everything - including the collapsible 'navbar' menu - works as intended. This of course is also a big part of Responsive testing and so needs to be spot on.

#### Products and Cart pages

I tested the input of various numbers into the product quantity fields on the products pages and the cart page. Users can successfully add a minimum of 1 item (from a choice of one or more products on offer) to the cart. If there were to be any attempt to add anything less (i.e. '0' items) the system would prevent that from happening. This is achieved using a combination of `value="1"` and `min="1"` attributes, which between them ensure that the user will be able to add a minimum of 1 item to the cart and that on page load that is the default number displayed in all the input fields as a prompt for the user. Also, to avoid any potential issues with large numbers the maximum input limit was set to 999 (`max="999"`).

On the cart page, however, it was necessary to set the required minimum to 0 (`min="0"`) on all input fields because we still want the users to be able to amend the quantity of any product item down to 0 if they wish to remove a given product from the cart.

#### Checkout page

I tested the functionality of the payment form on the checkout page to ensure that validation is working correctly when the user either doesn't fill in a required field or types invalid information into one of them. This is certainly true for each field concerned (as you get an error message if a requirement is not met) so the form passes in all respects.

Additionally, after you submit the form it redirects you to the products page and you get a successful submission message near the top of the page, as intended, so once again the test is a success.

#### Contact page

I tested the Contact form on this page and verified that all the required fields do indeed have a validation message coming up for each of them (asking the user to fill it in) if the user tries to submit the form while leaving any of them blank. The one exception to this is the *Phone number* field, which is not required, however if the user enters an invalid number (in this case a number of any length other than 10 or 11 digits) then an error message will come up. If this field is left blank though - provided everything else is filled in - the form will still submit successfully. So I have verified that the form submission is accepted when inputs are valid and denied when an invalid input is provided for any of the fields.

Upon submission of the form the user should be redirected to the home page and get a successful submission notification near the top of the page. Additionally, the user should receive an email on the same email address they provided on the form, telling them that their enquiry has been received and somebody will be in touch. The email reply should also contain confirmation of all the details the user provided on the form. After testing I can confirm that all of this works as intended.

#### Issue with Contact form

I had to set up the use of an external mail server for sending emails with automatic replies to users who filled out my contact form and for this project we were advised to use a simple and free provider, namely **Gmail**. Simple, that is, as long as you have a Google/Gmail account, which I do.

Now, because Google take the security of people's accounts and associated email accounts quite seriously for obvious reasons, there is unfortunately an unavoidable problem that comes with using your personal Google account as a server for sending emails. The first time that I tried to submit the contact form on my live site I got a *server error* message because Google was blocking my 'sign in' attempts as they thought somebody else was trying to sign into my account from an "unrecognised device" and/or in an "unusual location".

I was able to resolve the issue initially by going to my Google account and turning on an option to "allow less secure apps" to access my account. However, it turned out that an additional measure had to be taken to get rid of the server error and that was to go to a *DisplayUnlockCaptcha* page on my account and click a button to "allow access to my Google account".

When it seemed that this email issue was finally resolved it then happened again about a couple of weeks later. Thankfully I was able to take care of it straight away by going to the *DisplayUnlockCaptcha* page once more. However, if it can happen to me again so soon after verifying my account and while I was testing the contact form on the same (recognised) device then it can certainly happen to anybody else testing my form from another location and/or device.

Users of my website need to be aware of this potential problem should they get a *server error* message when trying to submit the contact form. Unfortunately, this is a third-party issue and is therefore out of my control.

#### Database

The main thing to test here was the correct functionality of MySQL (ClearDB) database on Heroku - namely that it serves all the product information (that has been uploaded there) to all the relevant web pages and that it successfully stores new user data and retrieves it when users sign in, etc.

With regards to displaying all the requested product information, I checked every single product page, then the cart page (with a number of different product combinations added to it) and finally the checkout page (displaying the same selections as the cart page) and found no problems in relation to any missing data.

As for storage of user data, I tested by registering different users, logging out and then back in and every time authentication was successful. Therefore the logical conclusion here is that the database functions efficiently and as intended.

</details>

## Deployment

Firstly, to prepare for deployment, my project's main settings file had to be adapted for the different environments that the project would go through. I created a **settings** package/directory (as an app) and within it I set up **base.py**, **dev.py** and **staging.py**. The base.py is the main settings file (for the default environment) and contains settings that are shared across all three environments. The next file provides the settings for the project's development environment and the final file provides the settings for the staging environment - respectively. Each of the latter files adds some extra settings (to the base.py) that are only needed for that particular environment.

The other thing that needed to be done was to ensure I have the correct dependencies for each of the environments. This was done by creating a **requirements** directory (also in the project root) and then **base.txt**, **dev.txt** and **staging.txt** inside there. The original *requirements.txt* file was kept in the root directory since Heroku still looks for it in order to check for dependencies.

At this point the original project code had already been pushed to the appropriate remote repository on my GitHub account. So the next stage was to set up Heroku to host my website and to connect it to my GitHub account and the particular remote repository (master branch) that hosts the project code.

The following steps were taken to achieve this:

- A new Heroku app (Europe region) was created on my Heroku account
- Under the *Deploy* tab of my app in the 'Deployment method' section I selected GitHub and found my project's repository
- I then granted Heroku access to it via *Authorise application* and then enabled 'Automatic deploys' from GitHub (enabling Heroku to deploy the latest code that's uploaded to the repository)
- A python package called **gunicorn** was installed and added to **base.txt**, since it is needed to run Python web applications on Heroku
- Also added **Procfile** and **Procfile.local**, as well as **runtime.txt** (which should tell Heroku to use the latest version of Python, even if your local project isn't doing so)
- Then I set the ```DJANGO_SETTINGS_MODULE``` variable to **settings.dev** on the local project; and also set the environment on Heroku to use **settings.staging**
- Additionally, **whitenoise** package was installed to serve static files on Heroku

Another important part of the process was to set up Stripe connection details on Heroku to enable users to make payments on the live site. That involved copying the environment variables - ```STRIPE_PUBLISHABLE``` and ```STRIPE_SECRET``` keys (which were originally generated on my Stripe account) from either **dev.py** or **staging.py** and placing them in the 'Config Vars' section under the *Settings* tab on Heroku.

One of the last things to do was to set up a database on Heroku. Under the *Resources* tab of my app in the 'Add-ons' section I found **ClearDB MySQL** and provisioned it for the app. At that point the database automatically created a new *Config Variable* (```CLEARDB_DATABASE_URL```) that stores all the info needed to connect to it remotely. This is found under the *Settings* tab in 'Config Vars' section. Finally, I added the environment variables for that database in my **staging.py** file so that URL could be used to connect to my database. Also, the **dj-database-url** package was installed locally and added to **staging.txt** in order to retrieve the value of the *Config Variable* from Heroku to generate the database connection details.

Additionally, the cloud database needed to be populated with the same data that I was using locally, so first of all, migrations were run on Heroku to create tables on **ClearDB**. Then the local database was 'dumped' into a *json* file (using the **dumpdata** command) which was then pushed to my GitHub repository. Finally, the data was loaded into the staging database on Heroku using the generated *json* file.

It is worth mentioning that all the product information in the local database was initially loaded up from a csv file called *price_list.csv* that can be found in the *docs* folder.

## Wireframing

I used **Balsamiq Mockups** to create a wireframe/storyboard for my website and the mockup files can be found in the *docs* folder.

## Credits

### Content

Courtesy of the press release published by the trade association [AVIXA](https://www.avixa.org/about-avixa/who-we-are/press-room/2017/10/02/avixa-releases-global-av-industry-outlook-and-trends-analysis)

### Acknowledgements

A special thank you to **@mr_bim** and **@mormoran** who helped me out with some minor but nonetheless tricky aspects of the project.