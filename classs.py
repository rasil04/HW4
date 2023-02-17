class Hero:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability


class Hero_super(Hero):
    def __str__(self):
        return f'name is {self.name}\n' \
               f'ability is {self.ability}'

    def prints(self):
        print(f'{self.name}, it is super_hero')

# a = Hero_super('Batman','fly')
# print(a)