# Faculty Resume Web Application - Lahijan University

This is a Django-based web application designed for managing and displaying faculty resumes at the Islamic Azad University, Lahijan Branch. The application includes a homepage listing all professors, individual resume pages for each professor, and an admin dashboard for the university dean to manage resumes (create, edit, delete). Resumes can include textual information, profile photos, and PDF files. The interface and content are entirely in Persian.

## Features

- **Homepage**: Displays a list of professors with links to their individual resume pages.
- **Resume Page**: Shows detailed resume information for each professor at the URL `/resume/id/<uuid>`.
- **Admin Dashboard**: Restricted to the university dean (admin) for full resume management (create, edit, delete).
- **File Uploads**: Supports uploading profile photos and PDF resume files.
- **Language**: Entirely in Persian (Farsi) for both interface and content.
- **Unique IDs**: Automatically generates UUIDs for each professor.

## Prerequisites

To run this project on your local machine, ensure you have the following installed:

- **Python**: Version 3.8 or higher ([Download Python](https://www.python.org/downloads/))
- **pip**: Python package manager (included with Python)
- **Git**: For cloning the repository (optional, [Download Git](https://git-scm.com/downloads))
- **A code editor**: Such as VS Code, PyCharm, or any text editor ([VS Code](https://code.visualstudio.com/))

## Step-by-Step Setup Instructions

Follow these steps carefully to set up and run the project on your local machine. Each step is explained for beginners.

### Step 1: Clone the Repository

1. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux).
2. Navigate to the directory where you want to store the project:
  
  ```bash
  cd path/to/your/folder
  ```
  
3. Clone the project repository from GitHub:
  
  ```bash
  git clone https://github.com/0xaRY4/lahijan_uni.git
  ```
  
  *Note: Replace `yourusername` with the actual GitHub username hosting the repository.*
4. Move into the project directory:
  
  ```bash
  cd lahijan_uni
  ```
  

*If you don’t have Git installed, you can download the project as a ZIP file from GitHub and extract it to your desired folder.*

### Step 2: Set Up a Virtual Environment

A virtual environment isolates project dependencies to avoid conflicts with other Python projects.

1. Create a virtual environment:
  
  ```bash
  python -m venv venv
  ```
  
  This creates a folder named `venv` in your project directory.
2. Activate the virtual environment:
  - **Windows**:
    
    ```bash
    venv\Scripts\activate
    ```
    
  - **macOS/Linux**:
    
    ```bash
    source venv/bin/activate
    ```
    
    You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

### Step 3: Install Dependencies

The project requires Django and Pillow (for image processing). Install them within the virtual environment.

1. Run the following command:
  
  ```bash
  pip install django pillow
  ```
  
2. Verify the installation:
  
  ```bash
  pip list
  ```
  
  You should see `django` and `pillow` listed.

### Step 4: Configure the Database

The project uses SQLite, a lightweight database included with Django.

1. Apply database migrations to set up the database schema:
  
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
  
  This creates a `db.sqlite3` file in the `lahijan_uni` directory.

### Step 5: Create an Admin User

You need an admin user to access the dashboard and manage resumes.

1. Run the following command:
  
  ```bash
  python manage.py createsuperuser
  ```
  
2. Follow the prompts to enter:
  - **Username**: e.g., `admin`
  - **Email**: Can be left blank (press Enter)
  - **Password**: Choose a secure password (not visible when typing)
3. Confirm the password by retyping it.

### Step 6: Create Media Folders

The project stores uploaded profile photos and PDF resumes in the `media` directory.

1. Create the required folders:
  
  ```bash
  mkdir -p media/profiles media/resumes
  ```
  
  This creates `media`, `media/profiles`, and `media/resumes` directories in the project root.

### Step 7: Run the Development Server

Start the Django development server to test the application.

1. Run the server:
  
  ```bash
  python manage.py runserver
  ```
  
2. Open a web browser and go to:
  
  ```
  http://127.0.0.1:8000
  ```
  
  You should see the homepage listing professors (initially empty).

### Step 8: Test the Application

Explore the application to ensure it works as expected.

- **Homepage**: Visit `http://127.0.0.1:8000` to see the list of professors.
- **Resume Page**: Click a professor’s name (after adding one) to view their resume at `/resume/id/<uuid>`.
- **Admin Login**: Go to `http://127.0.0.1:8000/accounts/login/` and log in with the admin credentials created in Step 5.
- **Dashboard**: After logging in, visit `http://127.0.0.1:8000/dashboard/` to manage resumes (create, edit, delete).
- **Add a Resume**:
  1. In the dashboard, click "ایجاد رزومه جدید" (Create New Resume).
  2. Fill in the form (e.g., name, degree, experience) and optionally upload a photo or PDF.
  3. Save and verify the resume appears on the homepage and dashboard.

## Project Structure

Here’s an overview of the project’s key directories and files:

- `lahijan_uni/`:
  - `settings.py`: Project configuration (database, apps, media settings).
  - `urls.py`: Main URL routing.
- `faculty/`:
  - `models.py`: Defines the `Professor` model for storing resume data.
  - `views.py`: Handles page rendering and logic.
  - `forms.py`: Form for creating/editing resumes.
  - `urls.py`: App-specific URL routing.
- `templates/`:
  - `base.html`: Base template for all pages.
  - `home.html`: Homepage template.
  - `resume_detail.html`: Individual resume template.
  - `dashboard.html`: Admin dashboard template.
  - Other templates for forms and login.
- `media/`:
  - `profiles/`: Stores profile photos.
  - `resumes/`: Stores PDF resume files.
- `db.sqlite3`: SQLite database file.

## Troubleshooting

If you encounter issues, try these steps:

- **Error: “pip not found”**:
  - Ensure Python is installed and added to your system’s PATH.
  - Run `python -m ensurepip --upgrade` and `python -m pip install --upgrade pip`.
- **Error: “ModuleNotFoundError: No module named ‘django’”**:
  - Verify the virtual environment is active (`(venv)` in terminal).
  - Reinstall dependencies: `pip install django pillow`.
- **Error: Media files not loading**:
  - Ensure `media/profiles` and `media/resumes` folders exist.
  - Check `MEDIA_ROOT` and `MEDIA_URL` in `settings.py`.
- **Error: “Page not found” or “500 Server Error”**:
  - Run the server with `DEBUG = True` in `settings.py` to see detailed errors.
  - Ensure migrations are applied: `python manage.py migrate`.
- **General Issues**:
  - Check the terminal output for error messages.
  - Consult the [Django Documentation](https://docs.djangoproject.com/) or ask for help in communities like Stack Overflow.

## Security Notes

- **Local Development**: The project is set up for local use with `DEBUG = True`. For production, set `DEBUG = False` and secure the `SECRET_KEY` in `settings.py`.
- **Admin Credentials**: Keep the admin username and password secure.

## Future Improvements

- **Styling**: Add CSS or a framework like Bootstrap for a better user interface.
- **Search/Filter**: Implement search or filter functionality for the professor list.
- **Database**: Switch to PostgreSQL for production environments.
- **Authentication**: Add multi-user support or role-based access.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make changes and commit: `git commit -m "Add feature"`.
4. Push to your fork: `git push origin feature-name`.
5. Create a Pull Request on GitHub.

Report bugs or suggest features in the [Issues](https://github.com/yourusername/lahijan_uni/issues) section.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details (if included).

---

*Islamic Azad University, Lahijan Branch - Undergraduate Project*
