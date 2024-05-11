# CURETRY - Online Medical Store
CURETRY is an Online Medical Store application built using Tkinter module in Python. It allows users to order medicines online, with a MySQL database used for storing data.

## Setup Instructions
   `Run sql_code.py`: Execute sql_code.py once to create the medicines database and the databases for storing customer details.

## Features
### User Interface (Curetry.py)
   - `User Authentication`: Users are prompted to login or signup if it's their first time.
   - `Medicine Catalog`: Users can view the list of medicines (static) with a search feature.
   - `Shopping Cart`: Users can select the quantity of medicines and add them to the cart.
   - `Preview Bill`: Users can preview the bill with the total amount for the cart items.
   - `Order Placement`: Users can enter delivery address and contact information to place the order.
   - `Bill Generation`: Upon successful order placement, a bill is generated using the fpdf library.

### Admin Interface (ProjectCuretryAdmin.py)
   - `Admin Authentication`: Admins are prompted to login.
   - `Stock Management`: Admins can view existing medicines, update their quantity, and add new medicines to the database.

## Usage
    Clone this repository or download the project files.
    Run sql_code.py to initialize the database.
    Execute Curetry.py for the user interface or ProjectCuretryAdmin.py for the admin interface.


