import requests

def cruise_api():
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'

    response = requests.request("GET", url)
    return(response.json())

def search_cruise(): #TODO Imprimir almacenando en variables los keys del diccionario
    cruises = cruise_api()
    for i,j in enumerate(cruises):
        route = 'Ruta: '
        room_class = ''
        room_price = ''
        room_location = ''
        room_capacity = ''
        for x in j['route']:
            route += ' - ' + x 

        for k,l in j['cost'].items():
            room_class +=f"- {k} ---> Precio:  USD {l} \n \t \t"
        
        for n,m in j['rooms'].items():
            room_location += f"- {n} ---> Pasillos: {m[0]} Habitaciones por Pasillo: {m[1]} \n \t \t" 
        
        for r,e in j['capacity'].items():
                room_capacity += ( f"- {r} ---> Personas: {e} \n \t \t")

        cruise = j['name']
        departure = j['departure']

        print(f'''{i+1}) Crucero: {cruise}
        >> {route}
        >> Horario de Salida: {departure}
        >> Tipo de Habitaciones: 
                {room_class}
        >> Cantidad de Habitaciones 
                {room_location}
        >> Capacidad por Habitacion:
                {room_capacity}''') #TODO FALTA CONTINUAR DONDE NOS QUEDAMOS EN PASILLOS/HABITACIONES


def introduction():
    search_cruise()