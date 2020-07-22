from FoodItem import FoodItem
from DrinkItem import DrinkItem
 
def add_food(menu):
    """Funcion para agregar elementos al menu del restaurante

    Args:

        menu (list): Estructura que almacena todos los productos

    Returns:

        menu(list): Devuelve la lista actualizada de productos del menu
    """
    food_name = input('Ingrese nombre del nuevo producto: ').title()
    while True:
        try:
            food_type = int(input(f'{food_name} es 1.Alimento 2.Bebida: '))
            if food_type == 1 or food_type == 2:
                break
            else: 
                print('Respuesta no valida')
        except:
            print('Opcion no valida')
    while True:
        try:
            price_without_tax = float(input('Ingrese el precio del producto (USD): '))
            break
        except:
            print('Precio no valido')
    food_price = (price_without_tax * 0.16) + price_without_tax 

    if food_type == 1:
        food_type = 'Alimento'
        while True:
            food_presentation = input('Escriba la letra incial de la presentacion del plato (Empaquetado o Preparacion): ').lower()
            if food_presentation == 'e' or food_presentation == 'p':
                break
            else: 
                print(f'La respuesta {food_presentation} no es valida')
        food = FoodItem(food_name, food_type, food_price, food_presentation, item_buy = 0)
        menu.append(food)

    elif food_type == 2:
        food_type = 'Bebida'
        while True:
            drink_presentation = input('Escriba la letra inicial del tamanio de la bebida (pequenia, mediana o grande): ').lower() 
            if drink_presentation == 'p' or drink_presentation == 'm' or drink_presentation == 'g':
                break
            else:
                print(f'La respuesta {drink_presentation} no es valida')
        drink = DrinkItem(food_name, food_type, food_price, drink_presentation, item_buy = 0)
        menu.append(drink)
    print()
    print(f'Su {food_name} se ha agregado al menu con exito!')
    print()
    return menu

def delete_food(menu):
    """Funcion para eliminar elementos en el menu

    Args:

        menu (list): Estructura que almacena todos los productos

    Returns:

        menu (list): Retorna el menu actualizado
    """
    delete_product = input('Ingrese el producto a eliminar: ').title()
    for i in menu:
        if delete_product == i.food_name:
            print(f'El producto {i.food_name} se ha eliminado con exito!')
            return menu.remove(i)
        print(f'El producto {delete_product} no existe en el menu!')
        return

def modify_food(menu):
    """La funcion modifica el producto ingresado

    Args:

        menu (list): Estructura que almacena todos los productos

    Returns:

        menu (list): Menu actualizado de productos
    """
    modify_product = input('Ingrese el nombre del producto a modificar: ').title()
    for j in menu:
        if modify_product == j.food_name:
            print(f'Ingrese los cambios para su {modify_product}: ')
            menu.remove(j)
            add_food(menu)
            return menu    
        print(f'Su {modify_product} no existe en el menu!')
        print()
        return

def add_combo(menu, menu_combo):
    """La funcion agrega al menu de combos, el combo creado por el usuario

    Args:

        menu (list): Estructura que almacena todos los productos del menu
        menu_combo (dict): Estructura que almacena los combos del menu

    Returns:

        menu_combo (dict): Devuelve los combos del menu actualizados
    """
    individual_combo = {} #Diccionario que lleva como key el nombre del combo y value los productos y el precio
    products_combo = [] 

    combo_name = input('Introduzca el nombre del nuevo combo: ').title()
    print('Los productos para realizar combo son los siguientes: ')
    print()
    for x in menu:
        print(x.food_name) 
    
    print()
    while True:
        individual_combo_product = input('Ingrese el nombre del producto a agregar al combo: ').title()
        for d in menu:
            if individual_combo_product == d.food_name:
                products_combo.append(d)
        while True:
            try:
                add_more_products = int(input('1.Agregar mas productos    2.Continuar     >> '))
                break
            except:
                print('Opcion no valida')
        if add_more_products == 1:
            continue
        elif add_more_products == 2:
            if len(products_combo) >= 2:
                break
            else:
                print()
                print('Se necesita al menos dos productos para formar un combo')
                print()
                continue
    while True:
        try:
            combo_price = float(input(f'Ingrese precio del combo {combo_name}: '))
            break
        except:
            print('El monto ingresado no es valido')
    combo_price_total = (combo_price * 0.16) + combo_price

    individual_combo['productos'] = products_combo
    individual_combo['precio'] = combo_price_total
    individual_combo['compras'] = 0
    menu_combo[combo_name] = individual_combo
    print()
    print(f'El combo {combo_name} se ha aniadido con exito!')
    print()
    return menu_combo

