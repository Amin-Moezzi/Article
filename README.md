# Article
#### Video Demo:  <URL HERE>
#### Description:

## Django Article Project
This is a Django-based web application called Articles that allows users to create,
edit, update, and delete articles. Users can also view  all of articles created by
others, with authentication mechanisms for managing their own content.

### Features

- User authentication (sign up, log in, log out)
- CRUD operations for articles (Create, Read, Update, Delete)
- Beautiful, responsive UI with Bootstrap 5
- Easy-to-use article management interface
- Articles can be created, edited, and deleted by authenticated users
### Technologies Used

- **Backend:** Django (Python web framework)
- **Frontend:** HTML, Bootstrap 5, crispy-bootstrap5
- **Database:** SQLite (default for Django)
- **Authentication:** Django's built-in user authentication system

  
### Clone the Repository

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/Amin-Moezzi/Article.git
   cd Article

## Installation

### Prerequisites
- Python 3.x


### requirements.txt
- asgiref
- crispy-bootstrap5
- Django
- django-crispy-forms
- pytz
- sqlparse
- tzdata
  
### installing  Dependencies & requirements 
```
cmd
pip install –r requirements.txt
```

#### Django
The foundation of your project, providing the web framework for development.
#### asgiref
Enables asynchronous support in Django, which is important for handling real-time
 interactions and background tasks.

#### pytz & tzdata
Allow your project to handle and manipulate timezones accurately.
#### sqlparse 
Assists Django in handling raw SQL queries by providing tools for parsing and
 formatting them
#### crispy-bootstrap5 & django-crispy-forms
   Work together to simplify and enhance the rendering of forms in a visually
   appealing way, particularly using Bootstrap 5 styling.

# Set Up Virtual Environment
   I create  a Virtual Environment for my project to isolate dependencies
   of my project, it allows me to manage and install Python packages separately
   from the system-wide Python installation. This is especially useful for managing
   dependencies for different projects without conflicts.

``` code
cmd
pip install virtualenv

python3 -m venv venv
```
### Activating the Virtual Environment On Windows
``` cmd
`venv\Scripts\activate`
```
Once activated, the virtual environment's name appears in the terminal prompt.

To deactivate and return to the global Python environment:
```
deactivate
```

### Set Up Database
Run migrations to set up the database:
```cmd 
python manage.py migrate
```

### Run the Development Server
Run the server to start the application:
```
cmd
python manage.py runserver
```
Navigate to http://127.0.0.1:8000/ in your browser to view the application.

### Screenshots
![Screenshot 2024-12-25 150144](https://github.com/user-attachments/assets/04b444c5-43a9-4bd1-84a6-05826f99923f)
![Screenshot 2024-12-25 150412](https://github.com/user-attachments/assets/faa6a42a-434c-460b-884c-db1cbbf5c8c5)
![image](https://github.com/user-attachments/assets/1cfb2e1e-4a5b-429e-a25a-7c804f34628b)
![image](https://github.com/user-attachments/assets/988a555b-1ce0-4f34-ab72-50c9021004bd)
![image](https://github.com/user-attachments/assets/6b7a72d2-dd26-40e8-80c5-1b3379cee0d0)
![image](https://github.com/user-attachments/assets/9c75a7af-e301-4279-abac-ea00e0fb657c)
![image](https://github.com/user-attachments/assets/ebf3e663-ab07-4cd1-8cac-15a727c7e18d)

### Contribution
I welcome any suggestions and contributions to help improve this web application.
