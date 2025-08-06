# Django Ecommerce

A basic e-commerce website built with Django. This project demonstrates a simple yet functional online store, showcasing core Django concepts along with front-end and back-end integration.

## Live Demo

You can check out the deployed version here:  
[https://django-ecommerce-wbub.onrender.com/](https://django-ecommerce-wbub.onrender.com/)

## Features

- User authentication (sign up, login, logout)
- Product listing and detail pages
- Shopping cart functionality
- Order placement and management
- Admin panel for product and order management
- Responsive front-end using HTML, CSS, and JavaScript

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **Deployment:** [Render](https://render.com/)

## Learning Outcomes

This project taught me:
- The core concepts of Django, including models, views, templates, and forms
- How to connect the front end and back end in a web application
- User authentication and authorization in Django
- Managing static files and media in Django
- Deploying Django applications to a live server

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prasath-m21/django-ecommerce.git
   cd django-ecommerce
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit [http://localhost:8000/](http://localhost:8000/)

## Directory Structure

```
django-ecommerce/
├── manage.py
├── ecommerce/           # Django project settings
├── store/               # Main app (products, cart, orders)
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, images)
├── requirements.txt
└── README.md
```

## Screenshots

<!-- You can add screenshots of your app here -->
<!-- ![Homepage Screenshot](screenshots/homepage.png) -->

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for suggestions or improvements.

## License

This project is licensed under the MIT License.

---

**Deployed at:** [https://django-ecommerce-wbub.onrender.com/](https://django-ecommerce-wbub.onrender.com/)
