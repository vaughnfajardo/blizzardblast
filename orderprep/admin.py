from django.contrib import admin

from .models import Addon, AddonTally, Customer, Customization, Employee, Ingredient, Manager, Milkshake, MilkshakeSales, MilkshakeTally, Orders, Recipe, RecipeIngredient, RecipeTally, Restock, Staff

admin.site.register(Addon)
admin.site.register(AddonTally) 
admin.site.register(Customer)
admin.site.register(Customization)
admin.site.register(Employee)
admin.site.register(Ingredient) 
admin.site.register(Manager)
admin.site.register(Milkshake)
admin.site.register(MilkshakeSales) 
admin.site.register(MilkshakeTally)
admin.site.register(Orders) 
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeTally)
admin.site.register(Restock) 
admin.site.register(Staff)