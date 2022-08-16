class Actor:
    def __init__(self, first_name, last_name, salary, phrase):
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = salary
        self.phrase = phrase

    def print_phrase(self):
        print(f'{self.phrase}')

    def tip_actor(self, tip):
        if tip % 2 == 1 or self.__salary < 1000:
            self.__salary += tip

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.phrase}, {self.__salary}'


joey = Actor('joey', 'tribiani', 2000, 'How you doin ? ')
lior = Actor('lior', 'ashkinazi', 800, 'talooy')

joey.__salary += 4000
print(joey.__salary)

print(joey)
