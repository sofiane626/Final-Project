from django_seed import Seed
from .models import CategoryArticle, Tag, Article
from user.models import User

def runBlog():
    seeder = Seed.seeder()

    # Création des catégories
    categories = ["Voiture", "Moto", "Avion"]
    for category in categories:
        CategoryArticle.objects.create(category=category)
    
    articles = [
        {
            "title": "AUDI",
            "img": "https://www.tuningblog.eu/wp-content/uploads/2022/07/Audi-RS-E-Tron-GT-Vollfolierung-Maxton-Design-Bodykit-Turismo-Wheels-6.jpg",
            "description": "Design inspiration lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed quis velit. Nulla facilisi. Nulla libero. Vivamus pharetra posuere sapien. Nam consectetuer. Sed aliquam, nunc eget euismod ullamcorper, lectus nunc ullamcorper orci, fermentum bibendum enim nibh eget ipsum. Nam consectetuer. Sed aliquam, nunc eget euismod ullamcorper, lectus nunc ullamcorper orci, fermentum bibendum enim nibh eget ipsum. Nulla libero. Vivamus pharetra posuere sapien.",
            "category": CategoryArticle.objects.get(category="Voiture"),
            "tag": Tag.objects.filter(tag__in=["Audi", "gris"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "PORSCHE",
            "img": "https://www.motortrend.com/uploads/sites/5/2018/02/2018-Porsche-911-GT3-front-three-quarter-in-motion-01.jpg",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus.",
            "category": CategoryArticle.objects.get(category="Voiture"),
            "tag": Tag.objects.filter(tag__in=["Porsche", "jaune"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "MCLAREN",
            "img": "https://drive-my.com/wp-content/uploads/2018/08/k2_items_src_5214bdb529ff52c2bc08d9b03f97b94e.jpg",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Voiture"),
            "tag": Tag.objects.filter(tag__in=["Mclaren", "orange"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "MERCEDES",
            "img": "https://bringatrailer.com/wp-content/uploads/2022/05/2012_mercedes-benz_c63-amg_c63-black-series-bat-9-04177.jpg?fit=940%2C627",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Voiture"),
            "tag": Tag.objects.filter(tag__in=["Mercedes", "gris"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "MERCEDES A45s",
            "img": "https://assets.autobuzz.my/wp-content/uploads/sites/2/2020/06/01172537/2020-Mercedes-AMG-A45-S-launched-Malaysia-AutoBuzz-4.jpg",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Voiture"),
            "tag": Tag.objects.filter(tag__in=["Mercedes", "jaune"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "YAMAHA MT07",
            "img": "https://i.ytimg.com/vi/evcUEfhFKJQ/maxresdefault.jpg",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Moto"),
            "tag": Tag.objects.filter(tag__in=["Yamaha", "noir"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "YAMAHA Tracer 700",
            "img": "https://cdn2.yamaha-motor.eu/prod/product-assets/2023/MT07TR/2023-Yamaha-MT07TR-EU-Midnight_Black-Static-006-03.jpg",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Moto"),
            "tag": Tag.objects.filter(tag__in=["Yamaha", "noir"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "YAMAHA T-MAX",
            "img": "https://www.bennetts.co.uk/-/media/bikesocial/2022-march-images/2022-yamaha-tmax-review/yamaha-tmax-review-2022-tech-max_32.ashx?h=493&w=740&la=en&hash=24C42A8BA04FD62524EBC8A1D37052FA703F93CA",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Moto"),
            "tag": Tag.objects.filter(tag__in=["Yamaha", "noir"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "F-22",
            "img": "https://www.aerocontact.com/public/img/aviaexpo/produits/images/618/detail_F-22_Raptor_900x636.jpg",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Avion"),
            "tag": Tag.objects.filter(tag__in=["voler", "guerre"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "F-16",
            "img": "https://aviationsmilitaires.net/media/pictures/1280px-F-16_rome.jpg",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Avion"),
            "tag": Tag.objects.filter(tag__in=["voler", "gris"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
    ]
    
    for art in articles:
        article = Article.objects.create(
            title=art["title"],
            img=art["img"],
            description=art["description"],
            category=art["category"],
            user=art["user"],
            validate=art["validate"],
        )
        article.tag.set(art["tag"])

    print("Seeding completed successfully!")