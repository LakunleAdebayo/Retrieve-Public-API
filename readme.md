# Django Information API

A simple RESTful API built with Django that collects my basic information including email, current datetime, and my GitHub repository URL.

## Features

- Returns basic information in JSON format
- CORS enabled for cross-origin requests

## API Specification

### Endpoint

```
GET /
```

### Response Format

```json
{
  "email": "olakunle.adebayo77@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "github link"
}
```

## Local Development Setup

1. Clone the repository:
```bash
git clone "github link" 
cd your-repo
```

2. Create and activate a virtual environment:
```bash
python -m venv myenv
source myenv\Scripts\activate  
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

