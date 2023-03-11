#category now available in all templates

from .models import Category
def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)