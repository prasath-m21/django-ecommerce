from .settings import *

# Security settings
DEBUG = False
ALLOWED_HOSTS = ['your-app-name.onrender.com', 'localhost', '127.0.0.1']

# Database - Use environment variable
import dj_database_url
DATABASES['default'] = dj_database_url.config(
    default='postgresql://localhost/ecommerce_db',
    conn_max_age=600
)

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files - Use Cloudinary for production
# You'll need to set up Cloudinary later

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Email - Use real email service in production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
