# Janitiri Project

A Django REST API for managing patient health data with a focus on heart-related metrics.

## Setup Instructions



### Installation Steps

1. Clone the repository
```bash
git clone https://github.com/ismailrazak/Janitri-Backend-Assignment.git
cd janitiri
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure database
```bash
python manage.py migrate
```

6. Run the development server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## Project Assumptions and Design Decisions


Data Model Design
   - Custom User model extends AbstractUser with unique email requirement
   - PatientProfile model implements a one-to-one relationship with User model
     - Each patient has a single profile with medical records
     - Profiles are deleted when the associated user is deleted (CASCADE)
   - HeartData model implements a many-to-one relationship with PatientProfile
     - Each patient can have multiple heart rate readings
     - Heart rate data includes BPM measurements and timestamps
     - Data is linked to patient profiles with CASCADE deletion

How The api works:
   - A user can register first with email username password.
   - Then the user can login by using email/username with password.
   - The user can then hit the patient endpoint and create a medical record which auto creates a patient profile.
   - now the user can access heart data endpoint and and add heart rate values which get added to the patient profile.
## API Documentation

### Authentication Endpoints

#### Register New User
- **URL**: `/api/register/`
- **Method**: `POST`

- **Data required**:
  ```json
  {
    "username": "testuser",
    "email": "testuser@gmail.com",
    "password": "testuser",
    "password1": "testuser",
  }
  ```

### Patient Endpoints

#### List/Create Patients
- **URL**: `/api/patients/`
- **Data format**:
  ```json
  {
    "medical_record": "TextField"
  }
  ```

#### Get Patient
- **URL**: `/api/patients/<id>`

### Heart Data Endpoints


- **URL**: `/api/heartdata/`
- **Data format**:
  ```json
  {
    "heart_rate": "integer",
  }
  ```

#### Get Heart Data
- **URL**: `/api/heartdata/<id>`


### Admin Interface
- **URL**: `/admin/`
- Access the Django admin interface for database management
- Requires superuser credentials
  ```json
  {
    "username/email": "admin/admin@admin.com",
  "password": "admin"
  }
  ```
### Authentication
- **URL**: `/auth/`
- Built-in DRF authentication views
- Includes login/logout functionality

