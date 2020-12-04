
# WFPB RECIPES

This project promotes the WFPB diet. The website can be used by users who are already following this lifestyle and the beginners alike.
The website enables the user to create their own recipe collection, share their recipes with others, and find an inspiration by trying recipes posted by other users.


## UX

The project was designed to allow users to create their own online recipe book, avoid endless online search for a particular recipe, share their recipes with other users

and be able to easily find new recipes that suit their lifestyle.

In case a user wants to look for a specific kind of recipes, there is a search field on the home page, that find recipes based on category, cuisine or a recipe name.

Through CRUD functionality, the project enables the user to create, read, edit and delete their own recipes.

The register / login option serves as an additional data protection and ensures that only the user can edit or delete their own recipes.


#### User Stories

As a user, I want:

- to have all of my recipes in the same place
- to be able to add a new recipe to my already existing collection
- to be able to manage my own recipe collection, by being able to edit or delete recipes
- to make sure that no one else can change or delete my own recipes
- to be able to share my recipes with my friends and/ or people who follow the same lifestyle
- to be able to easily find recipes from a certain country
- to be able to see only recipes from a certain category, e.g. desserts



#### Wireframes

As there are many pages to this project, I have included the wireframes in a separate document.

Please see the wireframes.md file for the entire collection of wireframes:

https://github.com/AMikic33/milestone_project_3/tree/master/static/wireframes



## Features

#### Existing Features

- Register - the user is able to create their own account and choose a password
- Login - the user is able to login with their own password, thus providing more protection to their own recipe collection
- User Profile - each user has their own profile where they have an overview of their own recipes
- Homepage - allows users to see the recipes created by other users
- Search function - allows users to look for a certain recipe by name (by typing in full or a part of the recipe name), 
                    by category (appetizer, main course, dessert) or by cuisine (e.g. italian, french, mexican, etc.)
- Add recipe - allows users to add a new recipe with all the details and  recipe photo included
- Edit recipe - allows users to edit their own recipes 
- Delete recipe - allows users to delete their own recipes
- Logout - Users can log out of the website at any time by clicking on the logout button on any page in the nav bar
- Mobile side nav - makes a better overview and avoids mistakes due to too small nav buttons when in mobile view

#### Features left to implement

- Pagination - if there is a lot of recipes on the home page or user profile, pagination would be a better option than scrolling through
- Favourites - create an option where user can save their favourite recipes and see them all on one page
- Video - the user would be able to upload a video of the recipe as well
- Social profiles - users would be able to add personal informations about themselves, share their profiles and follow another users
- Delete option - a second confirmation would be needed before the recipe's being deleted



## Technologies Used

- HTML
- CSS
- Materialize
- Google fonts
- JavaScript
- Python
- Flask
- PyMongo
- MongoDB
- Heroku
- Balsamiq

## Testing

The following manual testing was done to ensure that the website had no bugs or layout issues and that all links and features worked correctly.

#### Individual Page Testing

###### Registration page

- registering by inputing username and password
- clicking on submit button to make sure the new account has been successfully created and flash message "Your profile is created!" is appearing
- back to registration - clicking on login button on the bottom to make sure it redirects to login page

###### Log In page

- inputing existing username and password and clicking on submit button to make sure it directs user to their profile with welcome "username" appearing
- back to login - clicking on registration button on the bottom to make sure it redirects to registration page


###### User Profile page

- click on "Recipes" in navbar to verify that it brings the user to the home page
- click on "Home" in navbar to verify that it brings the user to the home page
- click on "Add Recipe" in navbar to verify that it brings the user to add new recipe page
- click on one "here" link in the intro text to to verify that it brings the user to the home page
- click on one of the recipe links to verify that it brings the user to single recipe page
- click on "Log Out" in navbar to verify that it brings the user back to Login page with flash message "Logout successful" appearing


###### Home Page

- click on "Add Recipe" in navbar to verify that it brings the user to add new recipe page
- click on "Profile" in navbar to verify that it brings the user to their profile page
- inputing existing recipe name in the search field and clicking "Search" to verify it shows all recipes with that word
- inputing existing recipe category in the search field and clicking "Search" to verify it shows all recipes with that category
- inputing existing recipe cuisine in the search field and clicking "Search" to verify it shows all recipes with that cuisine
- while only searched recipes appearing, clicking on reset button to verify it brings the user back to the home page
- inputing a word that is not in the page (Github) in the search field and clicking "Search" to verify that the flash message "No results for this search" is appearing
- while flash message "No results for this search" is on the screen, clicking on reset button to verify it brings the user back to the home page
- click on "Go to recipe" in one of the cards to verify it brings the user to the chosen recipe page
- click on a recipe created by another user to verify the buttons "Edit recipe" and "Delete Recipe" are not appearing
- click on a recipe created by user to verify the buttons "Edit recipe" and "Delete Recipe" are appearing
- click on "Log Out" in navbar to verify that it brings the user back to Login page with flash message "Logout successful" appearing


