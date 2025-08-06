#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Auto-create superuser
echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com', 
        password='admin123'
    )
    print('Superuser created: username=admin, password=admin123')
else:
    print('Superuser already exists')
END

# Create sample products
echo "Creating sample products..."
if [ -f "create_sample_products.py" ]; then
    python manage.py shell < create_sample_products.py
    echo "Sample products created!"
else
    echo "Sample products script not found, skipping..."
fi

echo "Build completed successfully!"
