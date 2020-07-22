from Room import Room
from Client import Client
import CruiseManagement
import pickle

#El Dios de los Mares:
simple_edlm = []

def ticket_invoice(total_family_client, clients, cruise_name): 
    """Imprime la factura, crea y almacena el cliente en un archivo de texto plano 

    Args:

        total_family_client (int): Cantidad de familiares que se hospedaran del cliente
        cruise_name (str): Nombre de los cruceros
    """

    empty_list = []
    abundante = False
    rooms_elected = ''
    rooms_price = 0
    rooms_price_discount = 0
    name = input('Ingrese su nombre: ').title()
    while True:
        try:
            age = int(input('Ingrese su edad: '))
            break
        except:
            print('Edad no valida')
    while True:
        try:
            dni = int(input('Ingrese su DNI: '))
            break
        except:
            print('DNI no valido')
    while True:
        try:
            disease = int(input('''Sufre usted alguna discapacidad: 
            1) Si
            2) No
            Ingrese numero de opcion: '''))
            if disease == 1:
                disease = True
                break
            elif disease == 2:
                disease = False
                break
            else:
                print('Opcion no valida')
        except:
            print('Opcion no valida')
        
    clients_data_encripted = open('RoomsDataBase.txt', 'rb')
    clients_data_decrypt = pickle.load(clients_data_encripted)
    for i in clients_data_decrypt:
        rooms_elected += i.room_ubication + ' -- '
        rooms_price += i.room_price
    
    if disease:
        rooms_price_discount += 0.3
    
    if dni % 2 == 0:
        pass
    else:
        rooms_price_discount += 0.10

    count =  1
    suma = 0
    while (count<dni):
        if (dni % count == 0):
            suma += count
        count = count + 1
        if suma > dni:
            abundante = True
        else:
            pass
    if abundante:
        rooms_price_discount += 0.15
    

    if rooms_price_discount > 0:
        discount_total_room = (rooms_price * rooms_price_discount) 
    else:
        discount_total_room = 0

    taxes_price_room = rooms_price * 0.16 
    money_spent = (rooms_price - discount_total_room) + taxes_price_room

    if age > 65:
        if total_family_client > 2:
            print('Una de sus habitaciones ha sido mejorada a la siguiente clase!')
        else:
            print('Su habitacion fue mejorada a la siguiente clase!')
    
    client = Client(dni, name, age, money_spent, disease)
    client_database = open('ClientData.txt', 'a') 
    client_database.write(f'{client.dni}|{client.name}|{client.age}|{client.money_spent}|{client.disease}\n') 
    client_database.close()
    clients_data_encripted.close()
    print()
    print(f'''      //////////////////////////////
    Factura ---> {cruise_name} \n
    Nombre: {name}
    DNI: {dni}
    Habitaciones seleccionadas: {rooms_elected}
    Monto: USD {rooms_price}
    Descuento: USD {discount_total_room}
    Impuestos (16%): USD {taxes_price_room}
    ---------------------------------
    TOTAL A PAGAR ----> USD {money_spent}
    //////////////////////////////''')
    print()
  
    del simple_edlm[:]
    clients_data_encripted = open('RoomsDataBase.txt', 'wb')
    pickle.dump(simple_edlm, clients_data_encripted)
    clients_data_encripted.close()
    return
    
