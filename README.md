# Tweet--Project
A basic tweet management application built using Python and Django to learn web development.

##  Project Description
This Tweet Management Project is a web-based application built using Django that allows users to create, read, update, and delete (CRUD) tweets. It includes user authentication, tweet posting, and management features.

##  Features
✅ User Authentication – Signup, login, and logout functionality.
✅ Tweet Posting – Users can create and manage their tweets.
✅ CRUD Operations – Edit and delete tweets as needed.
✅ User Profile Management – Users can manage their profiles.
✅ Responsive Design – Built with Bootstrap for mobile-friendly UI.
✅ Django Admin Panel – Manage users and tweets through the Django admin interface.

## Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: MySql.
Version Control: Git & GitHub

## Installation & Setup
Follow these steps to set up the project on your local machine.
## Clone the Repository

git clone https://github.com/Akshay-Kumar-97/Tweet--Project.git
cd Tweet--Project

## Create & Activate a Virtual Environment
python -m venv env
source env/bin/activate    # On macOS/Linux
env\Scripts\activate       # On Windows

## Install Dependencies
pip install -r requirements.txt

## Apply Database Migrations
python manage.py migrate

## Create a Superuser (for Admin Panel)
python manage.py createsuperuser

## Follow the prompts to set up a username and password.

##Start the Development Server
python manage.py runserver
Now, open your browser and visit:

Tweet Homepage: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
