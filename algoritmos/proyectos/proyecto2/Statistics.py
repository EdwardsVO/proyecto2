import requests
import operator
import numpy as np
import matplotlib.pyplot as plt

clients = []
clients_spents = []
clients_buy_tours = []
clients_in_edlm = []
clients_in_lri = []
clients_in_ero = []
clients_in_sn = []
graph_clients = []
cruises_tickets = {}
food_sells_edlm = {}
food_sells_lri = {}
food_sells_ero = {}
food_sells_sn = {}
graph_food_1 = []
graph_food_2 = []
graph_food_3 = []
graph_food_4 = []


def printed_statistics(message_client_spent, message_percentage, message_faithful_clients, message_cruises_tickets):
    print(f'''  
    //////////////////////////////////////////

                    ESTADISTICAS    

  --> {message_client_spent}\n
  --> {message_percentage}\n
  --> {message_faithful_clients}\n
  --> {message_cruises_tickets}\n
  --> TOP 5 Ventas De Los Restaurantes en los cruceros(Mayor a menor)''')
  
    print('         ~ El Dios de Los Mares:')
    cruise_sells_edlm = sorted(food_sells_edlm.items(), key=operator.itemgetter(1), reverse=True)
    for name in enumerate(cruise_sells_edlm):
        print(f'            >> {name[1][0]}: Ventas --> {food_sells_edlm[name[1][0]]}')
        graph_food_1.append(food_sells_edlm[name[1][0]])
    print()
    x = graph_food_1
    food_number = [1,2,3,4,5]
    plt.plot(food_number, x)
    plt.xlabel('Productos')
    plt.ylabel('Ventas')
    plt.title('Productos mas vendidos: El Dios De Los Mares')
    plt.draw()
    plt.savefig('GraficoFood1', dpi = 300)
    plt.close()
    plt.show()
    del graph_food_1[:]

    print('         ~ La Reina Isabel:')
    cruise_sells_lri = sorted(food_sells_lri.items(), key=operator.itemgetter(1), reverse=True)
    for name in enumerate(cruise_sells_lri):
        print(f'            >> {name[1][0]}: Ventas --> {food_sells_lri[name[1][0]]}')
        graph_food_2.append(food_sells_lri[name[1][0]])
    print()
    x = graph_food_2
    food_number = [1,2,3,4,5]
    plt.plot(food_number, x)
    plt.xlabel('Productos')
    plt.ylabel('Ventas')
    plt.title('Productos mas vendidos: La Reina Isabel')
    plt.draw()
    plt.savefig('GraficoFood2', dpi = 300)
    plt.close()
    plt.show()
    del graph_food_2[:]

    print('         ~ El Libertador del Oceano:')
    cruise_sells_ero = sorted(food_sells_ero.items(), key=operator.itemgetter(1), reverse=True)
    for name in enumerate(cruise_sells_ero):
        print(f'            >> {name[1][0]}: Ventas --> {food_sells_ero[name[1][0]]}')
        graph_food_3.append(food_sells_ero[name[1][0]])
    print()
    x = graph_food_3
    food_number = [1,2,3,4,5]
    plt.plot(food_number, x)
    plt.xlabel('Productos')
    plt.ylabel('Ventas')
    plt.title('Productos mas vendidos: El Libertador del Oceano')
    plt.draw()
    plt.savefig('GraficoFood3', dpi = 300)
    plt.close()
    plt.show() 
    del graph_food_3[:]
    print('         ~ Sabas Nieves:')
    cruise_sells_sn = sorted(food_sells_sn.items(), key=operator.itemgetter(1), reverse=True)
    for name in enumerate(cruise_sells_sn):
        print(f'            >> {name[1][0]}: Ventas --> {food_sells_sn[name[1][0]]}')
        graph_food_4.append(food_sells_sn[name[1][0]])
    print()
    x = graph_food_4
    food_number = [1,2,3,4,5]
    plt.plot(food_number, x)
    plt.xlabel('Productos')
    plt.ylabel('Ventas')
    plt.title('Productos mas vendidos: Sabas Nieves')
    plt.draw()
    plt.savefig('GraficoFood4', dpi = 300)
    plt.close()
    plt.show()
    del graph_food_4[:]
    print()
    print('*Se han generado y guardado todas las graficas*')
    print()
    print('                 GRACIAS POR TODO !!')
    print('     //////////////////////////////////////////\n')

    

def cruise_api():
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'

    response = requests.request("GET", url)
    return(response.json())

