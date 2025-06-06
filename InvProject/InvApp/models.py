from django.db import models

# Create your models here.


class Category(models.Model):
    # On crée d’abord un identifiant automatique (par défaut Django ajoute un AutoField si on n’en déclare pas, 
    # mais on peut expliciter si on veut)
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique = True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    # Ajout du lien vers Category
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='products'
    )
    
    def __str__(self):
        return self.name