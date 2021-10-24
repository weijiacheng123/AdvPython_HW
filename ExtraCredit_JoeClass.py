

class Customer:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


class Car:

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, value):
        self.__make = value

    def set_model(self, value):
        self.__model = value

    def set_year(self, value):
        self.__year = value

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


class ServiceQuote:
    
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labour_charges(self, lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labour_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return 10

    def get_total_charges(self):
        charges = self.__parts_charges + self.__labor_charges
        return charges + charges * self.get_sales_tax() / 100

