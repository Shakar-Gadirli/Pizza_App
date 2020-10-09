# Pizza Project



## Installation
* Download all the files
* Run the main.py file



## Brief Description

This simple app allows you to create account and log in to your account.As a customer, you can order pizza,view your history, get notifications about newly created pizzas and log out of your account.As an admin, you can add new pizza to pizza list,see all the information about the customers and log out of your account.Additionally, the app enables to mswitch from one page to another.

#### Login Page
In this page, you can log in to your account.If you enter incorrect password or username, there will be pop-up message that tells you 'username' or 'password' is incorrect.
#### Sign Up page
If you don't have account, you can create new account by pressing 'Create Account' button in Login page,This will redirect you to Sign Up page where you can enter username and password.If there is already an username that you want to take, there will be pop-up message that tells you "This username is already taken,try different one"

#### Admin page
To register as admin you should consider these:
* username: admin
* password: admin

This will redirect you to Admin page where you can:
##### Add new pizza
Here you can fill the blank with the name of pizza, ingredients and price, then you should press 'add new pizza' button to add newly created pizza.So, you will see a pop-up message that tells you "You added pizza".
* If you try to add pizza that is already exists you will see message "This Pizza exists"
* If you leave any field empty, you will see message: "There is empty field"
##### Customer info
here you can enter the username of any user and you can see their password and username

Finally, you can press log out button to go back to the Log in page

#### Main Menu
After logging in to your account,you will be directed to the Main Menu where you can see all the Pizzas to select.
You will see Buttons that have Pizzas' names on them,by pressing them you will be directed to Toppings page.Also,there are Pizza Order History and Log out buttons to see all the pizzas you have bought and their prices and to go back to the login page respectively.

#### Toppings Menu
There you will see titles that represent the names of the pizzas such as Chicken, Bacon,Olives,Tomato and Salsa, and below them thera two button: Add and Remove.
* Add button will add new toppings to your pizza
* Remove button will remove toppings from your pizza
After you change the pizza as you like, you can see "Buy" button.
* Buy button will redirect you to the Purchase page

#### Purchase Page
In this page you will see 4 buttons:
* Purchase: you will order pizza by just pressing on it.Then, you will be directed to the Main Menu page.Also this order will be added to your purchase history.
* Want more pizza?: you will be redirected to the Main Menu to select more pizzas
* Remove pizza?: This will remove your currently selected pizza
* Previous page: this will allow you to go back to the Toppings Page

#### Note
All the pages have Previous page button that allows you to go back to the previous page.