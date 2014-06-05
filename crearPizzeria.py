# -*- encoding: utf-8 -*-

def CrearTipusPizza():
    from Comanda.models import TipusPizza
    tipus = [('Calzone', 2), ('Normal', 0), ('Panini', 2), ('Focaccia', 3), ('Massa Fina', 1), ('Massa De Pa', 2)]
    for t in tipus:
        tp = TipusPizza()
        tp.tipus_pizza = t[0]
        tp.preu_tipus = t[1]
        tp.save() 
        
def CrearPizzes():
    from Comanda.models import Varietat
    varietats = [
                 ('Margarida', 5, True, 'margarida.png'),
                 ('Rústica', 6, True, 'rustica.png'),
                 ('Prosciutto', 5, True, 'prosciutto.png'),
                 ('Tropical', 6, True, 'tropical.png'),
                 ('Al Gust', 3, False, 'margarida.png'),
                 ('Pepperoni', 5, True, 'pepperoni.png'),
                 ('L\'escala', 8, True, 'lEscala.png'),
                 ('Vegetal', 7, True, 'vegetal.png'),
                 ('Marinera', 9, True, 'marinera.png'),
                 ('Quatre Formatges', 6, True, 'quatreFormatges.png'),
                 ('Quatre Estacions', 6, True, 'quatreEstacions.png'),
                 ('Carbonara', 6, True, 'carbonara.png'),
                 ('Barbacoa', 7, True, 'barbacoa.png'),
                 ('Diávola', 7, True, 'diavola.png'),
                 ('Capriciosa', 6, True, 'capriciosa.png'),
                 ('Funghi', 7, True, 'funghi.png'),
                 ('Spezial', 9, True, 'spezial.png'),
                 ('De La Casa', 9, True, 'deLaCasa.png')
                 ]
    for v in varietats:
        vari = Varietat()
        vari.nom_pizza = v[0]
        vari.preu_base = v[1]
        vari.es_predefinida = v[2]
        vari.imatge_pizza_ext = v[3]
        vari.save()
        
def CrearIngredients():
    from Comanda.models import Ingredient
    ingredients = [
                   ('Formatge', 1, 10, 'formatgeIng.png'),
                   ('Pernil', 1, 10, 'pernilIng.png'),
                   ('Pinya', 1, 10, 'pinyaIng.png'),
                   ('Salami', 1, 10, 'salamiIng.png'),
                   ('Bolets', 1, 10, 'boletsIng.png'),
                   ('Carn Adobada', 1, 10, 'carnAdobadaIng.png'),
                   ('Formatge Blau', 1, 10, 'formatgeBlauIng.png'),
                   ('Anxoves', 1, 10, 'anxovesIng.png'),
                   ('Olives', 1, 10, 'olivesIng.png'),
                   ('Tonyina', 1, 10, 'tonyinaIng.png'),
                   ('Musclos', 1, 10, 'musclosIng.png'),
                   ('Parmesà Rallat', 1, 10, 'parmesaRallatIng.png'),
                   ('Oli Picant', 1, 10, 'oliPicantIng.png'),
                   ('Pebrot', 1, 10, 'pebrotIng.png'),
                   ('Blat De Moro', 1, 10, 'blatDeMoroIng.png'),
                   ('Formatge Roquefort', 1, 10, 'formatgeRoquefortIng.png'),
                   ('Tomàquet', 1, 10, 'tomaquetIng.png'),
                   ('Bacó', 1, 10, 'bacoIng.png'),
                   ('Orenga', 1, 10, 'orengaIng.png'),
                   ]
    for i in ingredients:
        ing = Ingredient()
        ing.nom_ingredient = i[0]
        ing.preu_ingredient = i[1]
        ing.stock = i[2]
        ing.extensio_imatge = i[3]
        ing.save()
    
    