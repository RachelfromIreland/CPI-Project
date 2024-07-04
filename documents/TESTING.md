# Testing

## Testing User Stories: 
| User Goal | How It Is Achieved |
| ---| ---|
| Book a party | After logging in, clicking on the Book A Party navbar item or on the button on the homepage allows the user to access the form to book a party.  This form adds a new item to the database which can be viewed by the user who added it or by admin.  Testing involved creating the basic form and using devtools to look for any errors. |
| View information about the facility | The user can view information about the facility on the homepage.  The format was tested by first adding a basic skeleton structure and styles before adding the content. |
| Change or delete bookings as a user  | Once logged in and viewing the My Bookings page, the user can edit and delete their bookings. This was tested by creating multiple bookings for a single user and then editing and deleting them.  Styles were added later and functionality was tested throughout this process. |
| Enquire about services other than parties | The user can fill out a form which will send an email to the staff email created for the project.  This was tested throughout by submitting the form multiple times with different messages to denote different tests, and checking the console in devtools for any errors.  It was tested throughout the development and styling process to ensure no changes impacted functionality. |
| View bookings as staff | A staff login was created by adding a superuser with django.  The superuser was then tested by creating some regular users and adding multiple bookings to ensure the superuser could see all bookings in the /admin page. |
| Edit and delete bookings as admin | The superuser can also edit and delete bookings, and this was tested by creating multiple bookings by multiple users and having the superuser edit and delete some of these bookings. |
| View Bookings as a user | Once logged in the user can view their bookings by clicking My Bookings in the navbar, or by being redirected after a booking.  This was tested throghout by creating multiple users to ensure they could only see bookings they had created, and styles to make the list more user friendly were added later. |


## Manual Testing

Full Testing was performed on the following physical devices using Chrome Devtools to check responsiveness.

### Devices Tested:
- Windows PC with 32” Monitor
- Samsung Galaxy zFlip 4
- Windows laptop 17”
- Apple Macbook 12"

### Browser Testing

During development, the testing was mainly with Google Chrome.

In production the site has been tested on the following browsers:
- Google Chrome
- Mozilla Firefox
- Opera
- Microsoft Edge

## Functionality Tests

### Navigation Bar 
- Navigation bar was tested for responsiveness and is fully responsive on small, medium and large screens.
- On small screens, the menu icon appears and the menu items are hidden.  This is reversed on medium and larger screens.
- All links are redirecting to the correct pages. 
- When signed out the options to register or sign in are visible.
- When signed in the options to log out and 'My Bookings' are visible.
- The active page is brighter than the others.
- Each link has a subtle hover effect.


### Footer
- Links redirect to the correct social media page.
- Links open in a new browser tab. 

### Home Page
- The home page is fully responsive and content is displayed on all screen sizes.
- The book and contact buttons redirect to the correct pages.
- The header and footer are fully visible on all screen sizes.
- If a user is logged in their username is displayed in the upper right corner.
- If a user is not logged in a message stating they aren't logged in is displayed.


### Book a Party
- The user is redirected to the sign up page if they are not logged in.
- Both sign in and sign up buttons redirect to the correct pages.
- If the user is signed in they can access Book A Party again and this time the form loads.
- All fields in the form are required and cannot be left blank.
- Double bookings are prevented with a message to the user.
- Clicking book now after entering all fields correctly redirects to the bookings list as planned.


### My Bookings
- The page loads correctly if the user is logged in and the page cannot be accessed if the user is logged out.
- The page correctly displays a list of the user's bookings and the list displays the name, date and time.
- Each booking in the list contains an edit and delete button, and these redirect to the correct pages.
- The list is easy to read and navigate, and the username is visible in the message at the top of the list.
- If a user has no bookings, a message is displayed confirming this.


### Edit Booking
- After clicking on the Edit button on a booking the user is correctly redirected to the edit page.
- All fields are again required and cannot be left blank.
- Changing to a timeslot that is already booked again gives a message to the user that they need to choose another time.
- Save correctly saves the changes and brings the user back to the booking list.
- Cancel correctly redirects back to the booking list without making any changes.

