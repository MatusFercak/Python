import random
import matplotlib.pyplot as plt


class Worker:
    def __init__(self, start_floor, goal_floor):
        self.start_floor = start_floor
        self.goal_floor = goal_floor

    def __str__(self):
        string = f'Start floor: {self.start_floor}\n'
        string += f'End floor: {self.goal_floor}\n'
        return string

    def get_start(self):
        return self.start_floor

    def get_goal(self):
        return self.goal_floor


class Elevator:
    def __init__(self, capacity, current_floor=0):
        self.capacity = capacity
        self.current_floor = current_floor
        self.moving_up = True
        self.passengers = []

    def __str__(self):
        string = f'Capacity: {self.capacity}\n'
        string += f'Current floor: {self.current_floor}\n'
        string += f'Moving up: {self.moving_up}\n'
        string += f'Passangers: {self.passengers}\n'
        string += f'Count: {len(self.passengers)}/{self.capacity}\n'
        return string

    def get_passengers(self):
        return self.passengers

    def get_current_floor(self):
        return self.current_floor

    def move(self):
        if self.moving_up:
            self.current_floor += 1
        else:
            self.current_floor -= 1
        
    def get_passenger_count(self):
        return len(self.passengers)

    def change_direction(self):
        self.moving_up = not self.moving_up
        
    def add_passenger(self, passenger):
        if len(self.passengers) != self.capacity:
            self.passengers.append(passenger)
            return True
        return False

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)

        if self.moving_up and self.get_passenger_count() == 0:
            self.change_direction()


class Building:
    def __init__(self, floor_count, elevator_count, elevator_capacity):
        self.floor_count = floor_count
        self.elevators = []
        for _ in range(elevator_count):
            self.elevators.append(
                Elevator(elevator_capacity))

        self.floors = []
        for _ in range(floor_count):
            self.floors.append([])

    def __str__(self):
        string = f'Floor count: {self.floor_count}\n'

        string += 'Elevators: '
        for i in self.elevators:
            string += '# '
        string += '\n'

        string += 'Floors: \n'
        for i in range(len(self.floors)):
            #print(i)
            string += f'{i} - [{len(self.floors[i])}]'
            
            #print(self.elevators[2])
            for e in self.elevators:
                if i == e.get_current_floor():
                    string += f' [{e.get_passenger_count()}]'
            string += '\n'
        return string

    def add_worker_to_floor(self, worker, floor):
        self.floors[floor].append(worker)

    def is_waiting(self):
        workers = int()
        for i in self.floors[0]:
            if i.get_start() == 0:
                workers += 1

        return True if workers != 0 else False

    def time_step(self):
        for e in self.elevators:
            floor = e.get_current_floor()
            if len(self.floors[floor]) != 0 or e.get_passenger_count() != 0:

                for i in self.floors[floor]:
                    if i.get_start() == floor:
                        e.add_passenger(i)

                for i in e.get_passengers():
                    if i in self.floors[floor]:
                        self.floors[floor].remove(i)

                for i in e.get_passengers():
                    if i.get_goal() == floor:
                        self.add_worker_to_floor(i, floor)

                for i in self.floors[floor]:
                    if i.get_goal() == floor:
                        e.remove_passenger(i)

                e.move()
                if floor == 0:
                    e.moving_up = True
                if floor == self.floor_count-1:
                    e.moving_up = False

                


def simulate_workday(
        number_of_workers, floor_count,
        number_of_elevators, elevator_capacity):
    waiting_counts = []
    bu = Building(floor_count, number_of_elevators, elevator_capacity)
    add_workers = 0
    for i in range(random.randint(1,5)):
        bu.add_worker_to_floor(Worker(0,random.randint(1, floor_count -1)),0)
        add_workers += 1
    bu.time_step()
    
    while add_workers <= number_of_workers or bu.is_waiting():
        if add_workers <= number_of_workers:
            for i in range(random.randint(1,5)):
                bu.add_worker_to_floor(Worker(0,random.randint(1, floor_count -1)),0)
                add_workers += 1
        bu.time_step()
        waiting_counts.append(len(bu.floors[0]))
        print(bu)

    return waiting_counts


def main():
    X = simulate_workday(1000, 10, 10, 4)
    Y = [i for i in range(len(X))]

    plt.plot(Y,X)
    plt.title('Elevators')
    plt.xlabel('Elevetor move')
    plt.ylabel('Workers on the floor 0')
    plt.show()
    


if __name__ == '__main__':
    main()
























