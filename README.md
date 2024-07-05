# CPI Ltd

**CPI Ltd** is a local community centre.  People can book children's birthday parties in the sports hall and a variety of other facilities. 

The user has the option to book parties as well as send a contact form with any other queries. 

The site can be accessed by this [link](https://cpi-ltd-project-38c4fa95377b.herokuapp.com/).


## Contents

* [User Stories](#user-stories)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Concept](#concept)
    * [Design](#design)
    * [Colors](#colors)
* [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Bugs](#bugs)
    * [Validator Testing](#validator-testing)
* [Technologies Used](#technologies-used)
* [Deployment](#deployment)
* [Future Improvements](#future-improvements)
* [Credits](#credits)
* [Tools](#tools)
* [Acknowledgments](#acknowledgments)

    

## User Stories
- User stories for the project can be found [here](https://github.com/users/RachelfromIreland/projects/2/views/1).

## Features

### Navbar

![Navbar Screenshot](/documents/images/navbar-screenshot.JPG)

- Positioned at the top of the page.
- Contains the name of the centre on the left side.
- Contains navigation links:
  - Home: Leads to the home page.  Users can learn about CPI Ltd, and can book parties or send a form for more information.
  - Book A Party: Leads to the booking form for parties.  If logged in a user can access the form and book.
  - Contact Us: Leads to the contact form page where users can fill out the form to send queries to staff.  Any user can use this, even if they don't have an account.
  - My Bookings: Visible to those who are logged in, My Bookings allows users to view and edit bookings.
  - Register and Login:  These options are available to new users to sign up or log in to book parties.
  - Logout: This option is available to logged in users to log out of their account.

The links have a subtle animated hover effect. 
The navigation is clear and easy to understand for the user.

The navigation bar is responsive:

On Mobile Devices the navigation bar is hidden and is toggled by a button on the right-hand side.

![Mobile navbar screenshot](/documents/images/nav-mobi.JPG) 

When the palette menu is clicked, there is a dropdown menu with the links in the same order. 

![Navbar expanded mobile screenshot](/documents/images/nav-mobi-full.JPG)

### Home Page
#### Contents:
- It has a fixed background image of the exterior of the centre.
- The main function of the centre.
- Lists the centre location and contact info.
- Contains a short blurb about the facilities within the centre.
- Has link to party booking form.
- Has link to contact form.
 
![Homepage](/documents/images/homepage.JPG)

### Book A Party Section
The Book A Party section has a fixed background image of the centre for consistency.
On the page is a form that contains:
- A heading reading "Book A Party!"
- Fields for the name on the booking, number attending, date and timeslot.
- The timeslots correspond to the two party slots per day the centre offers.
- A button that leads the user to a list of their bookings, also found under 'My Bookings' from the navbar.

![Book A Party](/documents/images/book-party.JPG)

### Contact Us Section
- The Contact Us Section contains a heading followed by the contact form.
- The form contains fields for name, email, phone and message.
- The form is powered by [Formspree](https://formspree.io/) and submitting the form sends the information to an email created for the project, cpiprojecttest@gmail.com.  More information on this can be found below.

![Contact Us](/documents/images/contact.JPG)

### Thank You Message
- The Thank You message appears after submitting the contact form.
- It contains a thank you message for the user.
- There is a button below the message which brings the user back to the home page.

![Thank you screenshot](/documents/images/contact-thank-you.JPG)

### My Bookings Section
- The My Bookings section has a welcome message for the user at the top.
- Following the message there is a list of all the parties the user has booked.
- Each listing has both an edit and a delete button.
- The edit and delete buttons allow the user to change or cancel their booking.

![My Bookings](/documents/images/booking-list.JPG)

### Register Section
- The Register Section has a form a new user can fill in to create an account.
- It contains fields for username and password as well as an optional email field.
- It is only visible to users who have not logged in.

![Register Screen](/documents/images/register.JPG)

### Login Section
- The Login Section allows a registered user to log in.
- It is only visible to users who have not logged in.

![Login Screen](/documents/images/login.JPG)

### Logout Section
- The Logout Section allows users to log out.
- It asks the user to confirm before logging out.

![Logout Screen](/documents/images/logout.JPG)

### Footer
The footer contains social media links that open in a new tab.  

![Footer](/documents/images/footer.JPG)

### Admin
- The django admin page allows the superuser to view, edit and delete all bookings.
- An admin login will be provided on submission for assessors.

![Admin Panel](/documents/images/admin-panel.JPG)


## Features

### Existing Features
- Django admin is utilised to allow staff to log in as a superuser.    
    - The superuser can view, edit and delete bookings for all users.
- After login, a user can book, view, edit and delete parties.  
    - If the party time slot is available the user will have the option to book it.
    - If a time slot is unavailable the user will be informed and asked to choose a different slot.
    - If a user wants to edit or delete bookings, they will have the option to cancel the changes.
- The contact form is powered by [Formspree](https://formspree.io/).
    - First, the user completes the form:

    ![A screenshot of the filled in contact form](/documents/images/email-test-form.JPG)

    - Then, a thank you message appears so the user knows their message was sent.

    ![A screenshot of the thank you message](/documents/images/contact-thank-you.JPG)

    - Through Formspree, forms are sent to a staff gmail account created for this project, cpitestproject@gmail.com.

    ![Screenshot of the email received](/documents/images/contact-email-result.JPG)
  

### Database Structure

Code Institute's [database site](https://dbs.ci-dbs.net/) was used to create the database for the project.

![A diagram of the database structure for the project](/documents/images/database.JPG)

#### Explanation

##### User Table
- Contains the basic fields for the user.  In this case they're id, username, email and password.  This model is provided by Django auth.

##### Booking Table
- The model for this table is found in [the book app.](/book/models.py) 
- It contains fields specific to a booking which are id, customer_id, booking_name, num_attending, date, time_slot, and booking_date.
- customer_id is a foreign key to the id in the User Table.

##### Relationships

- There is a one-to-many relationship between User and Booking because a user can have multiple bookings.
- The unique_together rule makes sure that no two bookings can have the same date and time_slot.  This ensures there will be no double bookings.


## Concept
### Flowchart
The original idea for the project can be seen in the basic flowchart below. 

![A flowchart showing the idea for the project](/documents/images/flowchart.JPG)

From there a wireframe was created to help visualise the project.

![The wireframe diagram used to plan the project](/documents/images/wireframe.JPG)

### Design
As CPI has a park and nature area on site green was chosen as the main site color.  Bootstrap was used to add color to button elements.
- Delete buttons appear in red to make them more noticeable to the user.
- Other buttons are light to tie in with the white text throughout the site.
- All pages use a background image of the exterior of the CPI complex.  As a community center, this was done to add familiarity to the user, and so that new users would recognise the building on arrival.

## Testing
- Details on testing for this project can be found [here](/documents/TESTING.md).

## Technologies Used
- Code Institute's GitPod Enterprise IDE was used for the development of the project.
- Git was used for the version control of the project.
- GitHub was used to host the code of the project.
- Django was used to build the project.
- Heroku was used to deploy the project.
- Bootstrap was used along with CSS to style the project.
- Whitenoise was used to handle static files.
- Gunicorn was used as a server for python.

### External Tools Used
- [Lucid Chart](https://www.lucidchart.com/pages/examples/flowchart-maker) was used to create the flowchart.
- [Formspree](https://formspree.io/) was used for the contact form.
- Code Institute's [database site](https://dbs.ci-dbs.net/) was used to create the database for the project.

## Deployment
This project was deployed using Heroku.

The steps to deploy are as follows:
- Fork or clone this repository.  The repository can be found [here](https://github.com/RachelfromIreland/CPI-Project).
- Log into your [Heroku](https://www.heroku.com) account, or create one if you haven't already.
- Navigate to 'New' in the upper right corner.
- Click create new app.  Give your app a unique name and choose the region closest to where you are.
- Link the repository to the Heroku app by pasting the [GitHub Repository link](https://github.com/RachelfromIreland/CPI-Project) into the Deploy tab.
- Click the deploy button under Manual Deployment. 

The live link can be found [here](https://cpi-ltd-project-38c4fa95377b.herokuapp.com/).

### Local Deployment
To make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone the repository:

git clone https://github.com/RachelfromIreland/CPI-Project

## Future improvements
- In the future, I would like to be able to implement more thorough user input validation.  As of now any date can be booked for a party, I would like to implement a 48 hour window which bookings should be made in advance of.
- I would also like to implement a feature that adds user email addresses to the database so they can be used by admin to send out a centre newsletter.
- For future projects, I would like to improve my commit messages.  I was very focused throughout the project and would often write a file and change it until it worked and then commit it.  This resulted fewer commit messages, which I think can be improved on next time.

## Credit
- Code Institute's [Django Blog](https://github.com/Code-Institute-Solutions/blog/tree/main) and [My Resume](https://github.com/Code-Institute-Solutions/resume-miniproject-bootstrap4/tree/master) walkthrough projects were invaluable in learning the skills needed for this project.  And the home page in particular was inspired by the layout of the Resume project.
- The background image for the project was taken from [castlefinn.ie](https://castlefinn.ie/points-of-interest/cpi-centre/).


## Acknowledgments
- This project was completed with the guidance of my mentor, Rory Patrick Sheridan.  His feedback was invaluable and his guidance made completing this project a very educational experience.
- User testing was completed by my fiancé, Caolán Curran.  His feedback enabled me to improve the site and create a more pleasant user experience. 
- The project was inspired by a conversation with my mother, Sylvia McGlinchey, the administrator at the real CPI Ltd.  