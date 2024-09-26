
# **LittleLemon DjangoApp**

**LittleLemon DjangoApp** is a web application built using the Django framework to manage the menu and reservations for the fictional **Little Lemon** restaurant. It provides an intuitive interface for both managing the restaurant's offerings and booking table reservations.

## **Key Features**:

- **Menu Management**:  
  - Users can *add*, *edit*, and *delete* menu items.
  - Each menu item includes details such as the dish name, description, price, and availability.
  
- **Reservation Booking**:  
  - Customers can book a table by providing their details, reservation date, and time.
  - Admins can view, approve, or cancel bookings via the admin panel.

- **Authentication System**: Manage users with roles for admins and customers.
- **REST API with Django REST Framework**:  
  - Endpoints to manage menu items and reservations via HTTP requests.

- **JWT Security**: User authentication is handled through **JSON Web Tokens (JWT)** for secure access.
- **Filtering and Pagination**: *Filter* and *paginate* menu items and reservations for a better user experience.
- **Interactive Templates**: Integration of **JavaScript** into Django templates for dynamic interactions.

## **Models**:

1. **Menu**: Represents the restaurant's menu, allowing admins to add new dishes and update or remove existing items.
2. **Booking**: Enables customers to book reservations by providing necessary booking details.

## **Technologies Used**:

- **Backend**: `Django`, `Django REST Framework (DRF)`
- **Database**: `MySql`
- **Frontend**: `Django templates` with integrated JavaScript for interactivity
- **Authentication**: `JWT (JSON Web Token)`

## **Installation and Setup**:

1. Fork the repository:
   
2. Navigate to the project directory:
   ```bash
   cd LittleLemon-DjangoApp
   ```
3. Activate The venv:
   ```bash
   ProjectScope/sripts/activate
   ```
4. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

> **Note**: Ensure you have Python and Django installed before running the application.

## **Author**:

This project is developed by [**Hamza**](https://github.com/Userphenixe).
