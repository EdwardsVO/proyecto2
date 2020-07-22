from Client import Client
import pickle
import RestaurantManagement
import TourManagement
import CruiseManagement
import RoomManagement
import Statistics

#TODO RECORDAR DOCSTRING DE LAS FUNCIONES 
def main_menu(restaurant, menu, menu_combo, tours, clients, cruise, rooms, statistics):
    while True:
        while True:
            try:
                module_selection = int(input('''Ingrese opcion:
                1) Ver cruseros 
                2) Comprar habitaciones
                3) Comprar Tour
                4) Ver Restaurante
                5) Obtener Estadisticas
                6) Salir
                >> '''))
                break
            except:
                print('Opcion no valida')

        if module_selection == 1: 
            cruise.introduction()

        elif module_selection == 2:  
            rooms.room_menu(clients)
            return main_menu(restaurant, menu, menu_combo, tours, clients, cruise, rooms, statistics)

        elif module_selection == 3: 
            tours.tour_introduction(clients)
            return main_menu(restaurant, menu, menu_combo, tours, clients, cruise, rooms, statistics) 

        elif module_selection == 4: 
            restaurant.introduction(restaurant, menu, menu_combo, clients) 
            return main_menu(restaurant, menu, menu_combo, tours, clients, cruise, rooms, statistics) 

        elif module_selection == 5: 
            statistics.statistics()
            return main_menu(restaurant, menu, menu_combo, tours, clients, cruise, rooms, statistics)

        elif module_selection == 6:
            print('Nos vemos pronto! ')
            break

def main():

    cruise = CruiseManagement
    restaurant = RestaurantManagement
    tours = TourManagement
    rooms = RoomManagement
    statistics = Statistics
    menu = []
    menu_combo = {}
    clients = []
    

    print('\\\BIENVENIDO A SAMANCARIBBEAN///')
    
    main_menu(restaurant, menu, menu_combo, tours, clients, cruise, rooms, statistics)


if __name__ == "__main__":
    main()