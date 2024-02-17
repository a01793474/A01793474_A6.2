""" Program to create hotel reservations """
import os
import json

HOTELID = 1
CLIENTID = 1


def validate_json(json_data):
    """ Validate if file is json"""
    try:
        json.loads(json_data)
    except ValueError:
        return False
    return True


class Hotel:
    """ class hotel"""

    def __init__(self, idh, name, rooms, available):
        """ Constructor hotel"""
        self.idh = idh
        self.name = name
        self.rooms = rooms
        self.available = available

    def create_hotel(self, idh, name, rooms, available):
        """ Method to create new hotel"""
        file_name = "Hotels.json"
        if os.path.isfile(file_name):
            found = []
            with open(file_name, "r", encoding='utf-8') as read_file:
                hotels = json.load(read_file)

                for i, _ in enumerate(hotels):
                    hotels[i] = dict(hotels[i])
                    searchhotels = list(hotels[i].values())

                    if searchhotels[0] == idh and idh > 0:
                        found.append(hotels[i])
                    elif searchhotels[1] == name and len(name) != 0:
                        found.append(hotels[i])

            if found:
                print("Hotel ya existe")
                return False

        global HOTELID
        data = {"id": HOTELID,
                "name": name,
                "rooms": rooms,
                "available": available
                }

        HOTELID = HOTELID+1

        json_data = json.dumps(data)
        a = []

        if validate_json(json_data):
            if not os.path.isfile(file_name):
                a.append(data)
                with open(file_name, mode='w', encoding='utf-8') as f:
                    f.write(json.dumps(a, indent=2))
            else:
                with open(file_name, encoding='utf-8') as feedsjson:
                    feeds = json.load(feedsjson)

                feeds.append(data)
                with open(file_name, mode='w', encoding='utf-8') as f:
                    f.write(json.dumps(feeds, indent=2))

                print("Hotel Created")
                return True
        else:
            print("Error in json file creation")
            return False
        
        return True

    def display_hotel(self, idh=0, name=''):
        """Method to show information of hotel
            accepts id or name of hotel
            returns id if found"""

        file_name = "Hotels.json"
        if not os.path.isfile(file_name):
            print("No se han creado hoteles")
            return False

        with open(file_name, "r", encoding='utf-8') as read_file:
            hotels = json.load(read_file)

            found = []

            for i, _ in enumerate(hotels):
                hotels[i] = dict(hotels[i])
                searchhotels = list(hotels[i].values())

                if searchhotels[0] == idh and idh > 0:
                    found.append(hotels[i])
                elif searchhotels[1] == name and len(name) != 0:
                    found.append(hotels[i])

        if not found:
            print("No se encontraron datos")
            return False

        return found[0]

    def delete_hotel(self, idh=0, name=''):
        """ Method to delete hotel accepts id or name of hotel"""
        a = []
        file_name = "Hotels.json"
        if not os.path.isfile(file_name):
            print("No se han creado hoteles")
            return False

        with open(file_name, "r", encoding='utf-8') as read_file:
            hotels = json.load(read_file)
            found = []

            for i, _ in enumerate(hotels):
                hotels[i] = dict(hotels[i])
                searchhotels = list(hotels[i].values())

                if searchhotels[0] == idh and idh > 0:
                    found.append(hotels[i])
                elif searchhotels[1] == name and len(name) != 0:
                    found.append(hotels[i])
                else:
                    a.append(hotels[i])

            if not found:
                print("No se encontraron datos")
                return False

            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(a, indent=2))

            print(f'Se han borrado {len(found)} registros')
            return True

    def reserve_room_hotel(self, idh=0, name=''):
        """ Method to reserve a room hotel accepts id or name of hotel"""
        a = []
        file_name = "Hotels.json"
        if not os.path.isfile(file_name):
            print("No se han creado hoteles")
            return False

        with open(file_name, "r", encoding='utf-8') as read_file:
            hotels = json.load(read_file)
            found = []

            for i, _ in enumerate(hotels):
                hotels[i] = dict(hotels[i])
                searchhotels = list(hotels[i].values())

                if searchhotels[0] == idh and idh > 0:

                    if hotels[i]["available"] == 0:
                        print("No hay cuartos disponibles")
                        return False

                    hotels[i]["available"] = hotels[i]["available"]-1
                    a.append(hotels[i])
                    found.append(hotels[i])
                elif searchhotels[1] == name and len(name) != 0:
                    a.append(hotels[i])
                    found.append(hotels[i])
                else:
                    a.append(hotels[i])

            if not found:
                print("No se encontraron datos")
                return False

            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(a, indent=2))

            print('Se ha realizado la reserva')
            return True

    def cancel_room_hotel(self, idh=0, name=''):
        """Method to cancel reserve a room hotel
            accepts id or name of hotel"""
        a = []
        file_name = "Hotels.json"
        if not os.path.isfile(file_name):
            print("No se han creado hoteles")
            return False

        with open(file_name, "r", encoding='utf-8') as read_file:
            hotels = json.load(read_file)

            found = []

            for i, _ in enumerate(hotels):
                hotels[i] = dict(hotels[i])
                searchhotels = list(hotels[i].values())

                if searchhotels[0] == idh and idh > 0:

                    if hotels[i]["available"] == hotels[i]["rooms"]:
                        print("No hay reserva que cancelar")
                        return False

                    hotels[i]["available"] = hotels[i]["available"]+1
                    a.append(hotels[i])
                    found.append(hotels[i])
                elif searchhotels[1] == name and len(name) != 0:
                    a.append(hotels[i])
                    found.append(hotels[i])
                else:
                    a.append(hotels[i])

            if not found:
                print("No se encontraron datos")
                return False

            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(a, indent=2))

            print('Se ha cancelado la reserva')
        return True

    def modify_hotel(self, name, rooms, available, idh):
        """ Method to modify a hotel requires id of hotel"""
        a = []
        file_name = "Hotels.json"
        if not os.path.isfile(file_name):
            print("No se han creado hoteles")
            return False

        with open(file_name, "r", encoding='utf-8') as read_file:
            hotels = json.load(read_file)
            found = []

            for i, _ in enumerate(hotels):
                hotels[i] = dict(hotels[i])
                searchhotels = list(hotels[i].values())

                if searchhotels[0] == idh and idh > 0:

                    hotels[i]["name"] = name
                    hotels[i]["rooms"] = rooms
                    hotels[i]["available"] = available
                    a.append(hotels[i])
                    found.append(hotels[i])
                else:
                    a.append(hotels[i])

            if not found:
                print("No se encontraron datos")
                return False

            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(a, indent=2))

            print('Se ha realizado el ajuste')
            return True


