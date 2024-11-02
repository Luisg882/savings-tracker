# YourSavings

YourSavings is a Django-based website where users can open an account and link it to their personal bank accounts. They can transfer money from their bank accounts to the main balance, open new savings pots, transfer funds from the main balance to the savings pots, and close them, sending the funds back to their personal bank accounts once they achieve their savings goals.

For project purposes, the functionality for adding and taking funds from nominated accounts is not included. The project is designed to manage the internal funds data on the website. These movements are mentioned hypothetically throughout the project.

![resposive image phone](/static/images/responsive-phone.png)

![resposive image table](/static/images/responsive-tablet.png)

![resposive image laptop](/static/images/responsive-laptopn.png)

![resposive image desktop](/static/images/responsive-desktop.png)

## Features

- **Navigation**
  - On top of every page, it shows the logo and title of the website followed by the navigation options.
  - The Home option will take the user to the main index.html. If they are already logged in, it will take them back to their profile page.
  - Register will take them to the Sign-Up page where they can register themselves. If the customer is already logged in, it will disappear.
  - For phones, the navigation options will be wrapped in a menu button. When clicked, it will display all the navigation options.
  - Log in will take the user to the login site.
  - If they are login it will change to sign out.

  ![navigation bar](/static/images/navbar.png)

- **Home**
  - Introduction: text description of the website and what the users can expect from the website.
  - Sign up button to go directly to the sign-up page allowing the user to open an account.
  - Login button for already registered users to log in.

  ![introduction section showing about sign up and login](/static/images/home.png)

- **Register**
  - Shows the Sign-Up form to populate the profile model (username, email, nominated bank account, main balance).
  - Password validation asks for at least 8 characters.
  - Email validation checks for the correct email structure.
  - Nominated bank account only allows 8 numbers.
  - The main balance will allow up to 10 digits.

  ![Sign up form](/static/images/sign-up.png)
  ![last part of the sign up form](/static/images/sing-up-end.png)
  
- **Log in**
  - Allows the user to log into their profiles.
  - Remember me option to prepopulate the user password and username.

  ![log in section](/static/images/login.png)

- **Sign Out**
  - Allows the user to log out of their profile.

  ![sign out](/static/images/sign-out.png)

- **Profile**
  - Shows the current balance that the user has.
  - Add money redirects the user to the Move Money page.
  - Open a new pot allows the user to create new pots.
  - Your Saving pots display the pots the user has. If there are more than 3, it will paginate the pots by 3.

  ![profile page](/static/images/profile.png)

- **Move Money**
  - The user adds funds from their bank account to the main balance.
  - Back to profile button to go back to the profile.
  - Successful message will tell the user if it was successful and link to go back to the profile page.

  ![Move money page](/static/images/move-money.png)

- **Open new pot**
  - Allows the user to create a new pot.
  - User can name the pot.
  - Successful message will tell the user if it was successful and link to go back to the profile page.

  ![open new pot page](/static/images/open-new-pot.png) 

- **Saving pot details**
  - Shows the amount the user has in the pot.
  - Has the option to add funds from the main balance to the pot.
  - Close the pot option will direct the user to close the pot. Main balance before adding funds to a pot.

  Main balance before transferring funds to pot.

  ![main balance before adding funds to saving pot](/static/images/main-balance-before-add-money-to-saving-pot.png)

  Adding funds to the pot.

  ![saving pot adding the funds](/static/images/adding-funds-to-saving-pot.png)

  Main balance after adding funds to saving pot.

  ![main balance after adding funds to pot](/static/images/balance-after-adding-funds.png)

  Pot balance after adding funds.

  ![saving pot balance after adding funds](/static/images/saving-pot-after-adding-funds.png)

- **Change pot name**
  - User can change the name of the current pot.
  - Successful message will tell the user if it was successful and link to go back to the profile page.

  ![image of the change pot name with successful message](/static/images/change-pot-name.png)

- **Closing pot**
  - Allows the user to close the account and send the funds to their bank account.
  - If the account has funds, it will say that the funds will go to the bank account.
  - If there are no funds in the account, it will say your pot is empty and will be closed.
  
  ![closing pot with funds in page](/static/images/closing-saving-pot.png)
  ![closing pot without funds](/static/images/closing-saving-pot-no-funds.png)

