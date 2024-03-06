
class Character:
    level = 0
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2

    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        else:
            print(self.phrase2)
    def setLevel(self, newLevel):
        self.level = newLevel
        print(f"NEW LEVEL: {newLevel}")

kungFuPanda = Character("KungFuPanda", "Skadoosh", "You have been blinded by pure awesomeness!")
spiderman = Character("Spiderman", "My Spider-Sense is tingling", "Your friendly neighbourhood spiderman")

kungFuPanda.speak(1)
kungFuPanda.setLevel(2)
spiderman.speak(2)