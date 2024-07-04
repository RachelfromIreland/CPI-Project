# Testing

## Manual Testing
### Testing User Stories: 
| User Goal | How It Is Achieved |
| ---| ---|
| Book a party | After logging in, clicking on the Book A Party navbar item or on the button on the homepage allows the user to access the form to book a party.  This form adds a new item to the database which can be viewed by the user who added it or by admin.  Testing involved creating the basic form and using devtools to look for any errors. |
| View information about the facility | The user can view information about the facility on the homepage.  The format was tested by first adding a basic skeleton structure and styles before adding the content. |
| Change or delete bookings as a user  | Once logged in and viewing the My Bookings page, the user can edit and delete their bookings. This was tested by creating multiple bookings for a single user and then editing and deleting them.  Styles were added later and functionality was tested throughout this process. |
| Enquire about services other than parties | The user can fill out a form which will send an email to the staff email created for the project.  This was tested throughout by submitting the form multiple times with different messages to denote different tests, and checking the console in devtools for any errors.  It was tested throughout the development and styling process to ensure no changes impacted functionality. |
| View bookings as staff | A staff login was created by adding a superuser with django.  The superuser was then tested by creating some regular users and adding multiple bookings to ensure the superuser could see all bookings in the /admin page. |
| Edit and delete bookings as admin | The superuser can also edit and delete bookings, and this was tested by creating multiple bookings by multiple users and having the superuser edit and delete some of these bookings. |
| View Bookings as a user | Once logged in the user can view their bookings by clicking My Bookings in the navbar, or by being redirected after a booking.  This was tested throghout by creating multiple users to ensure they could only see bookings they had created, and styles to make the list more user friendly were added later. |


### Full Testing

Full Testing was performed on the following physical devices.

#### Devices Tested:
- Windows PC with 32” Monitor
- Samsung Galaxy zFlip 4
- Windows laptop 17”
- Apple Macbook 12"

### Functionality Tests
- All code was tested frequently at the time of writing by using devtools in the development server to check if everything was functioning as expected from writing the basic outline of the code through to testing the completed code.  Simple html messages were used to test everything was connected properly before the page structures were added in full.
- Forms were tested with basic structures before the full structure was added, with the exception of the contact form which was tested with email.

## Bugs
### Solved Bugs
| Bug | Solution |
| ---| ---|
| The contact us form was not resulting in an email to the staff inbox | After trying and failing to integrate email into django directly due to gmail security features, a third party site, [Formspree](https://formspree.io/), was used to send the contact form. This should also help future proof the site in the event of more security changes from email providers.  |
| Urls for the project were not loading | The urls for the site were resulting in path not found errors. After troubleshooting, adding the app name to the top of each app's urls.py file solved the issue. |
| The styles added with CSS were not loading | The STATIC_URL and STATIC_FILES_DIRS had not been added to settings.py correctly.  Fixing this error solved the issue. |

### Unsolved Bugs
No unsolved bugs were detected after testing.

## Validator Testing
# Update validator testing here