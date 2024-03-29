from django.http import HttpResponse
from django.db.models import Sum

from recipes.models import ShoppingList, RecipesIngredients


def create_shopping_cart_file(user):
    """Создает файл с суммированным перечнем и количеством
    необходимых ингредиентов."""
    if not user.shopping_cart.exists():
        return None

    recipes_list = ShoppingList.objects.filter(
        user=user).values_list('recipe_id', flat=True)

    shopping_list = RecipesIngredients.objects.filter(
        recipe_id__in=recipes_list
    ).values('ingredient_id__name',
             'ingredient_id__measurement_unit'
             ).annotate(total_amount=Sum('amount'))

    content = 'Ваш список покупок:\n\n'
    for item in shopping_list:
        name = item['ingredient_id__name']
        amount = item['total_amount']
        content += f'{name}: {amount}\n'

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = (
        'attachment; filename="shopping_cart.txt"')
    response.write(content)

    return response
