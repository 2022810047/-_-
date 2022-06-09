import collision_dection

# Sprite 클래스 상속 
class Character(Sprite):
    def __init__(self, x, y, width, height, image, jump=False):
        super().__init__(x, y, width, height, image)
        self.jump = jump 

    def hop(self):
        if self.jump == True:
            self.x += 300
