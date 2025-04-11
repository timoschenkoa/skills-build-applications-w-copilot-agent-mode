# Updated MongoDB database connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Enable CORS for all origins, methods, and headers
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['*']

# Allow all hosts
ALLOWED_HOSTS = ['*']