### Delete Booking
- Clicking on the Delete button on a booking correctly redirects to the delete page.
- The message asking a user if they're sure they wish to delete is displayed correctly.
- Clicking cancel correctly redirects back to the booking list.
- Clicking delete removes the booking from the list.

### Contact Us
- Clicking either of the contact buttons on the homepage correctly loads the contact form.
- All fields with the exception of phone number are required and cannot be left blank, email is the default communication for staff as it is an email they will receive.  A phone number is optional.
- The form being submitted correctly sends an email to the staff email address.
- When all fields are filled out a thank you message is diaplayed.
- The button on the thank you message correctly returns a user to the home page.


### Register
- Django auth is loading correctly and a user is able to register a new account.
- Form correctly responds to invalid inputs.
- Redirects to the home page correctly.

### Log In
- Django auth is loading correctly and a user is able to log in to their account.
- Form correctly responds to invalid inputs.
- Redirects to the home page correctly.

### Log Out
- Django auth is loading correctly and a user is able to log out of their account.
- The message asking if a user wants to log out is loading correctly.
- Clicking the button on the message redirects to the home page correctly.


## Bugs
### Solved Bugs
| Bug | Solution |
| ---| ---|
| The contact us form was not resulting in an email to the staff inbox | After trying and failing to integrate email into django directly due to gmail security features, a third party site, [Formspree](https://formspree.io/), was used to send the contact form. This should also help future proof the site in the event of more security changes from email providers.  |
| Urls for the project were not loading | The urls for the site were resulting in path not found errors. After troubleshooting, adding the app name to the top of each app's urls.py file solved the issue. |
| The styles added with CSS were not loading | The STATIC_URL and STATIC_FILES_DIRS had not been added to settings.py correctly.  Fixing this error solved the issue. |

### Unsolved Bugs
| Bug | Explanation |
| ---| ---|
| User can book parties in the past | While testing it was discovered that the user can book parties in the past.  This will be corrected for future deployments if the site is to be used as the company website.  Due to time constraints it was not fixed before project submission. |

## Validator Testing
# Update validator testing here
- CSS
    - No errors were found when passing through the official [(Jigsaw)](https://jigsaw.w3.org/css-validator/) validator.
    - An image of the result can be found [here](/documents/images/validator_screenshots/css-valid.JPG).
- JavaScript
    - No errors were found when passing through the official [Jshint](https://jshint.com/) validator
    - An image of the result can be found [here](/documents/images/validator_screenshots/js-valid.JPG).

- HTML files were validated with the official [W3C validator](https://validator.w3.org/nu/).  Only files that were created or edited were validated, files added by django and not touched were not.  Results are below with links to screenshots.

| HTML Files | Validation Passed? |
| ---| ---|
| book/book_party.html |  |
| book/delete_booking.html |  |
| book/edit_booking.html |  |
| book/party_list.html |  |
| contact/contact.html |  |
| home/home.html |  |
| account/login.html |  |
| account/logout.html |  |
| account/signup.html |  |
| base.html |  |

- Python files were tested using [PEP8](https://pep8ci.herokuapp.com/).  Only files created and modified were validated.  Results are below with links to screenshots.

| Python Files | Validation Passed? |
| ---| ---|
| book/forms.py | [Yes](/documents/images/validator_screenshots/python_validation/book-forms-valid.JPG) |
| book/models.py | [Yes](/documents/images/validator_screenshots/python_validation/book-models-valid.JPG) |
| book/urls.py | [Yes](/documents/images/validator_screenshots/python_validation/book-urls-valid.JPG) |
| book/views.py |  |
| contact/forms.py | [Yes](/documents/images/validator_screenshots/python_validation/contact-form-valid.JPG) |
| contact/urls.py | [Yes](/documents/images/validator_screenshots/python_validation/contact-urls-valid.JPG) |
| contact/views.py | [Yes](/documents/images/validator_screenshots/python_validation/contact-views-valid.JPG) |
| cpi_ltd/urls.py | [Yes](/documents/images/validator_screenshots/python_validation/cpi-urls-valid.JPG) |
| home/urls.py | [Yes](/documents/images/validator_screenshots/python_validation/home-urls-valid.JPG) |
| home/views.py | [Yes](/documents/images/validator_screenshots/python_validation/home-views-valid.JPG) |
