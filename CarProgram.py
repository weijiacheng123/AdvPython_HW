import Car as c

def main():
    car_make = input("what's the make of the car?\n")
    car_model = input("what's the car's year model?\n")
    car_speed = print("your speed is 0 now.\n")

    my_car = c.car(car_model,car_make,car_speed)
    print(my_car.get_descriptive_name())

    for i in range(1,6):
        my_car.car_accelerate()
        print('After the ',i,'time(s) acceleration, the current speed is',my_car.get_speed())
        
    for i in range(1,6):
        my_car.car_brake()
        print('After the ',i,'time(s) brake, the current speed is',my_car.get_speed())

main()