## Features left to implement
  - Add functionality to request and send funds from bank accounts.
  - Add a function to automatically distribute the funds added from the main balance to the savings pots in different percentages.

## Technologies Used
  **Languages Used**
  - HTML5
  - CSS3
  - JavaScript
  - Python

  **Libraries and Programs Used**
   - **Django** - Used to link and control the front-end and back-end interface.
   - **Crispy Forms** - Used to display the forms in the HTML pages.
   - **Allauth** - Used to control the authentication of the users.
   - **Bootstrap 5** - Used to style the HTML pages.
   - **Gunicorn** - To support the usage of the site on Heroku.
   - **Psycopg2** - To allow the Django project to interact with the database.
   - **Grammarly** - Used to correct misspellings and grammar mistakes.
   - **Font Awesome** - To get social media icons.
   - **Google Fonts** - Oswald and Raleway fonts were used on the website.
   - **Invision** - To make early sketches of the website.
   - **Git** - Used as IDE to control and track the project's progression.
   - **Python Tutor** - Used to check the errors, and understand and correct the functions.

## Testing
  - Tested in Google Chrome, Firefox, and Edge browsers.
  - Website is responsive in all browsers.
  - All Social Media icons open in a new tab.
  - Navbar links take the user to the right location.
  - Login successfully accesses the user profile.
  - Sign out takes you back to the home page.
  - Sign up form checks and validates the right information given.

**Functional Testing**
  - **Profile**
    - Add money button takes you to the move-money.html.
    - Open new Pot takes you to the open pot page.
    - View Details in each saving pot takes you to the saving pot itself.

  - **Add money**
    - Only allows integer numbers.
    - The Send button shows the Transfer completed message and the Go to Profile link takes you back to the profile page.
    - Back to profile button takes you back to the profile page.

    ![image of the main balance before adding funds](/static/images/balance-before-adding-funds-from-bank-account.png)

    ![image adding funds to the main balance](/static/images/adding-funds-to-main-balance.png)

    ![image of the main balance after adding funds](/static/images/main-balance-after-adding-funds.png)

  - **Open new Pot**
    - Create button shows New Pot created message and the go to profile link takes you to the profile page showing the new pot.
    - Back to profile button takes you back to the profile page.
  
    ![image of the creation of Car pot](/static/images/create-new-pot.png)

    ![image of the profile with the new pot](/static/images/profile-with-new-pot.png)

  - **Saving details**
    - Add money shows the Transfer completed and updates the balance of the account.
    - If the user add more funds that they have in the main balance a failed message will appear
    - Change pot name takes you to the change pot name page.
    - Close pot will take the user to the close pot page.
    - Back to profile button takes you back to the profile page.

    ![image of the main balance before adding the funds in the saving pot](/static/images/profile-with-new-pot.png)

    ![image of saving pot after adding the funds](/static/images/adding-funds-to-saving-pot-test.png)

    ![image of main balance after adding funds in the saving pot](/static/images/main-balance-after-adding-funds-to-saving-pot.png)

  - **Change pot name**
    - Name changed message appears after changing the name and the Go to Profile link takes you back to the profile page. The Cancel button will take the user back to the saving pot details.

    ![image of pot before changing the name of the pot](/static/images/adding-funds-to-saving-pot.png)

    ![image of the new name of the pot](/static/images/test-change-pot-name.png)

    ![image of profile with pot with new name](/static/images/profile-with-changed-pot-name.png)

    ![image of transfer failed message](/static/images/failed-transfer-message.png)

  - **Close saving pot**
    - Close pot will take the user to the close pot page.
    - After clicking "Yes, Close Pot" button, it will show the message "Are you sure you want to close this pot? The funds will be transferred to your bank account." if the user has funds in it. If the user has no funds, this message will show "The saving pot is empty and will be closed." Two buttons "Yes, Close Pot" and "Cancel" will appear. If "Cancel" is clicked, it will take the user back to the saving pot details. If "Yes, Close Pot" is clicked, a new section will appear with the message "Are you sure you want to close this pot? The saving pot is empty and will be closed." in case that the user has no funds, or "Are you sure you want to close this pot? The funds will be transferred to your bank account." if the user has funds. Two new buttons, "Yes, Close Pot" and "Cancel", will appear. If "Yes, Close Pot" is clicked, the user will be redirected to the profile page. If "Cancel" is clicked, it will hide this new section. 

    ![closing pot with funds in page](/static/images/closing-saving-pot.png)

    ![closing pot after clicking first "Yes, Close Pot"](/static/images/closing-saving-pot-after-clicking-first-option.png)


