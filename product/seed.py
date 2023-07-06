from django_seed import Seed
from .models import Category, Product

def runProduct():
    seeder = Seed.seeder()

    categories = [
        {'value': 'Chemises'},
        {'value': 'T-Shirts'},
        {'value': 'Vestes'},
        {'value': 'Sweatshirts'},
        {'value': 'Gilets'},
    ]

    for item in categories:
        seeder.add_entity(Category, 1, item)
    
    print(seeder.execute())
    
    
    #----------------------------------------------------------------
    
    products = [
        {
            'img1': 'https://static.zara.net/photos///2023/I/0/2/p/8211/320/250/2/w/1126/8211320250_6_1_1.jpg?ts=1683813219804', 
            'img2': 'https://static.zara.net/photos///2023/I/0/2/p/8211/320/250/2/w/1126/8211320250_6_2_1.jpg?ts=1683813219785', 
            'img3': 'https://static.zara.net/photos///2023/I/0/2/p/8211/320/250/2/w/1126/8211320250_6_3_1.jpg?ts=1683813220377',
            'description' : 'Chemise en tissu à texture pour un entretien facile au quotidien.',
            'name': 'CHEMISE À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[0],
            'price': 26,
            'promo': 22,
            'tailleS':2,
            'tailleM':2,
            'tailleL':2,
            'tailleXL':2,
        },
        {
            'img1': 'https://static.zara.net/photos///2023/I/0/2/p/3277/306/800/2/w/750/3277306800_6_1_1.jpg?ts=1685354035104', 
            'img2': 'https://static.zara.net/photos///2023/I/0/2/p/3277/306/800/2/w/750/3277306800_6_2_1.jpg?ts=1685354034959', 
            'img3': 'https://static.zara.net/photos///2023/I/0/2/p/3277/306/800/2/w/750/3277306800_6_3_1.jpg?ts=1685354040445',
            'description' : 'Chemise en tissu à texture pour un entretien facile au quotidien.',
            'name': 'CHEMISE À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[0],
            'price': 46,
            'promo': 0,
            'tailleS':4,
            'tailleM':8,
            'tailleL':6,
            'tailleXL':1,
        },
    ]
    
    for item in products:
        seeder.add_entity(Product, 1, item)
    print(seeder.execute())
    
        
