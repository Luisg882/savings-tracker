# YourSavings

YourSavings is a Django based website were the user can open an account and link it to his personal bank account so they can send money from it to the main balance, open new saving pots, transfer the funds from the main balance to the saving pots and then close them sending the funds to their personal bank account once they achieve their saving goal.

## Features

- **Navigation**
  - On top of every page, it shows logo and title of the website follow by the navigation options.
  - The Home option will take the user to the main index.html. if they are already log in will take them back to heir profile page.
  - Register will take them to the Sign Up page were they can register themselves. If the customer is already log in it will desapeard
  - For phones the navigation options will be wrapped in a menu button> When clicked will display all the navigation options.

  ![navigation bar](/static/images/navbar.png)

- **Home**
  - Introduction: text description of the website and what the users are going to spect from the website
  - Sign up button to go directly to the sign up allowing the user to open the account
  - Login button for the already registered user login

  ![introduction section showing bout sign up and login](/static/images/home.png)

- **Register**
  - Shows the Sign up form to populate the profile model (username, email, nominated bank account, main balance, username)
  - Password validation asks for at least 8 characters
  - Email validation checking that uses the right email structure
  - Nominated bank account only allows 8 numbers 

  ![Sign up form](/static/images/sign-up.png)
  ![last part of the sign up form](/static/images/sing-up-end.png)
  
- **Log in**
  - Allows the user to log into their profiles
  - Remember me option to prepopulate the user password and username

  ![log in section](/static/images/login.png)

- **Sign Out**
  - Allow the user log out of his profile

  ![sign out](/static/images/sign-out.png)

- **Profile**
  - Will show the current balance that the user has 
  - Add money will redirect the user to the Move Money site
  - Open a new pot will allow the user to create new pots
  - Your Saving pots will display the pots the user has. If there is more than 3 it will paginate the pots by 3.

  ![profile page](/static/images/profile.png)

- **Move Money**
  - The user adds funds from their bank account to the main balance
  - Back to profile button to go back to the profile 

  ![Move money page](/static/images/move-money.png)

- **Open new pot**
  - Will allow the user to create a new pot
  - User can name the pot

  ![open new pot page](/static/images/open-new-pot.png) 

- **Saving pot details**
  - Will show the amount the user have it the pot
  - Have the option to add funds from the main balance to the pod
  - Close the pot option will direct the user to the close pot pageMain balance before adding funds to a pot
  ![main balance befro tadding funds to saving pot](/static/images/main-balance-before-add-money-to-saving-pot.png)

  Adding fund to the pot
  ![saving pot adding the funds](/static/images/adding-funds-to-saving-pot.png)