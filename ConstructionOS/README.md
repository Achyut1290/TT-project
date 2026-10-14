# ConstructionOS

ConstructionOS is a Flask-based construction management system for tracking projects, tasks, materials, labour, expenses, site updates, analytics, and reports.

## Features
- User registration and login
- Dashboard overview
- Project management
- Task management
- Material and inventory tracking
- Labour management
- Expense tracking
- Daily site updates
- Analytics dashboard
- Reports

## Tech Stack
- Python
- Flask
- MySQL
- HTML/CSS/Bootstrap
- JavaScript

## Setup
1. Create a MySQL database named `constructionos`.
2. Update your MySQL credentials in `config.py`.
3. Run the SQL script in `database/schema.sql`.
4. Create and activate a virtual environment.
5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
python app.py
```

7. Open `http://127.0.0.1:5000` in the browser.

## Password recovery
The forgot-password flow creates a signed reset link that expires after 30 minutes and can only be used until the password changes. To email reset links, configure `SMTP_HOST`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, and `SMTP_SENDER` in the environment. For local development without SMTP, the reset link is written to the Flask terminal log.

Set `FLASK_SECRET_KEY` to a long random value for deployments so reset links and login sessions remain valid across restarts.

## Notes
This project is structured as an intermediate working system, suitable for a viva/project demonstration.
