from datetime import date, timedelta
from pets.models import Pet, Product


def pets_context_processor(request):
    all_pets = Pet.objects.all()
    all_products = Product.objects.all()
    tomorrow = date.today() + timedelta(days=1)
    ctx = {'all_pets': all_pets,
           'all_products': all_products,
           'tomorrow': tomorrow}
    return ctx
