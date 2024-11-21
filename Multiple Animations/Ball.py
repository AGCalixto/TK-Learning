class Ball:
    def __init__(self, canvas, x: int, y: int, diameter: int, xSpeed: int, ySpeed: int, color: str):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def move(self):
        Coordinates = self.canvas.coords(self.image)
        if Coordinates[2] >= self.canvas.winfo_width() or Coordinates[0] < 0:
            self.xSpeed = -self.xSpeed
        if Coordinates[3] >= self.canvas.winfo_height() or Coordinates[1] < 0:
            self.ySpeed = - self.ySpeed

        self.canvas.move(self.image, self.xSpeed, self.ySpeed)

