import ExtraCredit_JoeClass as jc

def main():

    print('------- Customer Details -------')
    name = input('Enter name : ')
    address = input('Enter address : ')
    phone = input('Enter phone : ')
    customer = jc.Customer(name, address, phone)
    print()
    print('--------- Car Details ----------')
    make = input('Enter manufacturer : ')
    model = input('Enter car model : ')
    year = int(input('Enter year of manufacture : '))
    car = jc.Car(make, model, year)
    print()
    print('------- Charges Details --------')
    pcharge = float(input('Enter parts charges : '))
    lcharge = float(input('Enter labour charges : '))
    charges = jc.ServiceQuote(pcharge, lcharge)
    print()
    print('\nCustomer Information')
    print(f'Name : {customer.get_name()}\n'
      f'CONTACT INFO : {customer.get_address()}  ({customer.get_phone()})')
    print('\nCar Information')
    print(f'Manufacturer = {car.get_make()}\n'
      f'Model : {car.get_model()}\nYear : {car.get_year()}')
    print('\nCharges Information')
    print(f'Parts Charges : {charges.get_parts_charges()}\n'
      f'Labour Charges : {charges.get_labour_charges()}\n'
      f'Sales Tax : {charges.get_sales_tax()}\n'
      f'Total Charges : {charges.get_total_charges()}')

main()