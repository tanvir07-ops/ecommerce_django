# All category te click korle jate sob category gula dekhay tar jonnne ei file ti create kora!

from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)