#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
  if set(recipe.keys()) == set(ingredients.keys()):
    r = recipe.items()
    i = ingredients.items()
    batches = []
    for x in i:
      for y in r:
        if x[0] == y[0]:
          batches.append(x[1] // y[1])

    return min(batches)

  else:
    return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))