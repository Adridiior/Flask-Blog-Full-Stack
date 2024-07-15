
# Blog Flask Application

This is a simple blog application built with Flask. It allows users to register, log in, create, update, and delete blog posts.

## Features

- User Registration and Login
- Create, Read, Update, and Delete (CRUD) blog posts
- User Authentication
- Basic Navbar for Navigation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application:

   ```bash
   flask run
   ```

## Usage

- Visit `http://127.0.0.1:5000` in your web browser.
- Register a new account.
- Log in with your credentials.
- Create, update, and delete blog posts.

## Project Structure

- `app/` - Contains the application modules and templates
- `migrations/` - Database migration files
- `venv/` - Virtual environment
- `requirements.txt` - List of dependencies
- `README.md` - This file

## Contributing

Feel free to submit issues, fork the repository and send pull requests!

## License

This project is licensed under the MIT License.