def buy_ticket(cruise_election, clients):
    """Imprime pasillos y habitaciones, registra clientes en dichas habitaciones 
    y almacena los datos 

    Args:

        cruise_election (int): Eleccion del crucero a realizar el registro
    """
    if cruise_election == 1: #TODO El Dios de Los Mares
        cruise_name = 'El Dios de Los Mares'
        while True:
            try:
                room_type = int(input('''Ingrese tipo de habitacion: \n
                1) Simple ---> Puede tener servicio a la habitación >> Capacidad: 2 personas
                                -> Habitaciones sencillas, especiales para parejas \n
                2) Premium ---> Posee vista al mar >> Capacidad: 4 personas
                                -> Habitaciones perfectas para familias \n
                3) VIP ---> Puede albergar fiestas privadas >> Capacidad: 8 personas
                            -> Habitaciones optimas para grupos, promociones, y paquetes familiares grandes
                >> '''))
                print()
                if room_type < 1 or room_type > 3:
                    print('Opcion no valida')
                else:
                    break
            except:
                print('Opcion no valida')
        
        if room_type == 1:
            clients_ubicated = False
            room_simple_coordinates = []
            total_hallway_columns = 10
            total_rooms_row = ['A', 'B', 'C', 'D']

            print('Piso 1 ---> El Dios de Los Mares >> Simple')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_simple_coordinates.append(f'S{total_rooms_row[i]}{j + 1}')
                    print(f'S{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()

            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_simple_coordinates:
                    coordinates_room = open('RoomCoordinatesEDLM.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesEDLM.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 2:
                            simple_room = Room(2, 69.99, 'simple', False, room_election)
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 2 
                        else:
                            simple_room = Room(client_quantity, 69.99, 'simple', False, room_election)
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)
            

        if room_type == 2:
            clients_ubicated = False
            room_premium_coordinates = []
            total_hallway_columns = 9
            total_rooms_row = ['A', 'B', 'C']

            print('Piso 2 ---> El Dios de Los Mares >> Premium')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_premium_coordinates.append(f'P{total_rooms_row[i]}{j + 1}')
                    print(f'P{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()

            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_premium_coordinates:
                    coordinates_room = open('RoomCoordinatesEDLM.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesEDLM.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 4: 
                            simple_room = Room(4, 89.99 , 'premium', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 4 
                        else:
                            simple_room = Room(client_quantity, 89.99, 'premium', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)
          

        if room_type == 3:
            clients_ubicated = False
            room_vip_coordinates = []
            total_hallway_columns = 6
            total_rooms_row = ['A']

            print('Piso 3 ---> El Dios de Los Mares >> VIP')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_vip_coordinates.append(f'V{total_rooms_row[i]}{j + 1}')
                    print(f'V{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()
            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_vip_coordinates: 
                    coordinates_room = open('RoomCoordinatesEDLM.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesEDLM.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 8: 
                            simple_room = Room(8, 129.99 , 'vip', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 8 
                        else:
                            simple_room = Room(client_quantity, 129.99, 'vip', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)

    if cruise_election == 2: #TODO La Reina Isabel 
        cruise_name = 'La Reina Isabel'
        while True:
            try:
                room_type = int(input('''Ingrese tipo de habitacion: \n
                1) Simple ---> Puede tener servicio a la habitación >> Capacidad: 2 personas
                                -> Habitaciones sencillas, especiales para parejas \n
                2) Premium ---> Posee vista al mar >> Capacidad: 4 personas
                                -> Habitaciones perfectas para familias \n
                3) VIP ---> Puede albergar fiestas privadas >> Capacidad: 8 personas
                            -> Habitaciones optimas para grupos, promociones, y paquetes familiares grandes
                >> '''))
                print()
                if room_type < 1 or room_type > 3:
                    print('Opcion no valida')
                else:
                    break
            except:
                print('Opcion no valida')
        
        if room_type == 1:
            clients_ubicated = False
            room_simple_coordinates = []
            total_hallway_columns = 10
            total_rooms_row = ['A', 'B', 'C', 'D', 'E', 'F']

            print('Piso 1 ---> La Reina Isabel >> Simple')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_simple_coordinates.append(f'S{total_rooms_row[i]}{j + 1}')
                    print(f'S{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()

            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_simple_coordinates:
                    coordinates_room = open('RoomCoordinatesLRI.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesLRI.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 2:
                            simple_room = Room(2, 59.99, 'simple', False, room_election)
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 2 
                        else:
                            simple_room = Room(client_quantity, 59.99, 'simple', False, room_election)
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)
            

        if room_type == 2:
            clients_ubicated = False
            room_premium_coordinates = []
            total_hallway_columns = 8
            total_rooms_row = ['A', 'B', 'C', 'D']

            print('Piso 2 ---> La Reina Isabel >> Premium')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_premium_coordinates.append(f'P{total_rooms_row[i]}{j + 1}')
                    print(f'P{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()

            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_premium_coordinates:
                    coordinates_room = open('RoomCoordinatesLRI.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesLRI.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 4: 
                            simple_room = Room(4, 99.99 , 'premium', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 4 
                        else:
                            simple_room = Room(client_quantity, 99.99, 'premium', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)
          

        if room_type == 3:
            clients_ubicated = False
            room_vip_coordinates = []
            total_hallway_columns = 4
            total_rooms_row = ['A', 'B']

            print('Piso 3 ---> La Reina Isabel >> VIP')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_vip_coordinates.append(f'V{total_rooms_row[i]}{j + 1}')
                    print(f'V{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()
            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_vip_coordinates: 
                    coordinates_room = open('RoomCoordinatesLRI.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesLRI.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 8: 
                            simple_room = Room(8, 119.99 , 'vip', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 8 
                        else:
                            simple_room = Room(client_quantity, 119.99, 'vip', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)

    if cruise_election == 3: #TODO El Libertador Del Oceano
        cruise_name = 'El Libertador del Oceano'
        while True:
            try:
                room_type = int(input('''Ingrese tipo de habitacion: \n
                1) Simple ---> Puede tener servicio a la habitación >> Capacidad: 3 personas
                                -> Habitaciones sencillas, especiales para parejas \n
                2) Premium ---> Posee vista al mar >> Capacidad: 5 personas
                                -> Habitaciones perfectas para familias \n
                3) VIP ---> Puede albergar fiestas privadas >> Capacidad: 12 personas
                            -> Habitaciones optimas para grupos, promociones, y paquetes familiares grandes
                >> '''))
                print()
                if room_type < 1 or room_type > 3:
                    print('Opcion no valida')
                else:
                    break
            except:
                print('Opcion no valida')
        
        if room_type == 1:
            clients_ubicated = False
            room_simple_coordinates = []
            total_hallway_columns = 8
            total_rooms_row = ['A', 'B', 'C', 'D', 'E', 'F']

            print('Piso 1 ---> El Libertador del Oceano >> Simple')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_simple_coordinates.append(f'S{total_rooms_row[i]}{j + 1}')
                    print(f'S{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()

            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_simple_coordinates:
                    coordinates_room = open('RoomCoordinatesERO.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesERO.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 3:
                            simple_room = Room(3, 49.99, 'simple', False, room_election)
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 3 
                        else:
                            simple_room = Room(client_quantity, 49.99, 'simple', False, room_election)
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)
            

        if room_type == 2:
            clients_ubicated = False
            room_premium_coordinates = []
            total_hallway_columns = 6
            total_rooms_row = ['A', 'B', 'C', 'D']

            print('Piso 2 ---> El Libertador del Oceano >> Premium')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_premium_coordinates.append(f'P{total_rooms_row[i]}{j + 1}')
                    print(f'P{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()

            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_premium_coordinates:
                    coordinates_room = open('RoomCoordinatesERO.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesERO.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 5: 
                            simple_room = Room(5, 89.99 , 'premium', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 5 
                        else:
                            simple_room = Room(client_quantity, 89.99, 'premium', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)
          

        if room_type == 3:
            clients_ubicated = False
            room_vip_coordinates = []
            total_hallway_columns = 2
            total_rooms_row = ['A', 'B', 'C', 'D']

            print('Piso 3 ---> El Libertador del Oceano >> VIP')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_vip_coordinates.append(f'V{total_rooms_row[i]}{j + 1}')
                    print(f'V{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()
            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_vip_coordinates: 
                    coordinates_room = open('RoomCoordinatesERO.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesERO.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 12: 
                            simple_room = Room(12, 139.99 , 'vip', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 12 
                        else:
                            simple_room = Room(client_quantity, 139.99, 'vip', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)

    if cruise_election == 4: #TODO Sabas Nieves
        cruise_name = 'Sabas Nieves'
        while True:
            try:
                room_type = int(input('''Ingrese tipo de habitacion: \n
                1) Simple ---> Puede tener servicio a la habitación >> Capacidad: 3 personas
                                -> Habitaciones sencillas, especiales para parejas \n
                2) Premium ---> Posee vista al mar >> Capacidad: 5 personas
                                -> Habitaciones perfectas para familias \n
                3) VIP ---> Puede albergar fiestas privadas >> Capacidad: 10 personas
                            -> Habitaciones optimas para grupos, promociones, y paquetes familiares grandes
                >> '''))
                print()
                if room_type < 1 or room_type > 3:
                    print('Opcion no valida')
                else:
                    break
            except:
                print('Opcion no valida')
        
        if room_type == 1:
            clients_ubicated = False
            room_simple_coordinates = []
            total_hallway_columns = 12
            total_rooms_row = ['A', 'B', 'C', 'D']

            print('Piso 1 ---> Sabas Nieves >> Simple')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_simple_coordinates.append(f'S{total_rooms_row[i]}{j + 1}')
                    print(f'S{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()

            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_simple_coordinates:
                    coordinates_room = open('RoomCoordinatesSN.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesSN.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 3:
                            simple_room = Room(3, 59.99, 'simple', False, room_election)
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 3 
                        else:
                            simple_room = Room(client_quantity, 59.99, 'simple', False, room_election)
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)
            

        if room_type == 2:
            clients_ubicated = False
            room_premium_coordinates = []
            total_hallway_columns = 7
            total_rooms_row = ['A', 'B', 'C']

            print('Piso 2 ---> Sabas Nieves >> Premium')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_premium_coordinates.append(f'P{total_rooms_row[i]}{j + 1}')
                    print(f'P{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()

            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_premium_coordinates:
                    coordinates_room = open('RoomCoordinatesSN.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesSN.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 5: 
                            simple_room = Room(5, 99.99 , 'premium', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 5 
                        else:
                            simple_room = Room(client_quantity, 99.99, 'premium', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)
          

        if room_type == 3:
            clients_ubicated = False
            room_vip_coordinates = []
            total_hallway_columns = 4
            total_rooms_row = ['A', 'B']

            print('Piso 3 ---> Sabas Nieves >> VIP')
            for i in range(len(total_rooms_row)):
                for j in range(total_hallway_columns):
                    room_vip_coordinates.append(f'V{total_rooms_row[i]}{j + 1}')
                    print(f'V{total_rooms_row[i]}{j + 1}  ', end ='', sep = '\t')
                print()
            while True:
                try:
                    client_quantity = int(input('Ingrese cantidad de personas a hospedar: '))
                    total_family_client = client_quantity
                    break
                except:
                    print('Opcion no valida')
            while clients_ubicated == False:
                room_election = input('Ingrese la coordenada de la habitacion que desea: ').upper()
                if room_election in room_vip_coordinates: 
                    coordinates_room = open('RoomCoordinatesSN.txt', 'r')
                    coordinates_room.seek(0)
                    if room_election in coordinates_room.read():
                        print('Habitacion ocupada, escoja otra')
                    else:    
                        coordinates_room = open('RoomCoordinatesSN.txt', 'a') 
                        coordinates_room.write(room_election)
                        coordinates_room.write('\n')
                        coordinates_room.close()
                        if client_quantity > 10: 
                            simple_room = Room(10, 119.99 , 'vip', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            print('Capacidad de habitacion alcanzada. Elija otra para las personas restantes')
                            client_quantity -= 10
                        else:
                            simple_room = Room(client_quantity, 119.99, 'vip', False, room_election) 
                            simple_edlm.append(simple_room)
                            simple_database = open('RoomsDataBase.txt', 'wb') 
                            pickle.dump(simple_edlm, simple_database)
                            simple_database.close()
                            clients_ubicated = True
                else:
                    print('Habitacion no existente')
            
            ticket_invoice(total_family_client, clients, cruise_name)

def introduction(clients):
    """Ordena el tipo de busqueda preferido por el cliente

    """
    cruises = CruiseManagement
    while True:
        try:
            ship_election = int(input('''Ingrese Opcion:
            1) Elegir Boleto por Destino
            2) Elegir Boleto por Crucero
            3) Salir 
            >> '''))
            if ship_election < 1 or ship_election > 2:
                print('Opcion no valida')
            else:
                break
        except:
            print('Opcion no valida')
    
    if ship_election == 1:
        print('Destinos de nuestros Cruceros: ')
        for i,j in enumerate(cruises.cruise_api()):
            for x in j['route']:
                destination = x
            print(f'''{i+1}) {destination}''')
        
        while True:
            try:
                cruise_election = int(input('Ingrese el Crucero de su preferencia: '))
                if cruise_election < 1 or cruise_election > 4:
                    print('Opcion no valida')
                else:
                    break
            except:
                print('Opcion no valida')
        buy_ticket(cruise_election, clients)

    elif ship_election == 2:
        cruise_name = ''
        print('Nombres de Nuestros Cruceros: ')
        for i,j in enumerate(cruises.cruise_api()):
            cruise_name = j['name']
            print(f"{i+1}) {cruise_name}")

        while True:
            try:
                cruise_election = int(input('Ingrese el Crucero de su preferencia: '))
                if cruise_election < 1 or cruise_election > 4:
                    print('Opcion no valida')
                else:
                    break
            except:
                print('Opcion no valida')
        buy_ticket(cruise_election, clients)    

    elif ship_election == 3:
        return

def room_menu(clients):
    """Da inicio al modulo de registro, busca y desocupa habitaciones
    """
    while True:
        try:
            menu_room_election = int(input('''Ingrese Opcion: 
            1) Vender Habitacion
            2) Desocupar Habitacion
            3) Buscar Habitacion
            4) Salir
            >> '''))
            if menu_room_election < 1 or menu_room_election > 4:
                print('Opcion no valida')
            else:
                break
        except:
            print('Opcion no valida')
    if menu_room_election == 1:
        introduction(clients)
    elif menu_room_election == 2:
        new_room_coordinates = []
        room_edlm = ''
        room_lri = ''
        room_ero = ''
        room_sn = ''
        while True:
            try:
                ship_delete_election = int(input('''Ingrese numero del barco de la habitacion a desocupar: 
                1) El Dios de Los Mares
                2) La Reina Isabel
                3) El Libertador del Oceano
                4) Sabas Nieves'''))
                if ship_delete_election < 1 or ship_delete_election > 4:
                    print('Opcion no valida')
                else:
                    break
            except:
                print('Opcion no valida')

        
        if ship_delete_election == 1:
            data_delete_room = open('RoomCoordinatesEDLM.txt', 'r')
            data_delete_room.seek(0)
            for i in data_delete_room.readlines():
                room_edlm += '>> ' + i 
            print(f'''Las Habitaciones de El Dios De Los Mares ocupadas son: 

{room_edlm}''')
            data_delete_room.close()    
            room_delete_election = input('Ingrese habitacion a desocupar: ').upper()
            room_delete_election = room_delete_election + '\n'
            data_delete_room = open('RoomCoordinatesEDLM.txt', 'r')
            data_delete_room.seek(0)
            if room_delete_election in data_delete_room.read():
                data_delete_room = open('RoomCoordinatesEDLM.txt', 'r')
                for x in data_delete_room.readlines():
                    new_room_coordinates.append(x)
                data_delete_room.close()
                new_room_coordinates.remove(room_delete_election)
                data_delete_room = open('RoomCoordinatesEDLM.txt', 'w')
                for t in new_room_coordinates:
                    data_delete_room.write(t)
                    print('Habitacion desocupada!')
                    data_delete_room.close()
                    del new_room_coordinates[:]
            else:
                print('Habitacion desocupada!')

        elif ship_delete_election == 2:
            data_delete_room = open('RoomCoordinatesLRI.txt', 'r')
            data_delete_room.seek(0)
            for i in data_delete_room.readlines():
                room_lri += '>> ' + i
            print(f'''Las Habitaciones de La Reina Isabel ocupadas son: 

{room_lri}''')
            data_delete_room.close()    
            room_delete_election = input('Ingrese habitacion a desocupar: ').upper()
            room_delete_election = room_delete_election + '\n'
            data_delete_room = open('RoomCoordinatesLRI.txt', 'r')
            data_delete_room.seek(0)
            if room_delete_election in data_delete_room.read():
                data_delete_room = open('RoomCoordinatesLRI.txt', 'r')
                for x in data_delete_room.readlines():
                    new_room_coordinates.append(x)
                data_delete_room.close()
                new_room_coordinates.remove(room_delete_election)
                data_delete_room = open('RoomCoordinatesLRI.txt', 'w')
                for t in new_room_coordinates:
                    data_delete_room.write(t)
                    print('Habitacion desocupada!')
                    data_delete_room.close()
                    del new_room_coordinates[:]
            else:
                print('Habitacion desocupada!')

        elif ship_delete_election == 3:
            data_delete_room = open('RoomCoordinatesERO.txt', 'r')
            data_delete_room.seek(0)
            for i in data_delete_room.readlines():
                room_ero += '>> ' + i 
            print(f'''Las Habitaciones de El Libertador Del Oceano ocupadas son: 

{room_ero}''')
            data_delete_room.close()    
            room_delete_election = input('Ingrese habitacion a desocupar: ').upper()
            room_delete_election = room_delete_election + '\n'
            data_delete_room = open('RoomCoordinatesERO.txt', 'r')
            data_delete_room.seek(0)
            if room_delete_election in data_delete_room.read():
                data_delete_room = open('RoomCoordinatesERO.txt', 'r')
                for x in data_delete_room.readlines():
                    new_room_coordinates.append(x)
                data_delete_room.close()
                new_room_coordinates.remove(room_delete_election)
                data_delete_room = open('RoomCoordinatesERO.txt', 'w')
                for t in new_room_coordinates:
                    data_delete_room.write(t)
                    print('Habitacion desocupada!')
                    data_delete_room.close()
                    del new_room_coordinates[:]
            else:
                print('Habitacion desocupada!')

        elif ship_delete_election == 4:
            data_delete_room = open('RoomCoordinatesSN.txt', 'r')
            data_delete_room.seek(0)
            for i in data_delete_room.readlines():
                room_sn += '>> ' + i 
            print(f'''Las Habitaciones de Sabas Nueves ocupadas son: 

{room_sn}''')
            data_delete_room.close()    
            room_delete_election = input('Ingrese habitacion a desocupar: ').upper()
            room_delete_election = room_delete_election + '\n'
            data_delete_room = open('RoomCoordinatesSN.txt', 'r')
            data_delete_room.seek(0)
            if room_delete_election in data_delete_room.read():
                data_delete_room = open('RoomCoordinatesSN.txt', 'r')
                for x in data_delete_room.readlines():
                    new_room_coordinates.append(x)
                data_delete_room.close()
                new_room_coordinates.remove(room_delete_election)
                data_delete_room = open('RoomCoordinatesSN.txt', 'w')
                for t in new_room_coordinates:
                    data_delete_room.write(t)
                    print('Habitacion desocupada!')
                    data_delete_room.close()
                    del new_room_coordinates[:]
            else:
                print('Habitacion desocupada!')


    elif menu_room_election == 3: 
        introduction(clients)

    elif menu_room_election == 4:
        return

