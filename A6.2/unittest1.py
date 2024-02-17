"""File to test reserve_system.py"""
import os
import unittest 
from reserve_system import Hotel,Reservation,Customer,CLIENTID,HOTELID

class test_reservations(unittest.TestCase):
    
    def test_create_hotel(self):
        file_name = "Hotels.json"
        if os.path.isfile(file_name):
            self.assertFalse(Hotel.create_hotel(None, 0, "Hotel Mary", 40, 40))
            self.assertFalse(Hotel.create_hotel(None, 0, "Marriot", 40, 40))
        else:
            self.assertTrue(Hotel.create_hotel(None, 0, "Hotel California", 20, 20))
            self.assertTrue(Hotel.create_hotel(None, 0, "Marriot", 35, 35))
            self.assertFalse(Hotel.create_hotel(None, 0, "Marriot", 40, 40))
        
    def test_display_hotel(self):
        self.assertTrue(Hotel.display_hotel(None, name='Marriot'))
        self.assertFalse(Hotel.display_hotel(None, name='Test'))
    
    def test_delete_hotel(self):
        self.assertTrue(Hotel.create_hotel(None, 0, "Hilton", 35, 35))
        self.assertTrue(Hotel.delete_hotel(None, name='Hilton'))
    
    def test_reserve_room_hotel(self):
        self.assertTrue(Hotel.reserve_room_hotel(None, idh=1))
        self.assertTrue(Hotel.cancel_room_hotel(None, idh=1))
        
    def test_modify_hotel(self):
        self.assertTrue(Hotel.modify_hotel(None, idh=1, name="Hotel Mary", available=5, rooms=5))
        self.assertFalse(Hotel.modify_hotel(None, idh=5, name="Hotel Mary", available=5, rooms=5))
        
    def test_full_hotel(self):
        self.assertTrue(Hotel.modify_hotel(None, idh=1, name="Hotel Mary", available=5, rooms=5))
        self.assertTrue(Hotel.reserve_room_hotel(None, idh=1))
        self.assertTrue(Hotel.reserve_room_hotel(None, idh=1))
        self.assertTrue(Hotel.reserve_room_hotel(None, idh=1))
        self.assertTrue(Hotel.reserve_room_hotel(None, idh=1))
        self.assertTrue(Hotel.reserve_room_hotel(None, idh=1))
        self.assertFalse(Hotel.reserve_room_hotel(None, idh=1))
        self.assertTrue(Hotel.modify_hotel(None, idh=1, name="Hotel Mary", available=5, rooms=5))
        
    def test_create_customer(self):
        file_name = "Customer.json"
        if os.path.isfile(file_name):
            self.assertFalse(Customer.create_customer(None, 1, "Juan Perez", 2, 5))
            self.assertFalse(Customer.create_customer(None, 2, "Jasmin Soler", 4, 3))
        else:
            self.assertTrue(Customer.create_customer(None, 1, "Juan Perez", 2, 5))
            self.assertTrue(Customer.create_customer(None, 2, "Jasmin Soler", 4, 3))
            self.assertFalse(Customer.create_customer(None, 3, "Juan Perez", 2, 3))
        
    def test_display_customer(self):
        self.assertTrue(Customer.display_customer(None, name='Juan Perez'))
        self.assertFalse(Customer.display_customer(None, name='Test'))
        
    def test_modify_customer(self):
        self.assertTrue(Customer.modify_customer(None,idc=1,name="Juan Perez",people=2,daysofstay=10))
        
    def test_delete_customer(self):
        self.assertTrue(Customer.create_customer(None, 0, "Pedro Fernandez", 2, 3))
        self.assertTrue(Customer.delete_customer(None, name="Pedro Fernandez"))
        
    def test_create_reservation(self):
        self.assertTrue(Reservation.create_reservation(None, 1, "Jose Jimenes", 4, 4))
        self.assertTrue(Reservation.create_reservation(None, 1, "Juan Perez", 4, 6))
        self.assertTrue(Reservation.cancel_reservation(None, 1, "Juan Perez", 4))
        self.assertFalse(Reservation.cancel_reservation(None, 1, "Jose Angel", 2))
        
if __name__ == '__main__':
    unittest.main()