def delete_combo(menu_combo):
    """Funcion que elimina un combo del menu de combos

    Args:

        menu_combo (dict): Estructura que contiene el menu de combos

    Returns:

        dict: Devuelve el menu de combos actualizado
    """
    delete_combo_name = input('Introduzca el nombre del combo a borrar: ').title()
    if delete_combo_name in menu_combo:
        print()
        print(f'El combo {delete_combo_name} se ha eliminado con exito!')
        print()
        del menu_combo[delete_combo_name]
    else:
        print()
        print(f'su {delete_combo_name} no se encuentra en el menu de combos!')
        print()
    return menu_combo

def name_filter_client(menu, clients):
    """Ordena alfabeticamente los objetos dentro del menu

    Args:

        menu (list): Objetos del menu

    Returns:

        (list): Lista del menu ordenada alfabeticamente
    """
    name_sorted = [ u.food_name for u in menu ]
    name_sorted.sort()

    if len(name_sorted) > 0:
        for n in name_sorted: 
            for k in menu:
                if n == k.food_name:
                    print(f'Producto <<{k.food_name}>> ------ Precio: <<{k.food_price}>> ')
        print()

def price_filter_client(menu, clients):
    """Ordena por costo del producto

    Args:

        menu (list): Objetos del menu

    Returns:

        (list): lista ordenada por precio de los objetos del menu
    """
    price_sorted = [x.food_price for x in menu]
    price_sorted.sort()
    if len(price_sorted) > 0:
        for y in price_sorted: 
            for h in menu:
                if y == h.food_price:
                    print(f'Producto <<{h.food_name}>> ------ Precio: <<{h.food_price}>> ')
        print()

def name_filter_combo_client(menu_combo, clients):
    """Funcion que devuelve el menu de combos ordenado por precio y ademas permite la compra al usuario

    Args:

        menu_combo (dict): Menu de combos
        clients (list): Clientes en la embarcacion
    """
    menu_combo_sorted = sorted(menu_combo)
    print()
    for c in menu_combo_sorted:
        for j,m in menu_combo.items():
            if c == j:
                for g,l in m.items():
                    if g == 'precio':
                        print(f'''Combo: <<{c}>> ----- Precio <<{l}>>''')
    print()

def price_filter_combo_client(menu_combo, clients): 
    """Funcion que devuelve el menu de combos ordenado por precio y ademas permite la compra al usuario

    Args:

        menu_combo (dict): Menu de combos
        clients (list): Clientes en la embarcacion
    """
    prices_filtered = []
    for clave, valor in menu_combo.items():
        for t,u in valor.items():
            if t == 'precio':
                prices_filtered.append(u)
    prices_filtered_sorted = sorted(prices_filtered)
    for r in prices_filtered_sorted:
        for g,h in menu_combo.items():
            for t,y in h.items():
                if r == y:
                    print(f'''Combo <<{g}>> ----- Precio <<{y}>>''')        
    print()
   

def introduction(restaurant, menu, menu_combo, clients):
    """Menu principal del restaurant

    Args:

        restaurant: Modulo para hacer persistente los datos
        menu (list): Estructura con los datos de los productos del menu
        menu_combo (dict): Estructura con los combos del menu
    """
    print ('\\\Bienvenido a su Restaurat <CocoSaman>///')
    while True:
        while True:
            try:
                distribution_election = int(input('''Ingrese su ocupacion:
                1) Administrador
                2) Cliente
                3) Volver al menu principal 
                >> '''))
                if distribution_election < 1 or distribution_election > 3:
                    print('Respuesta no valida')
                else:
                    break
            except:
                print('Dato no valido')

        if distribution_election == 1:
            while True:
                try:
                    administrator_election = int(input('''Ingrese una opcion:
                    1) Agregar producto 
                    2) Eliminar producto
                    3) Modificar producto
                    4) Agregar combo
                    5) Eliminar combo
                    >> '''))
                    if administrator_election < 1 or administrator_election > 5:
                        print('Respuesta invalida')
                    else:
                        break
                except:
                    print('Opcion no valida')

            if administrator_election == 1:
                add_food(menu)
            elif administrator_election == 2: 
                delete_food(menu) 
            elif administrator_election == 3:
                modify_food(menu) 
            elif administrator_election == 4:
                add_combo(menu, menu_combo) 
            elif administrator_election == 5: 
                delete_combo(menu_combo) 

        elif distribution_election == 2: 
            while True:
                try:
                    client_election = int(input('''Ingrese opcion de busqueda:
                        1. Filtrar productos por nombres
                        2. Filtrar productos de menor a mayor precio
                        3. Filtrar combos por nombres
                        4. Filtrar combos de menor a mayor precio
                        >> '''))
                    if client_election < 1 or client_election > 4:
                        print('Respuesta no valida')
                    else:
                        break
                except:
                    print('Opcion no valida')
            
            if client_election == 1: 
                name_filter_client(menu, clients)
            if client_election == 2: 
                price_filter_client(menu, clients)
            if client_election == 3: 
                name_filter_combo_client(menu_combo, clients)
            if client_election == 4:
                price_filter_combo_client(menu_combo, clients)
        

        elif distribution_election == 3: 
            return 
             
            

