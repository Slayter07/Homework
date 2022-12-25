import random


class Wimen:
    def __init__(self, name='Wimen', job=None, home=None, ):
        self.name = name
        self.money = 100
        self.satiety = 50
        self.gladness = 50
        self.job = job
        self.home = home

    def get_home(self):
        self.home = Home()


    def get_job(self):
        if self.lags.walk():
            pass
        else:
            self.eat()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.buy('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.legs.walk():
            pass
        else:

                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness += self.job.gladness_less
        self.satiety -= 4


    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clear_home(self):
        self.gladness -= 10
        self.home.mess = 0

    def indexes_day(self, day):
        day = f'Today the {day} of {self.name} life'
        print(f'{day:+^50}')
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}")
        print(f'Money = {self.money}')
        print(f'Satiety = {self.satiety}')
        print(f'Gladness = {self.gladness}')
        home_indexes = 'Home indexes'
        print(f'{home_indexes:^50}')
        print(f'Food = {self.home.food}')
        print(f'Mess = {self.home.mess}')

    def is_alive(self):
        if self.gladness <= 0:
            print('Depression')
            return False
        if self.satiety <= 0:
            print('Dead....')
            return False
        if self.money < -200:
            print('Bankrupt...')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.walk is None:
            print(f'I go for a walk {self.walk}')
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job}"
                  f"with salary {self.job.salary}")

        self.indexes_day(day)
        dice = random.randint(1, 4)
        if self.satiety < 10:
            print('I go eat')
            self.eat()
        elif self.gladness < 10:
            if self.home.mess > 15:
                print('I want to chill, but there is si much mess ')
                self.clear_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money < 20:
            print('Start working!')
            self.work()
        elif self.walk.strength < 10:
            print('I need to repair my car')
            self.to_repair()
        elif dice == 1:
            print("Let's chill")
            self.chill()
        elif dice == 2:
            print('Start working')
            self.work()
        elif dice == 3:
            print('Cleaning time')
            self.clear_home()
        elif dice == 4:
            print('Time for treats!')
            self.shopping(manage='delicacies')


class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {'Java': {'salary': 50, "gladness_less": 10},
            'C++': {'salary': 80, "gladness_less": 5},
            'Python': {'salary': 30, "gladness_less": 8},
            'Rust': {'salary': 60, "gladness_less": 6}}

nick = Wimen(name='Nick')

for day in range(1, 8):
    if nick.live(day) == False:
        break