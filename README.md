# Media Processor (image_to_video)
This project is a Django-based backend for a media processing application. It accepts images from a React frontend, saves them in the database, and generates a video from the image after a delay of 30 seconds. The status of the image processing is updated at each step, and the user can view their uploaded images and generated videos.


## Docker build:
`docker-compose up --build`

------------------------------------------------------------------------------------------------------------------------------------------------------------

## Run without docker
## Prerequisites
`Python 3.x`

`pip (Python package installer)`

`virtualenv (optional but recommended)`

## Installation

### Clone the repository

```
git clone <repository_url>
cd django-media-processor
```

### Create a virtual environment

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the required packages

```
pip install -r requirements.txt
```


### Configure the Django project

Open image_to_video/settings.py and update the database settings and other configurations as needed.

### Run database migrations

```
python manage.py migrate
```

### Create a superuser

```
python manage.py createsuperuser
```

### Start the development server

```
python manage.py runserver
```

### API Endpoints

`POST /api/upload/: Upload an image`

`GET /api/status/<id>/: Get the status of a media file`

`GET /api/media/: List all media files`

### Usage

#### Upload an image
`Send a POST request to /api/upload/ with an image file.`

#### Check the status
`Send a GET request to /api/status/<id>/ to check the status of the image processing.`

#### View all media files
`Send a GET request to /api/media/ to list all uploaded images and generated videos.`

### Worker Process
A mock worker process generates a video from the uploaded image after a delay of 30 seconds. This process updates the status of the media file in the database.

### To start the worker process:

```
python manage.py runworker
```

### Configuration
```
MEDIA_URL: URL to serve media files
MEDIA_ROOT: Directory to store media files
```
