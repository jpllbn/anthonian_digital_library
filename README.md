# Anthonian Digital Library

## Overview
The Anthonian Digital Library is a cloud-enabled library management system designed for St. Anthony's College. It provides a centralized platform for students, faculty, and administrators to access resources, manage borrowings, and track clearances efficiently.

## Features
- **Role-Based Access**: Tailored interfaces for students, faculty, and administrators.
- **Digital Library Access**: Seamless access to physical and digital resources from anywhere, anytime.
- **Automated Clearance**: Streamlined clearance process with real-time status tracking.
- **Secure System**: Enterprise-grade security with AES-256 encryption.

## Project Structure

The project is divided into two main components:

### Backend
The backend is built using Python and includes the following files:
- `auth.py`: Handles authentication and authorization.
- `crud.py`: Contains CRUD operations for database interactions.
- `database.py`: Manages database connections.
- `models.py`: Defines database models.
- `schemas.py`: Defines data validation schemas.
- `main.py`: Entry point for the backend server.

### Frontend
The frontend is built using HTML, CSS, and JavaScript. It includes the following directories:
- `html/`: Contains HTML files for different user roles (admin, faculty, student).
- `css/`: Contains stylesheets for the application.
- `js/`: Contains JavaScript files for interactivity.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/anthonian_digital_library.git
   ```
2. Navigate to the backend directory and install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Start the backend server:
   ```bash
   python main.py
   ```
4. Open the `index.html` file in the `frontend` directory to view the application.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

