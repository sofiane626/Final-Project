from django_seed import Seed
from .models import Category, Product

def runProduct():
    seeder = Seed.seeder()
    
    categories = [
        {'value': 'Chemises'},
        {'value': 'T-Shirts'},
        {'value': 'Vestes'},
        {'value': 'Sweat'},
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
            'stock':2,
        
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
            'stock':4,

        },
        {
            'img1': 'https://static.zara.net/photos///2023/I/0/2/p/0794/308/800/2/w/750/0794308800_6_1_1.jpg?ts=1686757099200', 
            'img2': 'https://static.zara.net/photos///2023/I/0/2/p/0794/308/800/2/w/750/0794308800_6_2_1.jpg?ts=1686148772997', 
            'img3': 'https://static.zara.net/photos///2023/I/0/2/p/0794/308/800/2/w/750/0794308800_6_3_1.jpg?ts=1686148774432',
            'description' : 'Chemise en tissu à texture pour un entretien facile au quotidien.',
            'name': 'CHEMISE À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[0],
            'price': 75,
            'promo': 0,
            'stock':5,

        },
        {
            'img1': 'https://static.zara.net/photos///2023/I/0/2/p/4087/480/055/2/w/750/4087480055_6_1_1.jpg?ts=1687859877632', 
            'img2': 'https://static.zara.net/photos///2023/I/0/2/p/4087/480/055/2/w/750/4087480055_6_2_1.jpg?ts=1687859877736', 
            'img3': 'https://static.zara.net/photos///2023/I/0/2/p/4087/480/055/2/w/750/4087480055_6_3_1.jpg?ts=1687859882449',
            'description' : 'T-shirt en tissu à texture pour un entretien facile au quotidien.',
            'name': 'T-shirt À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[1],
            'price': 100,
            'promo': 0,
            'stock':3,

        },
        {
            'img1': 'https://static.zara.net/photos///2023/I/0/2/p/4442/350/615/2/w/750/4442350615_6_1_1.jpg?ts=1688110922254', 
            'img2': 'https://static.zara.net/photos///2023/I/0/2/p/4442/350/615/2/w/750/4442350615_6_2_1.jpg?ts=1688110925005', 
            'img3': 'https://static.zara.net/photos///2023/I/0/2/p/4442/350/615/2/w/750/4442350615_6_3_1.jpg?ts=1688110928828',
            'description' : 'T-shirt en tissu à texture pour un entretien facile au quotidien.',
            'name': 'T-shirt À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[1],
            'price': 10,
            'promo': 0,
            'stock':4,

        },
        {
            'img1': 'https://static.zara.net/photos///2023/I/0/2/p/4087/461/500/2/w/750/4087461500_6_1_1.jpg?ts=1686910790855', 
            'img2': 'https://static.zara.net/photos///2023/I/0/2/p/4087/461/500/2/w/750/4087461500_6_2_1.jpg?ts=1686910790306', 
            'img3': 'https://static.zara.net/photos///2023/I/0/2/p/4087/461/500/2/w/750/4087461500_6_3_1.jpg?ts=1686910792596',
            'description' : 'T-shirt en tissu à texture pour un entretien facile au quotidien.',
            'name': 'T-shirt À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[1],
            'price': 40,
            'promo': 0,
            'stock':4,

        },
        {
            'img1': 'https://static.zara.net/photos///2023/V/0/2/p/4302/402/431/2/w/750/4302402431_6_1_1.jpg?ts=1671705771650', 
            'img2': 'https://static.zara.net/photos///2023/V/0/2/p/4302/402/431/2/w/750/4302402431_6_2_1.jpg?ts=1671705771522', 
            'img3': 'https://static.zara.net/photos///2023/V/0/2/p/4302/402/431/2/w/750/4302402431_6_3_1.jpg?ts=1671705771788',
            'description' : 'Veste en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Veste À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[2],
            'price': 300,
            'promo': 0,
            'stock':4,

        },
        {
            'img1': 'https://static.zara.net/photos///2022/I/0/2/p/3046/411/800/2/w/750/3046411800_6_1_1.jpg?ts=1666259420900', 
            'img2': 'https://static.zara.net/photos///2022/I/0/2/p/3046/411/800/2/w/750/3046411800_6_2_1.jpg?ts=1666259421006', 
            'img3': 'https://static.zara.net/photos///2022/I/0/2/p/3046/411/800/2/w/750/3046411800_6_3_1.jpg?ts=1666259423486',
            'description' : 'Veste en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Veste À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[2],
            'price': 350,
            'promo': 0,
            'stock':10,

        },
        {
            'img1': 'https://static.zara.net/photos///2023/V/0/2/p/0706/506/802/2/w/750/0706506802_6_1_1.jpg?ts=1684232563523', 
            'img2': 'https://static.zara.net/photos///2023/V/0/2/p/0706/506/802/2/w/750/0706506802_6_2_1.jpg?ts=1684232562881', 
            'img3': 'https://static.zara.net/photos///2023/V/0/2/p/0706/506/802/2/w/750/0706506802_6_3_1.jpg?ts=1684232563710',
            'description' : 'Veste en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Veste À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[2],
            'price': 250,
            'promo': 0,
            'stock':10,

        },
        {
            'img1': 'https://static.zara.net/photos///2023/I/0/2/p/0761/350/800/2/w/750/0761350800_6_1_1.jpg?ts=1688110917303', 
            'img2': 'https://static.zara.net/photos///2023/I/0/2/p/0761/350/800/2/w/750/0761350800_6_2_1.jpg?ts=1688110917398', 
            'img3': 'https://static.zara.net/photos///2023/I/0/2/p/0761/350/800/2/w/750/0761350800_6_3_1.jpg?ts=1688110926368',
            'description' : 'Sweat en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Sweat À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[3],
            'price': 50,
            'promo': 0,
            'stock':10,
            
        },
        {
            'img1': 'https://static.zara.net/photos///2023/I/0/2/p/0761/350/807/2/w/750/0761350807_6_1_1.jpg?ts=1688039025314', 
            'img2': 'https://static.zara.net/photos///2023/I/0/2/p/0761/350/807/2/w/750/0761350807_6_2_1.jpg?ts=1688039024303', 
            'img3': 'https://static.zara.net/photos///2023/I/0/2/p/0761/350/807/2/w/750/0761350807_6_3_1.jpg?ts=1688039028422',
            'description' : 'Sweat en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Sweat À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[3],
            'price': 50,
            'promo': 0,
            'stock':8,
            
        },
        {
            'img1': 'https://static.zara.net/photos///2023/V/0/2/p/2795/420/615/2/w/750/2795420615_6_1_1.jpg?ts=1679917968550', 
            'img2': 'https://static.zara.net/photos///2023/V/0/2/p/2795/420/615/2/w/750/2795420615_6_2_1.jpg?ts=1679917969681', 
            'img3': 'https://static.zara.net/photos///2023/V/0/2/p/2795/420/615/2/w/750/2795420615_6_3_1.jpg?ts=1679917987372',
            'description' : 'Sweat en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Veste À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[3],
            'price': 50,
            'promo': 0,
            'stock':4,
            
        },
        {
            'img1': 'https://static.zara.net/photos///2022/V/0/2/p/1564/414/401/2/w/750/1564414401_6_1_1.jpg?ts=1643706451463', 
            'img2': 'https://static.zara.net/photos///2022/V/0/2/p/1564/414/401/2/w/750/1564414401_6_2_1.jpg?ts=1643708020280', 
            'img3': 'https://static.zara.net/photos///2022/V/0/2/p/1564/414/401/2/w/750/1564414401_6_3_1.jpg?ts=1643706529738',
            'description' : 'Gilet en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Gilet À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[4],
            'price': 70,
            'promo': 0,
            'stock':6,
            
        },
        {
            'img1': 'https://static.zara.net/photos///2023/V/0/2/p/6216/409/700/2/w/750/6216409700_6_1_1.jpg?ts=1679314589493', 
            'img2': 'https://static.zara.net/photos///2023/V/0/2/p/6216/409/700/2/w/750/6216409700_6_2_1.jpg?ts=1679314589582', 
            'img3': 'https://static.zara.net/photos///2023/V/0/2/p/6216/409/700/2/w/750/6216409700_6_3_1.jpg?ts=1679314591937',
            'description' : 'Gilet en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Gilet À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[4],
            'price': 20,
            'promo': 0,
            'stock':3,
            
        },
        {
            'img1': 'https://static.zara.net/photos///2023/V/0/2/p/4358/689/052/2/w/750/4358689052_6_1_1.jpg?ts=1676032622994', 
            'img2': 'https://static.zara.net/photos///2023/V/0/2/p/4358/689/052/2/w/750/4358689052_6_2_1.jpg?ts=1676032621393', 
            'img3': 'https://static.zara.net/photos///2023/V/0/2/p/4358/689/052/2/w/750/4358689052_6_3_1.jpg?ts=1676032641261',
            'description' : 'Gilet en tissu à texture pour un entretien facile au quotidien.',
            'name': 'Gilet À TEXTURE ENTRETIEN FACILE',
            'category': Category.objects.all()[4],
            'price': 10,
            'promo': 0,
            'stock':4,
            
        },
    ]
    
    for item in products:
        seeder.add_entity(Product, 1, item)
    print(seeder.execute())
    
        
