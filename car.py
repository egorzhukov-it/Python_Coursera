import os.path
import csv


class BaseCar:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    @staticmethod
    def get_photo_file_ext(self=None, *args):
        if self is None:
            return
        else:
            root_ext = os.path.splitext(*args)
            return root_ext[1]


class Car(BaseCar):
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name,  carrying):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
    def __init__(self, car_type, brand, photo_file_name, body_whl, carrying):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.body_whl = body_whl
        self.body_width = float(0)
        self.body_height = float(0)
        self.body_length = float(0)

    def get_body_volume(self=None):
        if self.body_whl == '':
            self.body_width = float(0)
            self.body_height = float(0)
            self.body_length = float(0)
        else:
            a = []
            for b in self.body_whl.split('x'):
                a.append(b)
            self.body_width = float(a[0])
            self.body_height = float(a[1])
            self.body_length = float(a[2])

        return self.body_width * self.body_length * self.body_height


class SpecMachine(BaseCar):
    def __init__(self, car_type, brand, photo_file_name,  carrying, extra):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        car_list = []
        for row in reader:
            #print(row)
            try:

                for row_list in row:
                    if row_list == 'car':
                        new_car = Car(row[0], row[1], row[2],  row[3], row[5])
                        car_list.append(new_car)
                        #print(new_car.get_photo_file_ext())
                    if row_list == 'truck':
                        new_truck = Truck(row[0], row[1], row[3], row[4], row[5])
                        car_list.append(new_truck)
                        #print(new_truck.get_body_volume())

                    if row_list == 'spec_machine':
                        new_spec_machine = SpecMachine(row[0], row[1], row[3], row[5], row[6])
                        car_list.append(new_spec_machine)
            except ValueError:
                next(reader)

    return car_list

#print(get_car_list('./coursera_week3_cars.csv'))
