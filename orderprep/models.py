# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addon(models.Model):
    addon_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    customization = models.ForeignKey('Customization', models.DO_NOTHING)
    ingredient = models.ForeignKey('Ingredient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'addon'


class AddonTally(models.Model):
    date_recorded = models.DateField(blank=True, null=True)
    ingredient = models.ForeignKey('Ingredient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'addon_tally'

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Customization(models.Model):
    customization_id = models.IntegerField(primary_key=True)
    customization_name = models.CharField(max_length=25, blank=True, null=True)
    customization_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customization'


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Ingredient(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    ingredient_name = models.CharField(max_length=25, blank=True, null=True)
    category = models.CharField(max_length=15, blank=True, null=True)
    price_per_serving = models.FloatField(blank=True, null=True)
    quantity_on_hand = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


class Manager(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    manager_schedule = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Milkshake(models.Model):
    shake_id = models.IntegerField(primary_key=True)
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING)
    customization_id = models.IntegerField()
    shake_price = models.FloatField(blank=True, null=True)
    size = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milkshake'


class MilkshakeSales(models.Model):
    date_recorded = models.DateField(blank=True, null=True)
    total_sales = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milkshake_sales'


class MilkshakeTally(models.Model):
    date_recorded = models.DateField(blank=True, null=True)
    total_tally = models.IntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milkshake_tally'


class Orders(models.Model):
    txn_number = models.IntegerField(primary_key=True)
    order_date = models.DateField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'


class Recipe(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length=25, blank=True, null=True)
    recipe_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class RecipeIngredient(models.Model):
    recipe = models.OneToOneField(Recipe, models.DO_NOTHING, primary_key=True)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)
    shake_size = models.CharField(max_length=5, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe_ingredient'
        unique_together = (('recipe', 'ingredient'),)


class RecipeTally(models.Model):
    date_recorded = models.DateField(blank=True, null=True)
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recipe_tally'


class Restock(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    restock_status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restock'


class Staff(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    staff_role = models.CharField(max_length=25, blank=True, null=True)
    role_schedule = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
