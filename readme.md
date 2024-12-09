# Project Setup and API Documentation

## Setting up the Project

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install dependencies**:

   For venv ( install uv - optional, for faster package installation):

   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

   For regular installation:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the API documentation**:
   - Navigate to `http://127.0.0.1:8000/swagger/` for interactive Swagger UI documentation.

---

## Available API Endpoints

### User Endpoints

1. **List Users**
   - **URL**: `/user/`
   - **Method**: `GET`
   - **Description**: Retrieves a list of all users.

2. **Create User**
   - **URL**: `/user/create/`
   - **Method**: `POST`
   - **Description**: Creates a new user.

3. **Update User**
   - **URL**: `/user/update/<int:pk>/`
   - **Method**: `PUT`
   - **Description**: Updates the details of a user by ID.

4. **Delete User**
   - **URL**: `/user/destroy/<int:pk>`
   - **Method**: `DELETE`
   - **Description**: Deletes a user by ID.

5. **Retrieve User**
   - **URL**: `/user/<int:pk>`
   - **Method**: `GET`
   - **Description**: Retrieves details of a specific user by ID.

### Expense Endpoints

1. **List Expenses**
   - **URL**: `/expense/`
   - **Method**: `GET`
   - **Description**: Retrieves a list of all expenses.

2. **Create Expense**
   - **URL**: `/expense/create/`
   - **Method**: `POST`
   - **Description**: Creates a new expense.

3. **Update Expense**
   - **URL**: `/expense/update/<int:pk>/`
   - **Method**: `PUT`
   - **Description**: Updates an expense by ID.

4. **Delete Expense**
   - **URL**: `/expense/destroy/<int:pk>`
   - **Method**: `DELETE`
   - **Description**: Deletes an expense by ID.

5. **Retrieve Expense**
   - **URL**: `/expense/<int:pk>`
   - **Method**: `GET`
   - **Description**: Retrieves details of a specific expense by ID.

6. **List Expenses by Date Range**
   - **URL**: `/expense/by-date-range/`
   - **Method**: `GET`
   - **Description**: Lists all expenses for a user within a specified date range.
   - **Query Parameters**:
     - `user`: User ID (required)
     - `start_date`: Start date in `YYYY-MM-DD` format (required)
     - `end_date`: End date in `YYYY-MM-DD` format (required)

7. **Expense Summary by Month**
   - **URL**: `/expense/summary/`
   - **Method**: `GET`
   - **Description**: Returns the total expenses per category for a given month.
   - **Query Parameters**:
     - `user`: User ID (required)
     - `year`: Year in `YYYY` format (required)
     - `month`: Month in `MM` format (required)

---

## Additional Notes
- Ensure that the database is properly configured in the Django settings before running migrations.
- Use `drf-yasg` for auto-generated API documentation. Install it via pip if not already installed:
  ```bash
  pip install drf-yasg
  ```
- The Swagger documentation can be accessed directly at:
  - `http://127.0.0.1:8000/swagger/`
  - `http://127.0.0.1:8000/redoc/`

Feel free to reach out if you encounter any issues during setup or usage.

