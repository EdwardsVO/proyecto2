from Tour import Tour
from Client import Client
import pickle

capacity_port_tour = []
capacity_localfood_tour = []
capacity_historicplaces_tour = [] 
new_line = []

def check_tour(people_in, tour_price, total_price_tour, name, tour_time):
    """Funcion que imprime en pantalla el resumen de la compra de algun paquete

    Args:

        people_in (int): Cantidad de personas por familia dentro del tour
        tour_price (float): Precio de paquete por persona
        total_price_tour (float): Cantidad total a pagar 
        name (str): Nombre del paquete elegido 
        tour_time (str): Horario del paquete elegido
    """
    print(f'''Resumen de compra: 

    Nombre del paquete: {name}
    Horario del tour: {tour_time}
    Cantidad de personas dentro del paquete: {people_in}
    Cantidad total (USD): {total_price_tour}  
    ''')
    return

def tour_start(tour_election, clients):
    """Funcion que ordena, calcula, actualiza y guarda valores de compra

    Args:

        tour_election (int): Numero de tour seleccionado
       
    """
    present_dni = []
    if tour_election == 1:
        while True:
            try:
                people_in = int(input('Ingrese cantidad de personas que asistiran al tour (Max 4 por familia): '))
                if people_in < 1 or people_in > 4:
                    print('Cantidad no valida')
                else:
                    break
            except:
                print('Cantidad no valida')
        name = 'Tour en el Puerto'
        
        tour_price = 30
        tour_time = '7 AM'
        total_price_tour = tour_price * people_in
        if people_in > 2:
            total_price_tour = total_price_tour - (tour_price * 0.1) 
        if people_in > 3:
            total_price_tour = total_price_tour - (tour_price * 0.1)   

        while True:
            try:
                tour_confirmation = int(input('Ingrese el DNI del titular: '))
                break
            except:
                print('DNI no valido')
    
        clients_data = open('ClientData.txt', 'r')
        tour_confirmation = str(tour_confirmation)
        tour_confirmation_str = tour_confirmation + '\n'
        for i in clients_data.readlines():
            if tour_confirmation == i.split('|')[0]:
                port_tour = Tour(name, people_in, tour_price, tour_time)
                clients_dni = open('ToursClientsDni.txt', 'r')
                clients_dni_append = open('ToursClientsDni.txt', 'a')
                clients_dni_append.write(i.split('|')[0] + '\n')
                clients_dni_append.close()
                clients_dni.close()
                money_spent = float(i.split('|')[3])
                money_spent += total_price_tour
                money_spent = str(money_spent)
                found = True
    
                for x in range(3):
                    new_line.append(i.split('|')[x] + '|')
                new_line.append(money_spent + '|')
                new_line.append(i.split('|')[4])
                clients_data.close()
            else: 
                new_line.append(i.split('|')[0] + '|')
                new_line.append(i.split('|')[1] + '|')
                new_line.append(i.split('|')[2] + '|')
                new_line.append(i.split('|')[3] + '|')
                new_line.append(i.split('|')[4])

        clients_data = open('ClientData.txt', 'w')
        for j, val in enumerate(new_line):
            clients_data.writelines(new_line[j])
        clients_data.close()
        del new_line[:]
        
       
        clients_dni = open('ToursClientsDni.txt', 'r')
        for x in clients_dni.readlines():
            if x == tour_confirmation_str:   
                if len(capacity_port_tour) + people_in <= 10:
                    for x in range(people_in):
                        capacity_port_tour.append(port_tour)
                    check_tour(people_in, tour_price, total_price_tour, name, tour_time)
                    clients_dni.close()
                    return
                else: 
                    print()
                    print(f'Quedan solo {10 - len(capacity_port_tour)} cupos disponibles')
                    clients_dni.close()
                    return
            else:
                continue
        clients_dni.close()

        print()
        print('DNI no registrado, intente de nuevo')
        print()
        tour_introduction(clients)


    elif tour_election == 2:
        while True:
            try:
                people_in = int(input('Ingrese cantidad de personas que asistiran al tour (Max 2 por familia): '))
                if people_in < 1 or people_in > 2:
                    print('Cantidad no valida')
                else:
                    break
            except:
                print('Cantidad no valida')

        name = 'Degustacion de Comida Local'
        
        tour_price = 100
        tour_time = '12 PM'
        total_price_tour = tour_price * people_in
         
        while True:
            try:
                tour_confirmation = int(input('Ingrese el DNI del titular: '))
                break
            except:
                print('DNI no valido')

        clients_data = open('ClientData.txt', 'r')
        tour_confirmation = str(tour_confirmation)
        tour_confirmation_str = tour_confirmation + '\n'
        for i in clients_data.readlines():
            if tour_confirmation == i.split('|')[0]:
                localfood_tour = Tour(name, people_in, tour_price, tour_time)
                clients_dni = open('ToursClientsDni.txt', 'r')
                clients_dni_append = open('ToursClientsDni.txt', 'a')
                clients_dni_append.write(i.split('|')[0] + '\n')
                clients_dni_append.close()
                clients_dni.close()
                money_spent = float(i.split('|')[3])
                money_spent += total_price_tour
                money_spent = str(money_spent)
                found = True
    
                for x in range(3):
                    new_line.append(i.split('|')[x] + '|')
                new_line.append(money_spent + '|')
                new_line.append(i.split('|')[4])
                clients_data.close()
            else: 
                new_line.append(i.split('|')[0] + '|')
                new_line.append(i.split('|')[1] + '|')
                new_line.append(i.split('|')[2] + '|')
                new_line.append(i.split('|')[3] + '|')
                new_line.append(i.split('|')[4])

        clients_data = open('ClientData.txt', 'w')
        for j, val in enumerate(new_line):
            clients_data.writelines(new_line[j])
        clients_data.close()
        del new_line[:]

        clients_dni = open('ToursClientsDni.txt', 'r')
        for x in clients_dni.readlines():
            if x == tour_confirmation_str:   
                if len(capacity_localfood_tour) + people_in <= 100:
                    for x in range(people_in):
                        capacity_localfood_tour.append(localfood_tour)
                    check_tour(people_in, tour_price, total_price_tour, name, tour_time)
                    clients_dni.close()
                    return
                else: 
                    print()
                    print(f'Quedan solo {100 - len(capacity_localfood_tour)} cupos disponibles')
                    clients_dni.close()
                    return
            else:
                continue

        clients_dni.close()
        print()
        print('DNI no registrado, intente de nuevo')
        print()
        tour_introduction(clients)

                

    elif tour_election == 3:

        while True:
            try:
                people_in = int(input('Ingrese cantidad de personas que asistiran al tour (no hay limite): '))
                if people_in > 0:
                    break
                else:
                    print('Cantidad no valida')
            except:
                print('Cantidad no valida')

        name = 'Trotar por el Pueblo/Ciudad'
        
        tour_price = 0
        tour_time = '6 AM'
        total_price_tour = tour_price * people_in
         
        while True:
            try:
                tour_confirmation = int(input('Ingrese el DNI del titular: ')) 
                break
            except:
                print('DNI no valido')
        
        clients_data = open('ClientData.txt', 'r')
        tour_confirmation = str(tour_confirmation)
        tour_confirmation_str = tour_confirmation + '\n'
        for i in clients_data.readlines():
            if tour_confirmation == i.split('|')[0]:
                excersice_tour = Tour(name, people_in, tour_price, tour_time)
                clients_dni_append = open('ToursClientsDni.txt', 'a')
                clients_dni_append.write(i.split('|')[0] + '\n')
                clients_dni_append.close()
                clients_data.close()
                check_tour(people_in, tour_price, total_price_tour, name, tour_time)
                return                
        clients_data.close()
        print()
        print('DNI no registrado, intente de nuevo')
        print()
        tour_introduction(clients)

    elif tour_election == 4:

        while True:
            try:
                people_in = int(input('Ingrese cantidad de personas que asistiran al tour (Max 4 por familia): '))
                if people_in < 1 or people_in > 4:
                    print('Cantidad no valida')
                else:
                    break
            except:
                print('Cantidad no valida')
        name = 'Visita a Lugares Historicos'
        
        tour_price = 40
        tour_time = '10 AM'
        total_price_tour = tour_price * people_in
        if people_in > 2:
            total_price_tour = total_price_tour - (tour_price * 0.1) 
        if people_in > 3:
            total_price_tour = total_price_tour - (tour_price * 0.1)   

        while True:
            try:
                tour_confirmation = int(input('Ingrese el DNI del titular: '))
                break
            except:
                print('DNI no valido')

        clients_data = open('ClientData.txt', 'r')
        tour_confirmation = str(tour_confirmation)
        tour_confirmation_str = tour_confirmation + '\n'
        for i in clients_data.readlines():
            if tour_confirmation == i.split('|')[0]:
                historicplaces_tour = Tour(name, people_in, tour_price, tour_time)
                clients_dni = open('ToursClientsDni.txt', 'r')
                clients_dni_append = open('ToursClientsDni.txt', 'a')
                clients_dni_append.write(i.split('|')[0] + '\n')
                clients_dni_append.close()
                clients_dni.close()
                money_spent = float(i.split('|')[3])
                money_spent += total_price_tour
                money_spent = str(money_spent)
                found = True
    
                for x in range(3):
                    new_line.append(i.split('|')[x] + '|')
                new_line.append(money_spent + '|')
                new_line.append(i.split('|')[4])
                clients_data.close()
            else: 
                new_line.append(i.split('|')[0] + '|')
                new_line.append(i.split('|')[1] + '|')
                new_line.append(i.split('|')[2] + '|')
                new_line.append(i.split('|')[3] + '|')
                new_line.append(i.split('|')[4])

        clients_data = open('ClientData.txt', 'w')
        for j, val in enumerate(new_line):
            clients_data.writelines(new_line[j])
        clients_data.close()
        del new_line[:]

        clients_dni = open('ToursClientsDni.txt', 'r')
        for x in clients_dni.readlines():
            if x == tour_confirmation_str:   
                if len(capacity_historicplaces_tour) + people_in <= 15:
                    for x in range(people_in):
                        capacity_historicplaces_tour.append(historicplaces_tour)
                    check_tour(people_in, tour_price, total_price_tour, name, tour_time)
                    clients_dni.close()
                    return
                else: 
                    print()
                    print(f'Quedan solo {15 - len(capacity_historicplaces_tour)} cupos disponibles')
                    clients_dni.close()
                    return
            else:
                continue

        clients_dni.close()
        print()
        print('DNI no registrado, intente de nuevo')
        print()
        tour_introduction(clients)
       
        print()
        print('DNI no registrado, intente de nuevo')
        print()
        tour_introduction(clients)


        
def tour_introduction(clients):
    """Da inicio a la aplicacion del restaurant

    """
    while True:
        try:
            tour_menu = int(input('''Introduzca una opcion: 
            1) Ver Paquetes de Tours
            2) Volver al menu principal
            >> '''))
            if tour_menu == 1 or tour_menu == 2:
                break
            else:
                print('Respuesta no valida')
        except:
            print('Respuesta no valida')

    if tour_menu == 1: 
        while True:
            try:
                tour_election = int(input('''Eliga el tour:
                1) Tour En el Puerto
                2) Degustacion de Comida Local
                3) Trotar en el Pueblo/Ciudad
                4) Visita a Lugares Historicos
                >> '''))
                if tour_election < 1 or tour_election > 4:
                    print('Respuesta no valida')
                else:
                    break
            except:
                print('Respuesta no valida')
        tour_start(tour_election, clients)

    elif tour_menu == 2:
        return 