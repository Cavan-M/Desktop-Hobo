
from PIL import Image, ImageTk


class Tom:
    def __init__(self, parent, x, y):
        self.path = "sprites/tom/"
        self.sprite_number = 0
        self.idle_count = 0
        self.drink_count = 0
        self.walk_count = 0
        self.direction = 1

        self.image = Image.open(self.path + "idle/tile0.png")
        self.sprite = ImageTk.PhotoImage(image=self.image)
        self.parent = parent
        self.tom = self.parent.create_image(x, y, image=self.sprite)

        self.parent.after(100, self.idle)

    def idle(self):
        if self.sprite_number < 6:
            if self.direction == 1:
                self.image = Image.open(self.path + "idle/tile{}.png".format(self.sprite_number))
            else:
                self.image = Image.open(self.path + "idle/tile{}.png".format(self.sprite_number)).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            self.sprite = ImageTk.PhotoImage(image=self.image)
            self.parent.itemconfig(self.tom, image=self.sprite)
            self.parent.after(100, self.idle)
            self.sprite_number += 1
        else:
            self.sprite_number = 0
            self.idle_count += 1
            if self.idle_count > 4:
                self.parent.move(self.tom, 2*self.direction, 0)
                self.idle2()
            else:
                self.idle()


    def idle2(self):
        if self.sprite_number < 11:
            if self.direction == 1:
                self.image = Image.open(self.path + "idle2/tile{}.png".format(self.sprite_number))
            else:
                self.image = Image.open(self.path + "idle2/tile{}.png".format(self.sprite_number)).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            self.sprite = ImageTk.PhotoImage(image=self.image)
            self.parent.itemconfig(self.tom, image=self.sprite)
            self.parent.after(100, self.idle2)
            self.sprite_number += 1
        else:
            self.idle_count = 0
            self.sprite_number = 0
            self.drink_count += 1
            self.parent.move(self.tom, -2*self.direction, 0)
            if self.drink_count > 1:
                if self.walk_count > 6:
                    self.direction *= -1
                    self.walk_count = 0
                self.walk()
            else:
                self.idle()

    def walk(self):
        if self.sprite_number < 8:
            if self.direction == 1:
                self.image = Image.open(self.path + "walk/tile{}.png".format(self.sprite_number))
            else:
                self.image = Image.open(self.path + "walk/tile{}.png".format(self.sprite_number)).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            self.sprite = ImageTk.PhotoImage(image=self.image)
            self.parent.itemconfig(self.tom, image=self.sprite)
            self.parent.move(self.tom, 5*self.direction, 0)
            self.parent.after(100, self.walk)
            self.sprite_number += 1

        elif self.walk_count % 2 == 0:
            self.walk_count += 1
            self.sprite_number = 0
            self.walk()
        else:
            self.walk_count += 1
            self.sprite_number = 0
            self.drink_count = 0
            self.idle()

