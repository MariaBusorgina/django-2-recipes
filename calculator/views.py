from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def ingredients(request, dish):
    servings = int(request.GET.get("servings", 1))
    dish_param = dish
    found_dish = DATA[dish_param].copy()
    found_dish.update((x, y * servings) for x, y in found_dish.items())
    context = {
        'recipe': found_dish,
    }
    return render(request, "calculator/index.html", context)

