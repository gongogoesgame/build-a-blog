class Cat:
    
    def __init__(self, color, name, meow):
        self.color = color
        self.name = name
        self.meow = meow
        self.lives = 9
        
    def meow(self):
        print(self.name + "says: " + self.meow)
        
def main():
    george = Cat("blue", "George", "MROOOOOOOOOOOOWWWW")
    sally = Cat("Brown", "Sally", "mew")
    george.meow()
if __name__ == "__main__":
    main()
    