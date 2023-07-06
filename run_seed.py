import django
django.setup()

from user.seed import runConnexion
from product.seed import runProduct


if __name__ == '__main__':
    runConnexion()
    runProduct()
