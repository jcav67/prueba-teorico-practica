"""
    Se crearon objetos independientes que se añaden a una lista 
    con el cual se hará toda la operación
"""

def crear_catalogo(catalogo) -> dict:
    """
        crea un diccionario de acuerdo a los requerimientos suministrados
        Fabricante → Categoría → Género
        args:
            catalogo-> List
        
        return:
            catalogo_completo -> dict
    """
    catalogo_completo = {}
    for producto in catalogo:
    
        if producto['Fabricante'] not in catalogo_completo.keys():
            catalogo_completo[producto['Fabricante']] = {}
        if producto['Categoría'] not in catalogo_completo[producto['Fabricante']].keys():
            
            catalogo_completo[producto['Fabricante']][producto['Categoría']] ={}
        
        if producto['Género'] not in catalogo_completo[producto['Fabricante']][producto['Categoría']].keys():        
            catalogo_completo[producto['Fabricante']][producto['Categoría']][producto['Género']] = [producto]
        else:
            catalogo_completo[producto['Fabricante']][producto['Categoría']][producto['Género']].append(producto) 

    return catalogo_completo


producto_1={
    "Nombre": "Zapatos XYZ",
    "Código_de_barras": "8569741233658",
    "Fabricante": "Deportes XYZ",
    "Categoría": "Zapatos",
    "Género": "Masculino",
    }

producto_2={
    "Nombre": "Zapatos ABC",
    "Código_de_barras": "7452136985471",
    "Fabricante": "Deportes XYZ",
    "Categoría": "Zapatos",
    "Género": "Femenino"
    }

producto_3= {
    "Nombre": "Camisa DEF",
    "Código_de_barras": "5236412896324",
    "Fabricante": "Deportes XYZ",
    "Categoría": "Camisas",
    "Género": "Masculino"
    }

producto_4 ={ 
    "Nombre": "Bolso KLM",
    "Código_de_barras": "5863219635478",
    "Fabricante": "Carteras Hi-Fashion",
    "Categoría": "Bolsos",
    "Género": "Femenino"
    }

catalogo = [producto_1, producto_2, producto_3, producto_4]

print(crear_catalogo(catalogo=catalogo))


