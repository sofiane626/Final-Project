from django_seed import Seed
from .models import CategoryArticle, Tag, Article
from user.models import User

def runBlog():
    seeder = Seed.seeder()

    # Création des catégories
    categories = ["Bedroom", "Living Room", "Dining Room"]
    for category in categories:
        CategoryArticle.objects.create(category=category)
    
    articles = [
        {
            "title": "Latest trend : The rise of shoppable posts",
            "img": "https://www.meubles-mailleux.com/assets/cache/214ad2b5-c5ae-4ca2-827c-c71b41e600e6/literie-01-1.jpg",
            "description": "Design inspiration lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed quis velit. Nulla facilisi. Nulla libero. Vivamus pharetra posuere sapien. Nam consectetuer. Sed aliquam, nunc eget euismod ullamcorper, lectus nunc ullamcorper orci, fermentum bibendum enim nibh eget ipsum. Nam consectetuer. Sed aliquam, nunc eget euismod ullamcorper, lectus nunc ullamcorper orci, fermentum bibendum enim nibh eget ipsum. Nulla libero. Vivamus pharetra posuere sapien.",
            "category": CategoryArticle.objects.get(category="Bedroom"),
            "tag": Tag.objects.filter(tag__in=["Rugs", "Decor"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "Comfortable Sofa Set",
            "img": "https://www.meubles-mailleux.com/assets/cache/3f59bab9-4bbb-484e-9f64-b0f8e2cacb48/salon-01-2023.jpg",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus.",
            "category": CategoryArticle.objects.get(category="Living Room"),
            "tag": Tag.objects.filter(tag__in=["Sofas", "Chairs"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "Stylish Dining Table",
            "img": "https://www.meubles-mailleux.com/assets/cache/af6ef92c-983b-4853-ae9b-9df777a22969/salle-a-manger-01-2023.jpg",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Dining Room"),
            "tag": Tag.objects.filter(tag__in=["Shelves", "Tables"]),
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