## Bugs
**Solved Bugs**
 - To check the saving details, I didn't add a slug field in the SavingPot model, so I couldn't search for the slug pattern to get the specific saving pot. To solve this, I added pot_id as a second argument of the saving_pot_details_view, allowing it to be added as a .get method to track and retrieve each saving in the variable saving_pot = profile.saving_pots.get(id=pot_id).

 ![saving pot details code](/static/images/saving-pot-details-bug.png)

 - The nominated bank account field of the sign-up form was allowing any kind of characters and symbols. I changed the nominated_bank_account field from CharField to DecimalField, allowing only 8 numbers and no decimals in the Profile model. I also removed slug and age fields since they were not used.

 Profile model before changes 

 ![Profile code before changes](/static/images/profile-model-before-changes.png)

 Profile model after changes

 ![Profile code after changes](/static/images/profile-model-after-changes.png)

 - When making changes to any of the models, the messages didn't display on the screen, and the user was redirected to the profile page after any changes. By adding a for loop in the HTML pages and the reverse method, it was possible to add a link to return to the profile page and display the success message. This process was repeated in the different views.

 View without reverse link

 ![image of view without reverse link](/static/images/view-without-reverse.png)

 View with reverse link

 ![image of view with reverse](/static/images/view-with-reverse.png)

**Unsolved Bugs**
  - Wanted to change the name of the Profile model to Account since it was more logical for the project, but errors retrieving the information from the database occurred because previous users had already created profiles. Attempted to erase the profiles and users to eliminate any trace of the profile model, but the error persisted, so it was decided to keep the Profile name.

  - Wanted to delete the age and slug fields from the Profile model since they weren't being used. Attempted to make the previous solution by erasing previous profiles that contained slug and age as part of the field, but the error persisted.

  - Wen the user login for the first time and goes to any of the sections that display a successful message will display a successfully signed in or signed out or bout. 

  ![image of the successful message bug](/static/images/successful-message-bug.png)


**Validator testing**
  - CSS
    - No errors were found in W3C (Jigsaw) validator
  - Python
    - No errors were found in pep8 linter
  - Java Script
    - ESLint was used and no errors were found.
  - Accessibility
    - Lighthouse test in index.html.

    ![image of the lighthouse result of the index.html](/static/images/lighthouse-index.png)

    - Lighthouse test in login.

    ![image of the lighthouse result of the login](/static/images/lighthouse-login.png)

    - Lighthouse test in sign up.

    ![image of the lighthouse result of the sign up](/static/images/lighthouse-signup.png)

    - Lighthouse test in log out.

    ![image of the lighthouse result of the log out](/static/images/lighthouse-logout.png)

    - Lighthouse test in Profile.

    ![image of the lighthouse result of the Profile](/static/images/lighthouse-profile.png)

    - Lighthouse test in Move Money.

    ![image of the lighthouse result of the Move Money](/static/images/lighthouse-move-money.png)

    - Lighthouse test in Open new pot.

    ![image of the lighthouse result of the Open new pot](/static/images/lighthouse-open-new-pot.png)

    - Lighthouse test in Close saving pot.

    ![image of the lighthouse result of the Close saving pot](/static/images/lighthouse-closing-pot.png)

    - Lighthouse test in Change saving pot name.

    ![image of the lighthouse result of the Change saving pot name](/static/images/lighthouse-change-name-pot.png)

    - Lighthouse test in Saving pot details.

    ![image of the lighthouse result of the Saving pot details](/static/images/lighthouse-saving-pot-details.png)


## Deployment
  This project was deployed in Heroku.
   - Create Procfile file and add web: gunicorn your_savings.wsgi to start the server
   - Turn debug to False.
   - Add heroku.com to the ALLOWED_HOSTS list.
   - Add config Vars DISABLE_COLLECTSTATIC with a value of 1 to prevent Heroku from uploading static files, add DATABASE_URL with the value of the database destination.
   - create requirements.txt to list all the used packages in the project so Heroku is aware of them.
   - Fork savings-traker from Git Hub.
   - Create a new Heroku app.
   - Change the dyno to Eco Dyno
   - Link the app to the Git Hub repository. 
   - Set the Deployment as automatic.
   - Deploy the program.