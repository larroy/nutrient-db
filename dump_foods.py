from nutrientdb import *
n = NutrientDB()
l = n.get_nutrient_list()
f = map(n.query_main_nutrients, l)
foods = open("foods.json", "wb")
for x in f:
    foods.write(json.dumps(x))
    foods.write('\n')

