class Robot:
    def __init__(self, x, y):
      self.set_position(x,y)

    def get_current_position(self):
        return self.x, self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def can_mount(self, block_position):
        return self.get_current_position() == block_position
    
    def set_position(self, x, y):
        self.x = x
        self.y = y

