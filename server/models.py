from django.db.models import CASCADE, CharField, DecimalField, DurationField, \
  ForeignKey, ImageField, ManyToManyField, Model, PositiveSmallIntegerField, \
  PROTECT, TextField, TextChoices

class Food(Model):
  class Unit(TextChoices):
    GRAMM = 'g'
    KILOGRAMM = 'kg'
    MILLILITER = 'ml'
    LITER = 'l'
    TEASPOON = 'tsp'
    TABLESPOON = 'tbs'
    BOX = 'box'
    CAN = 'can'
    PIECE = 'pcs'
    PORTION = 'por'

  unit = CharField(max_length=3, choices=Unit.choices)
  name = CharField(max_length=100, unique=True)
  emoji = CharField(max_length=3)
  stock = DecimalField(max_digits=10, decimal_places=2)

class Recipe(Model):
  title = CharField(max_length=100, unique=True)
  picture = ImageField()
  cooking_time = DurationField(null=True, blank=True)
  ingredients = ManyToManyField(Food, through='Ingredient')

class Ingredient(Model):
  recipe = ForeignKey(Recipe, on_delete=CASCADE)
  food = ForeignKey(Food, on_delete=PROTECT)
  amount = DecimalField(max_digits=5, decimal_places=2)

class Step(Model):
  number = PositiveSmallIntegerField()
  description = TextField()
  recipe = ForeignKey(Recipe, on_delete=CASCADE)
