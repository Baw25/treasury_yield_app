# Treasury Yield Application

ModernFI Treasury Yield App Fullstack App

## Example


## Features
- **Visualize Treasury Yield Curves**: Displays yield data in a line chart for various terms over a selected date range.
- **Order Management**: Create new treasury orders, view historical orders, and edit existing orders. 


## Tech Stack
### Frontend
- **React**
- **Material-UI** for component styling
- **Chart.js** for visualizations

### Backend (Compatible Setup)
- **Django and Django REST Framework**
- **PostgreSQL**

## API Endpoints
The backend exposes the following API endpoints:

- Treasury Yields:
    GET /api/treasury-yields/list/: Retrieve all treasury yields.
- Orders:
    GET /api/orders/: Retrieve orders.
    POST /api/orders/create/: Create order.
    GET /api/orders/:id/: Retrieve a single order.
    PUT /api/orders/:id/: Update a single order.
    DELETE /api/orders/:id/: Delete a single order

## Dependencies
- API: requirements.txt
- Frontend: package.json
- React 
- Node.js 
- Django
- PostgreSQL

## Setup Project Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/{user}/treasury-yield-dashboard.git
    cd treasury-yield-dashboard
    ```

2. **Install React frontend dependencies**:
    Make sure you have Node.js installed. Run:
    ```bash
    npm install
    ```
3. **Start the React frontend server**:
    ```bash
    npm start
    ```
   By default, the app runs at [http://localhost:3000](http://localhost:3000).


4. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix
    ```

5. **Install the required backend packages**:
    Make sure you are in the root directory:

    ```bash
    pip install -r requirements.txt
    ```

6. **Set up the PostgreSQL database**:
    Make sure PostgreSQL is running locally. Set up local DB:

    ```bash
    psql
    CREATE DATABASE treasury_db;
    ``` 

7. **Configure the database settings**:
   Update the `DATABASES` configuration in your Django `settings.py` file:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': '<db_name>',
           'USER': '<db_user>',
           'PASSWORD': '<password>',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }

8. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9. **Start the Django dev server**:
    ```bash
    python manage.py runserver
    ```    

## Setup of TreasuryYield Table using Script
1. **Run the data scraping script**:
    ```bash
    python scrape_treasury_yields.py
    ```   
    Check if double has been populated properly in the treasury_app_treasuryyields table.