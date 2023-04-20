import sys
import pygame as pg


class Button:

    def __init__(self, x, y, w, h, c, text=''):
        self.button = pg.Rect(x, y, w, h)
        self.clicked = False
        self.text = text
        self.color = c
        self.txt_surface = HEADERFONT.render(text, True, COLOR_HEAD)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.button,)

    def checkStatus(self):
        mouse_pos = pg.mouse.get_pos()
        if self.button.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                pg.draw.rect(screen, COLOR_ACTIVE_BUTTON, self.button)

        if pg.mouse.get_pressed()[0] == False:
            self.clicked = False

    def update(self, screen):
        if submit.checkStatus():
            pg.draw.rect(screen, (128, 115, 128),
                         (self.x, self.y, self.w, self.h))

    def select(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.button.collidepoint(event.pos):
                self.clicked = not self.clicked
            else:
                self.clicked = False
            self.color = COLOR_ACTIVE_BUTTON if self.clicked else self.color


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x +
                    5, self.rect.y+5))  # text offset
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


class IntInput:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:

            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isnumeric():
                        self.text += event.unicode
                    else:
                        self.text = self.text
                # Re-render the text.
            self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x +
                    5, self.rect.y+5))  # text offset
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


class Password():
    def __init__(self, x, y, w, h, key='', text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.key = key
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += 'X'
                    self.key += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x +
                    5, self.rect.y+5))  # text offset
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


class Head:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_HEAD
        self.text = text
        self.txt_surface = HEADERFONT.render(text, True, self.color)


def result():
    run2 = True
    pg.display.set_caption('Success')
    screen2 = pg.display.set_mode((640, 240))
    text_display = Head(200, 35, 140, 32, 'Welcome , ' + input_box4.text)
    text_display2 = Head(
        150, 70, 140, 32, 'You have successfully resgistered !')
    text_display3 = Head(
        150, 150, 140, 32, 'Your Password is : ' + input_box5.key)
    while run2:
        screen2.fill((255, 229, 204))

        screen2.blit(text_display.txt_surface,
                     (text_display.rect.x, text_display.rect.y))
        screen2.blit(text_display2.txt_surface,
                     (text_display2.rect.x, text_display2.rect.y))
        screen2.blit(text_display3.txt_surface,
                     (text_display3.rect.x, text_display3.rect.y))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                run2 = False
        pg.display.update()


pg.init()
pg.display.set_caption('Profile')
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

# ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_INACTIVE_BUTTON = pg.Color('pink')
COLOR_ACTIVE = pg.Color('dodgerblue2')
COLOR_ACTIVE_BUTTON = pg.Color((125, 118, 125))
COLOR_HEAD = pg.Color('black')
# ^^^
FONT = pg.font.Font('C:\WINDOWS\FONTS\AGENCYB.TTF', 20)
HEADERFONT = pg.font.Font('C:\WINDOWS\FONTS\AGENCYB.TTF', 32)

first_name = Head(75, 50, 140, 32, 'Firstname :  ')
last_name = Head(420, 50, 140, 32, 'Lastname :  ')
age = Head(100, 130, 140, 32, 'Age :  ')
gender = Head(280, 130, 140, 32, 'Gender :  ')
username = Head(100, 200, 140, 32, 'Username :  ')
password = Head(100, 270, 140, 32, 'Password :  ')
confirmpassword = Head(100, 340, 140, 32, 'Confirm Password :  ')

submit = Button(568, 423, 200, 40, COLOR_INACTIVE_BUTTON, 'Submit')
male = Button(410, 130, 40, 40, 'lightskyblue3', 'Male')
female = Button(540, 130, 40, 40, 'pink', 'Female')


input_box1 = InputBox(215, 58, 140, 32)  # สร้าง InputBox1
input_box2 = InputBox(550, 58, 140, 32)  # สร้าง InputBox2
input_box3 = IntInput(170, 138, 50, 32)
input_box4 = InputBox(230, 208, 200, 32)
input_box5 = Password(230, 278, 200, 32, '')
input_box6 = Password(330, 348, 200, 32, '')


# เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
input_boxes = [input_box1, input_box2, input_box3,
               input_box4, input_box5, input_box6]
headers = [first_name, last_name, age, gender,
           username, password, confirmpassword]
selection = [male, female]
run = True
setgender = ''
while run:
    screen.fill((255, 229, 204))

    for header in headers:
        screen.blit(header.txt_surface, (header.rect.x, header.rect.y))
    for box in input_boxes:  # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update()  # เรียกใช้ฟังก์ชัน update() ของ InputBox
        # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        box.draw(screen)

    submit.draw(screen)
    male.draw(screen)
    female.draw(screen)
    screen.blit(female.txt_surface, (595, 130))
    screen.blit(male.txt_surface, (462, 130))
    screen.blit(submit.txt_surface, (625, 420))
    if male.clicked:
        female.color = 'pink'
        setgender = 'Male'
    if female.clicked:
        male.color = 'lightskyblue3'
        setgender = 'Female'

    if submit.clicked:
        checktext = False
        checkmark = False
        matchup = False
        for check in input_boxes:
            if check.text != '':
                checktext = True
            else:
                checktext = False
        if setgender != '':
            checkmark = True
        if (input_box5.key == input_box6.key) and (input_box5.key != '') and (input_box6.key != ''):
            matchup = True

        if checktext and checkmark and matchup:
            result()

        if (checktext == True) and (checkmark == True) and (matchup == False):
            etextdisplay = HEADERFONT.render(
                "Your Password Doesn't Match", True, 'red')
            screen.blit(etextdisplay, (100, 380))
        elif (checktext == False) or (checkmark == False):
            etextdisplay2 = HEADERFONT.render(
                "Please complete the information", True, 'red')
            screen.blit(etextdisplay2, (100, 380))
        print('Hello, '+input_box1.text + input_box2.text +
              " You're age : " + ' ' + input_box3.text + 'years old')
        print(checktext, checkmark, matchup)

    submit.update(screen)
    for event in pg.event.get():
        for pick in selection:
            pick.select(event)
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    # print(pg.mouse.get_pos())
    pg.time.delay(30)
    pg.display.update()
