# CPI Ltd

**CPI Ltd** is a local community centre.  People can book children's birthday parties in the sports hall and a variety of other facilities. 

![Program Startup Screenshot](/documents/program_screenshot.JPG)

The user has the option to book parties as well as send a contact form with any other queries. 

The site can be accessed by this [link](https://cpi-ltd-project-38c4fa95377b.herokuapp.com/).


## Contents

* [User Stories](#user-stories)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Concept](#concept)
    * [Flow Chart](#flow-chart)
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

# Navbar screenshot here
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

# Movile navbar screenshot here 

When the palette menu is clicked, there is a dropdown menu with the links in the same order. 

# Mobile expanded nav screenshot here

### Home Page
#### Contents:
- It has a fixed background image of the exterior of the centre.
- The main function of the centre.
- Lists the centre location and contact info.
- Contains a short blurb about the facilities within the centre.
- Has link to party booking form.
- Has link to contact form.
 
# Home page screenshot here

### Book A Party Section
The Book A Party section has a fixed background image of the centre for consistency.
On the page is a form that contains:
- A heading reading "Book A Party!"
- Fields for the name on the booking, number attending, date and timeslot.
- The timeslots correspond to the two party slots per day the centre offers.
- A button that leads the user to a list of their bookings, also found under 'My Bookings' from the navbar.

# Booking screenshot here

### Contact Us Section
- The Contact Us Section contains a heading followed by the contact form.
- The form contains fields for name, email, phone and message.
- The form is powered by ![Formspree](https://formspree.io/) and submitting the form sends the information to an email created for the project, cpiprojecttest@gmail.com.  More information on this can be found below.

# Contact screenshot here

### Thank You Message
- The Thank You message appears after submitting the contact form.
- It contains a thank you message for the user.
- There is a button below the message which brings the user back to the home page.

# Thank you screenshot

### My Bookings Section
- The My Bookings section has a welcome message for the user at the top.
- Following the message there is a list of all the parties the user has booked.
- Each listing has both an edit and a delete button.
- The edit and delete buttons allow the user to change or cancel their booking.

# My bookings screenshot here

### Register Section
- The Register Section has a form a new user can fill in to create an account.
- It contains fields for username and password as well as an optional email field.
- It is only visible to users who have not logged in.


# Register Screenshot here

### Login Section
- The Login Section allows a registered user to log in.
- It is only visible to users who have not logged in.

# Login Screenshot here

### Logout Section
- The Logout Section allows users to log out.
- It asks the user to confirm before logging out.

# Log out Screenshot here

### Footer
The footer contains social media links that open in a new tab.  

### Admin
- The django admin page allows the superuser to view, edit and delete all bookings.



## Features

### Existing Features
- Welcome Message with a prompt asking a user if they have visited before.    
    - Inputting 'yes' will prompt the user to enter their username and password.
    - Inputting 'no' will allow the user to create an account.
        - Validation functions ensure inputs meet the prompted requirements.
    - Any other response prompts a message stating a 'yes' or 'no' response is required.
- After login, a user can search for books by title.  
    - If the book is available the user will have the option to check it out.
    - If a book is unavailable the user will be informed of the return date.
    - If a title is not found the user will be prompted to try again and informed that titles are case sensitive.
- After searching for a book and taking one of the first two steps above, the user is given the option to search again or exit the program.  Choosing to exit begins the program again.
- The contact form is powered by ![Formspree](https://formspree.io/).
    - Forms are sent using this format:

    # Email format example

    - The forms are sent to a staff gmail account created for this project, cpitestproject@gmail.com.
    - The login information for this email will be provided on submission to allow assessors to test functionality.


### Future Features
- Allow staff members to pull user emails and send out information on upcoming community events. 


## Concept
### Flowchart
The original idea for the project can be seen in the basic flowchart below.  Specific functions and more detailed processes were added while writing the code.

# Flowchart screenshot

### Design
As CPI has a park and nature area on site green was chosen as the main site color.  Bootstrap was used to add color to button elements.
- Delete buttons appear in red to make them more noticeable to the user.
- Other buttons are light to tie in with the white text throughout the site.
- Important notes to the user appear in yellow, for example noting that book titles must appear as they do on the book.
- All pages use a background image of the exterior of the CPI complex.  As a community center, this was done to add familiarity to the user, and so that new users would recognise the building on arrival.


## Testing

### Manual Testing
#### Testing User Stories: First Time Visitors
| User Goal | How It Is Achieved |
| ---| ---|
| As a First Time User, I want the program to be easy to read and intuitive to navigate to ensure a pleasant user experience. | Colorama styles break up the text in the console and the prompts are descriptive and easy to understand. |
| As a First Time User, I want to easily create an account. | The user is walked through creating an account step by step with prompts, and error messages in red tell them when they need to edit their response. |
| As a First Time User, I want to be able to borrow a book. | After creating an account the user is prompted to search titles from the library and can check out any available ones. |


#### Testing User Stories: Returning Visitors
| User Goal | How It Is Achieved |
| ---| ---|
| As a Returning User, I want to be able to log in to my previously made account. | If a user states that they have used the program before they will be prompted to log in using their existing username and password. |
| As a Returning User, I want to see if a book I've had my eye on for a while which was previously unavailable is available to borrow. | The return date for the books is updated automatically on starting the program, any dates which have passed are removed and availability is set to 'Yes'. |


#### Full Testing

Full Testing was performed on the following physical devices.

##### Devices Tested:
- Windows PC with 32” Monitor
- Samsung Galaxy zFlip 4
- Windows laptop 17”
- Apple Macbook 12"

#### Functionality Tests
- All code was tested frequently at the time of writing by using devtools in the development server to check if everything was functioning as expected from writing the basic outline of the code through to testing the completed code.  Simple html messages were used to test everything was connected properly before the page structures were added in full.
- Forms were tested with basic structures before the full structure was added, with the exception of the contact form which was tested with email.

### Bugs
#### Solved Bugs
| Bug | Solution |
| ---| ---|
| All books in the spreadsheet were flagged as unavailable whether availability was 'no' or not. | Solution: Used .value() to return the cell value to be able to compare it to the string used in the function. |
| The program crashed when trying to update the books spreadsheet and when running the function to update the return dates. | Used .strptime() to ensure the date format in the code matched the date format of the spreadsheet. Checked the cell format on the spreadsheet when the error persisted and ensured the entire column was formatted the same way. |
| Running the update returns function just resulted in an error on the console. | After running some more tests and Googling the error messages, the empty cells in the column were found to be preventing the function from working.  Adding an extra if statement to only have the function look for cells with dates resolved the issue. |

#### Unsolved Bugs
No unsolved bugs were detected after testing.

### Validator Testing
- The program was tested using [PEP8](https://pep8ci.herokuapp.com/). No errors were found.
- A screenshot of the results can be found [here](/documents/PEP8_validation.png).


## Technologies Used
- Code Institute's GitPod Enterprise IDE was used for the development of the program.
- Git was used for the version control of the program.
- GitHub was used to host the code of the program.
- Heroku was used to deploy the program.

## Deployment
This project was deployed using Heroku.

The steps to deploy are as follows:
- Fork or clone this repository.
- Create a new Heroku app.
- Link the repository to the Heroku app.
- Click the deploy button. 

The live link can be found [here](https://cpi-ltd-project-38c4fa95377b.herokuapp.com/).

## Future improvements
- In the future, I would like to be able to implement more thorough user input validation.  As of now any date can be booked for a party, I would like to implement a 48 hour window which bookings should be made in advance of.
- I would also like to implement a feature that adds user email addresses to the database so they can be used by admin to send out a centre newsletter.
- For future projects, I would like to improve my commit messages.  I was very focused throughout the project and would often write a file and change it until it worked and then commit it.  This resulted fewer commit messages, which I think can be improved on next time.

## Credit
- CI Django Blog and My Resume - LINK HERE


## Tools
- [Lucid Chart](https://www.lucidchart.com/pages/examples/flowchart-maker) was used to create the flowchart.
- [Formspree](https://formspree.io/) was used for the contact form.

## Acknowledgments
- This project was completed with the guidance of my mentor, Rory Patrick Sheridan.  His feedback was invaluable and his guidance made completing this project a very educational experience.
- User testing was completed by my fiancé, Caolán Curran and mother, Sylvia McGlinchey - administrator at the real CPI Ltd.  His feedback enabled me to improve the site and create a more pleasant user experience.