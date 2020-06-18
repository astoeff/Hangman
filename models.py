class Word:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class PremiumPlayer(Player):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return self.name + ' ' + str(self.age)
