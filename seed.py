import os
import django
import random
from faker import Faker

# configuracion de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from inventory.models import Category, Item

def seed_data():
    fake = Faker(['es_ES'])
    print("Limpiando datos existentes...")
    Item.objects.all().delete()

    print("Creando categorías...")
    categories = ['Herramientas Eléctricas', 'Herramientas de Mano', 'Equipos de Medición', 'Seguridad']
    cat_objs = [Category.objects.get_or_create(name=cat)[0] for cat in categories]

    print("Creando 15 ítems de ejemplo...")
    herramientas = ['Taladro', 'Martillo', 'Multímetro', 'Sierra Circular', 'Destornillador', 'Lijadora', 'Nivel Láser', 'Amoladora']

    for _ in range(15):
        nombre = f"{random.choice(herramientas)} {fake.word().capitalize()}"
        Item.objects.create(
            name=nombre,
            category=random.choice(cat_objs),
            brand=fake.company(),
            serial_number=fake.bothify(text='SN-####-####-??'),
            description=fake.sentence(nb_words=10), # <--- AQUÍ: DEBE SER DESCRIPTION
            purchase_date=fake.date_between(start_date='-2y', end_date='today')
        )
    print("¡listo! 15 ítems de ejemplo creados.")

if __name__ == '__main__':
    seed_data()