def statistics():
    try:
        client = open('ClientData.txt', 'r')
        for i in client.readlines():
            clients_spents.append(float(i.split('|')[3]))
            clients.append(i)
        client.close()
        if len(clients_spents) or len(clients) > 0: 
            spents_average = sum(clients_spents) / len(clients)
            message_client_spent = f'El promedio de gasto de un cliente es de USD {spents_average}'
        else:
            message_client_spent = 'ERROR: No se han registrado clientes aun'    
    except:
        message_client_spent = 'ERROR: No se han Registrado clientes aun' 
    del clients_spents[:] 
    del clients[:] 

    try:
        client = open('ToursClientsDni.txt', 'r')
        for i in client.readlines():
            i = int(i)
            if i not in clients_buy_tours:
                clients_buy_tours.append(i)
        client.close()
        client_update = open('ClientData.txt', 'r')
        for j in client_update.readlines():
            clients.append(i)
        client_update.close()
        not_buy = len(clients) - len(clients_buy_tours)
        percentage = (not_buy * 100) / len(clients)
        message_percentage = f'El {percentage}% de los clientes no compro un tour' 
    except:
        message_percentage = "El 100% de lo clientes no compraron un tour" 
        
    del clients_buy_tours[:] 
    del clients[:]  

    try:
        client = open('ClientData.txt', 'r')
        for k in client.readlines():
            clients_spents.append(float(k.split('|')[3]))
        clients_spents_sorted = sorted(clients_spents)
        graph_clients.append(float(clients_spents_sorted[-3]))
        graph_clients.append(float(clients_spents_sorted[-2]))
        graph_clients.append(float(clients_spents_sorted[-1])) 
        client.close()

        client_money = open('ClientData.txt', 'r')
        for y in client_money.readlines():
            if str(clients_spents_sorted[-1]) == y.split('|')[3]:
                client_1 = y.split('|')[1]
            if str(clients_spents_sorted[-2]) == y.split('|')[3]:
                client_2 = y.split('|')[1]
            if str(clients_spents_sorted[-3]) == y.split('|')[3]:
                client_3 = y.split('|')[1]

          
        message_faithful_clients = f'''Los clientes mas fieles a la linea fueron:
    1 >> {client_1} --> Gastos => USD {clients_spents_sorted[-1]}
    2 >> {client_2} --> Gastos => USD {clients_spents_sorted[-2]}
    3 >> {client_3} --> Gastos => USD {clients_spents_sorted[-3]}''' 
        x = graph_clients
        client_number = [1,2,3]
        plt.plot(client_number, x)
        plt.xlabel('Clientes')
        plt.ylabel('Gastos USD')
        plt.title('Clientes mas fieles')
        plt.draw()
        plt.savefig('GraficoTOPClients', dpi = 300)
        plt.close()
        plt.show()
    
    except:
        message_faithful_clients = 'ERROR: Deben haber por lo menos tres clientes registrados' 

    try:
        ship_1 = open('RoomCoordinatesEDLM.txt', 'r')
        for t in ship_1.readlines():
            clients_in_edlm.append(t)
        ship_1.close()
    except:
        pass
    
    try:
        ship_2 = open('RoomCoordinatesLRI.txt', 'r')
        for u in ship_2.readlines():
            clients_in_lri.append(u)
        ship_2.close()
    except:
        pass

    try:
        ship_3 = open('RoomCoordinatesERO.txt', 'r')
        for g in ship_3.readlines():
            clients_in_ero.append(g)
        ship_3.close()
    except:
        pass
    try:
        ship_4 = open('RoomCoordinatesSN.txt', 'r')
        for l in ship_4.readlines():
            clients_in_sn.append(l)
        ship_4.close()
    except:
        pass

    cruises_tickets[len(clients_in_edlm)] = 'El Dios De Los Mares'
    cruises_tickets[len(clients_in_lri)] = 'La Reina Isabel'
    cruises_tickets[len(clients_in_ero)] = 'El Libertador del Oceano'
    cruises_tickets[len(clients_in_sn)] = 'Sabas Nieves'
    try:
        cruises_tickets_sorted = sorted(cruises_tickets.items())
        cruise_1 = cruises_tickets_sorted[-1][1]
        cruise_2 = cruises_tickets_sorted[-2][1]
        cruise_3 = cruises_tickets_sorted[-3][1]
        
        message_cruises_tickets = f'''Los cruceros con mas ventas de tickets fueron:
        1 >> {cruise_1}
        2 >> {cruise_2}
        3 >> {cruise_3}''' 

        x = [cruises_tickets_sorted[-3][0], cruises_tickets_sorted[-2][0], cruises_tickets_sorted[-1][0]]
        cruise_number = [1,2,3]
        plt.plot(cruise_number, x)
        plt.xlabel('Cruceros')
        plt.ylabel('Ventas')
        plt.title('Cruceros con mas ventas')
        plt.draw()
        plt.savefig('GraficoTOPCruises', dpi = 300)
        plt.close()
        plt.show()

    except:
        message_cruises_tickets = 'ERROR: No se han comprado suficientes tickets'

    cruise_sells = cruise_api()
    for i,j in enumerate(cruise_sells):
        for t,u in enumerate(j['sells']):     
            if i == 0:
                food_sells_edlm[u['name']] = u['amount']
            if i == 1:
                food_sells_lri[u['name']] = u['amount']
            if i == 2:
                food_sells_ero[u['name']] =u['amount']
            if i == 3:
                food_sells_sn[u['name']] = u['amount']

    
    printed_statistics(message_client_spent, message_percentage, message_faithful_clients, message_cruises_tickets)
    