###### Single recipe page

- click on "Recipes" in navbar to verify that it brings the user to the home page
- click on "Home" in navbar to verify that it brings the user to the home page
- click on "Add Recipe" in navbar to verify that it brings the user to add new recipe page
- click on "Profile" in navbar to verify that it brings the user to their profile page
- click on "Edit recipe" to verify it enables the user to edit their recipe
- click on "Delete recipe" to verify it enables the user to delete their recipe with flash message "Recipe deleted" appearing
- click on "Log Out" in navbar to verify that it brings the user back to Login page with flash message "Logout successful" appearing


###### Edit recipe page

- click on "Recipes" in navbar to verify that it brings the user to the home page
- click on "Home" in navbar to verify that it brings the user to the home page
- click on "Add Recipe" in navbar to verify that it brings the user to add new recipe page
- click on "Profile" in navbar to verify that it brings the user to their profile page
- checking are all previous inputs appearing
- changing some of the inputs and clicking on "Edit recipe" button to verify the input has been changed
- click on "cancel" button to verify that it brings the user back to home page
- click on "Log Out" in navbar to verify that it brings the user back to Login page with flash message "Logout successful" appearing


###### Add recipe page

- click on "Recipes" in navbar to verify that it brings the user to the home page
- click on "Home" in navbar to verify that it brings the user to the home page
- click on "Profile" in navbar to verify that it brings the user to their profile page
- inputing all input text fields to verify they're working properly
- leaving one of the required fields empty to verify the error message "Please fill out this field" under the that field is appearing
- click on dropdowns to verify the user can see the options offered
- choosing some of the offered option for "Select Category", "Cooking time" and "Servings" to verify the user can choose any of the given option 
- click on submit recipe to verify the recipe has been created and that it brings user back to the home page with flash message "Recipe created" appearing
- checking does the default photo uploads if the user hasn't uploaded any photo of theirs
- click on "Log Out" in navbar to verify that it brings the user back to Login page with flash message "Logout successful" appearing


#### Responsivnes

The website has been designed to scale correctly to different screen sizes, which results you can see below. 

In order to ensure that the navigation bar was as responsive as possible, on Desktop the menu shows accross the top of the page while on mobile screens, 
the menu reduced to a burger icon with only the title visible. When the burger icon is clicked, a side menu appears with the links to other pages from the nav bar. 

To ensure that the view was user-friendly, the layout slightly changes depending on the size of the screen.

view site on "Galaxy S5" sizeand verify that there are no viewing issues
view site on "iPhone 5/SE" size and verify that there are no viewing issues
view site on "iPhone 6/7/8" size and verify that there are no viewing issues
view site on "iPhone 6/7/8 Plus" size and verify that there are no viewing issues
view site on "iPhone X" size and verify that there are no viewing issues
view site on "iPad" sizeand verify that there are no viewing issues
view site on "iPad Pro" sizeand verify that there are no viewing issues
view site on "desktop" and verify that there are no viewing issues

The website scales correctly on all screen sizes.



## Deployment

This project was deployed to Heroku at the address https://milestone-project-3-ana.herokuapp.com/ using the following steps:

##### Github

- create a new project on GitHub
- in the terminal, type "git add ." to add all new changes to the code to staging area
- type "git status" to see which files are ready to be commited
- commit these by typing "git commit -m" and adding a detailed description of the commit in ""
- push the code commit to github by typing "git push"

##### Heroku

- Create a Heroku account
- Create a new app
- Link the Heroku app with your Github repository
- Push changes to git using the terminal and verify that the connection to Heroku is working
- Add environment variables to Heroku settings.

## Credits

#### Content

- text on the home page: https://www.purewow.com/food/wfpb-recipes


#### Acknowledgements

- I would like to acknowledge my mentor Reuben Ferrante, for all the help and support on this project.
- I would like to thank the tutors for all of their help and support.
- I would also like to thank my friends and family for all of their support.