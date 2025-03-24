# Tech Connect Hub Realtime

A real-time collaboration platform built with Django that enables developers to connect, collaborate, and work together on projects.

## Features

- Real-time user interactions
- Project management and collaboration
- User authentication and authorization
- RESTful API endpoints
- AWS S3 integration for file storage
- PostgreSQL database support
- JWT-based authentication

## Tech Stack

- **Backend Framework**: Django 5.1.4
- **API Framework**: Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: PostgreSQL
- **File Storage**: AWS S3
- **Server**: Gunicorn
- **Static Files**: Whitenoise

## Prerequisites

- Python 3.x
- PostgreSQL
- AWS Account (for S3 storage)
- Virtual Environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Tech_connect_hub_realtime
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
Tech_connect_hub_realtime/
├── api/            # API endpoints and views
├── devsearch/      # Main project configuration
├── projects/       # Project-related models and views
├── static/         # Static files
├── templates/      # HTML templates
├── users/          # User-related models and views
├── manage.py       # Django management script
└── requirements.txt # Project dependencies
```

## API Documentation

The API endpoints are available at `/api/`. Authentication is required for most endpoints using JWT tokens.

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers. 