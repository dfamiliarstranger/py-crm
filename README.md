## INVENTORY MANAGEMENT SYSTEM WITH INVOICING FUNCTIONALIIES README

### Project Overview

This Django project is designed to manage inventory, sales, and purchases for a business. It includes functionality for CRUD operations on products, suppliers, purchases, sales, and inventory items. Additionally, it provides user authentication and authorization features to ensure secure access to the application.

### Features

1. User Authentication: Users can register, log in, and log out of the system. Authentication is enforced for accessing protected views and functionalities.

2. CRUD Operations:
   - Products: Create, read, update, and delete product details.
   - Suppliers: Manage supplier information including name, contact details, and address.
   - Purchases: Record purchases of products from suppliers, including quantity, price, and total cost.
   - Sales: Record sales transactions including quantity sold and price.
   - Inventory: View current inventory items and their quantities.

3. Form Validation: The application includes form validation to ensure that required fields are filled out correctly, and that invalid data is not submitted.

4. Dynamic Forms: Dynamic forms are used for adding purchases, allowing users to add multiple products to a purchase transaction dynamically.

5. Invoice Generation: Users can generate invoices manually through a form, which includes information about the sales transaction and relevant inventory items.

### Project Structure

The project is structured as follows:

- `accounts`: Contains views, templates, and forms related to user authentication and authorization.
- `inventory`: Manages CRUD operations for products, suppliers, and inventory items.
- `purchases`: Handles purchase-related functionalities including recording purchases and adding products to purchases.
- `sales`: Deals with sales-related functionalities, including recording sales transactions.
- `templates`**: Contains HTML templates for rendering views.
- `static`: Stores static files such as CSS, JavaScript, and images.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: Lists all Python dependencies required for the project.
- `README.md`: This file.

### Getting Started

1. Clone the Repository: Clone this repository to your local machine using `git clone`.

2. Install Dependencies: Install the required Python dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.

3. Database Setup: Configure the database settings in `settings.py`. Run migrations using `python manage.py makemigrations` followed by `python manage.py migrate` to apply migrations.

4. Create Superuser: Create a superuser account using `python manage.py createsuperuser` to access the Django admin interface.

5. Run the Development Server: Start the Django development server with `python manage.py runserver`. Access the application at `http://localhost:8000`.

6. Explore the Application: Log in with your superuser credentials to explore and interact with the application's features.

### Contributing

Contributions to this project are welcome. If you encounter any bugs, issues, or have suggestions for improvements, please open an issue or submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code for personal or commercial use.
