import RetailltemClass as RC

def main():

    item_1 = RC.Retailltem('jacket', 12 , 59.95)
    item_2 = RC.Retailltem('designer jeans', 40 , 34.95)
    item_3 = RC.Retailltem('shirt', 20 , 24.95)


    print('\nitem #1:\n',item_1.get_item())
    print('\nitem #2:\n',item_2.get_item())
    print('\nitem #3:\n',item_3.get_item())

main()