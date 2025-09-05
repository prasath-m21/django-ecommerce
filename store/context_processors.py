# store/context_processors.py

from .models import Category

def categories_processor(request):
    """
    Context processor to make categories available in all templates.
    This allows us to display categories in the navigation menu on every page.
    """
    return {
        'categories': Category.objects.all()
    }