class Customer:
    """ class Customer"""
    def __init__(self, idc, name, people, daysofstay):
        """ Constructor Customer"""
        self.idc = idc
        self.name = name
        self.people = people
        self.daysofstay = daysofstay

    def create_customer(self, idc, name, people, daysofstay):
        """Method to create new customer"""
        file_name = "Customer.json"
        if os.path.isfile(file_name):
            found = []
            with open(file_name, "r", encoding='utf-8') as read_file:
                customer = json.load(read_file)

                for i, _ in enumerate(customer):
                    customer[i] = dict(customer[i])
                    searchhotels = list(customer[i].values())

                    if searchhotels[0] == idc and idc > 0:
                        found.append(customer[i])
                    elif searchhotels[1] == name and len(name) != 0:
                        found.append(customer[i])

            if found:
                print("Persona ya existe")
                return False

        global CLIENTID

        data = {"id": CLIENTID,
                "name": name,
                "people": people,
                "daysofstay": daysofstay
                }

        CLIENTID = CLIENTID+1

        json_data = json.dumps(data)
        a = []

        if validate_json(json_data):
            if not os.path.isfile(file_name):
                a.append(data)
                with open(file_name, mode='w', encoding='utf-8') as f:
                    f.write(json.dumps(a, indent=2))
            else:
                with open(file_name, encoding='utf-8') as feedsjson:
                    feeds = json.load(feedsjson)

                feeds.append(data)
                with open(file_name, mode='w', encoding='utf-8') as f:
                    f.write(json.dumps(feeds, indent=2))

                print("Persona Creada")
                return True
        else:
            print("Error in json file creation")
            return False

        return True

    def display_customer(self, idc=0, name=''):
        """Method to show information of customer
            accepts id or name of customer
            returns id if found"""

        file_name = "Customer.json"
        if not os.path.isfile(file_name):
            print("No se han creado clientes")
            return False

        with open(file_name, "r", encoding='utf-8') as read_file:
            customer = json.load(read_file)

            found = []

            for i, _ in enumerate(customer):
                customer[i] = dict(customer[i])
                searchhotels = list(customer[i].values())

                if searchhotels[0] == idc and idc > 0:
                    found.append(customer[i])
                elif searchhotels[1] == name and len(name) != 0:
                    found.append(customer[i])

            if not found:
                print("No se encontraron datos")
                return False

        return found

    def delete_customer(self, idc=0, name=''):
        """ Method to delete customer accepts id or name of customer"""
        a = []
        file_name = "Customer.json"
        if not os.path.isfile(file_name):
            print("No se han creado hoteles")
            return False

        with open(file_name, "r", encoding='utf-8') as read_file:
            customer = json.load(read_file)

            found = []

            for i, _ in enumerate(customer):
                customer[i] = dict(customer[i])
                searchhotels = list(customer[i].values())

                if searchhotels[0] == idc and idc > 0:
                    found.append(customer[i])
                elif searchhotels[1] == name and len(name) != 0:
                    found.append(customer[i])
                else:
                    a.append(customer[i])

            if not found:
                print("No se encontraron datos")
                return False

            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(a, indent=2))

            print(f'Se han borrado {len(found)} registros')
            return True

    def modify_customer(self, name, people, daysofstay, idc):
        """Method to modify a customer requires id of customer"""
        a = []
        file_name = "Customer.json"

        if not os.path.isfile(file_name):
            print("No se han creado hoteles")
            return False

        with open(file_name, "r", encoding='utf-8') as read_file:
            customer = json.load(read_file)

            found = []

            for i, _ in enumerate(customer):
                customer[i] = dict(customer[i])
                searchhotels = list(customer[i].values())

                if searchhotels[0] == idc and idc > 0:

                    customer[i]["name"] = name
                    customer[i]["people"] = people
                    customer[i]["daysofstay"] = daysofstay
                    a.append(customer[i])
                    found.append(customer[i])
                else:
                    a.append(customer[i])

            if not found:
                print("No se encontraron datos")
                return False

            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write(json.dumps(a, indent=2))

            print('Se ha realizado el ajuste')
            return True


