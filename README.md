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



### Automated testing

- Accounts
    - Test user login form with good credentials
    - Test user login form with bad credentials
    - Test user registration form with good credentials
    - Test user registration form with no email
    - Test user registration form with mismatched passwords

- 

