# -*- encoding: utf-8 -*-

def CrearTipusPizza():
    from Comanda.models import TipusPizza
    tipus = [('Calzone', 2), ('Normal', 0), ('Panini', 2), ('Focaccia', 3), ('Massa Fina', 1), ('Massa De Pa', 2)]
    for t in tipus:
        tp = TipusPizza()
        tp.tipus_pizza = t[0]
        tp.preu_tipus = t[1]
        tp.save() 