class Reservation:
    """Class Reservation"""
    def __init__(self, idhotel, name, people, daysofstay):
        self.idhotel = idhotel
        self.name = name
        self.people = people
        self.daysofstay = daysofstay

    def create_reservation(self, idhotel, name, people, daysofstay):
        """Method to create new reservation
            with Hotel and Customer class
            accepts hotel id , name of customer,
            people for the reservation
            and days of stay"""
        if not Hotel.display_hotel(None, idh=idhotel):
            print("El hotel no existe")
            return False

        if Customer.display_customer(None, name=name):
            Customer.modify_customer(None,
                                     Customer.display_customer(None, name=name),
                                     name,
                                     people,
                                     daysofstay
                                     )
            print("el cliente ya existe Se ajusta su reserva")
        else:
            Customer.create_customer(None, 0, name, people, daysofstay)

        rooms = round(people/2)

        for i in range(0, rooms):
            Hotel.reserve_room_hotel(None, idh=idhotel)
            print(f"Se ha realizado la reserva {i} correctamente")
        return True

    def cancel_reservation(self, idhotel, name, people):
        """Method to cancel reservation with Hotel and Customer class
            accepts idhotel, customer name and people"""
        if not Hotel.display_hotel(None, idh=idhotel):
            print("El hotel no existe")
            return False

        if not Customer.display_customer(None, name=name):
            print("el cliente no existe")
            return False

        data = Customer.display_customer(None, name=name)
        newpeople = people-dict(data[0])["people"]

        if newpeople >= 0:
            rooms = round(newpeople/2)
        else:
            rooms = round(dict(data[0])["people"]/2)
        print(newpeople)
        for i in range(0, rooms):
            Hotel.cancel_room_hotel(None, idh=idhotel)
            print(f"Se ha ajustado la reserva {i} correctamente")

        return True

