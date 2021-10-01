from itertools import cycle
from random import randrange
from tkinter import Frame, Label, Tk , Canvas , messagebox , font
import pygame

def egg_main():

    canvas_width = 800
    canvas_height = 400

    win = Tk()
    win.title('Egg Catcher Game')
    win.maxsize(800, 400)
    win.minsize(800, 400)
    c = Canvas(win , width = canvas_width ,  height = canvas_height , background = '#0091EA')
    c.create_rectangle(-5, canvas_height - 100 , canvas_width + 5 , canvas_height + 5 , fill='#64DD17', width=3, outline='black')
    c.create_oval(-80,-80,120,120,fill='#FFEA00' , width=3, outline='black')

    c.pack()
    global score , egg_speed , egg_interval, lives_remaning

    color_cycle = cycle(['#E040FB' , '#546E7A' , '#18FFFF','#FF5722' , '#00C853', '#FFC107'])
    egg_width = 45
    egg_height = 55
    egg_score = 10
    egg_speed = 500
    egg_interval = 4000
    difficulty_factor = 0.95

    catcher_color = '#6200EA'
    catcher_width = 100
    catcher_height = 100
    catcher_start_x = canvas_width / 2 - catcher_width / 2
    catcher_start_y = canvas_height -catcher_height - 20
    catcher_start_x2 = catcher_start_x + catcher_width
    catcher_start_y2 = catcher_start_y + catcher_height

    catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=3)


    score = 0
    score_text = c.create_text(350,5,anchor='nw' , font=('Arial',23,'bold'),fill='#FF9100',text='Score : ' + str(score))

    lives_remaning = 3
    lives_text = c.create_text(canvas_width-10,5,anchor='ne' , font=('Arial',18,'bold'),fill='#FF9100',text='Lives : ' + str(lives_remaning))

    eggs = []

    def create_eggs():
        x = randrange(10,740)
        y = 40
        new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=3, outline='black')
        eggs.append(new_egg)
        win.after(egg_interval,create_eggs)

    def move_eggs():
        for egg in eggs:
            (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
            c.move(egg,0,10)
            if egg_y2 > canvas_height:
                egg_dropped(egg)
        win.after(egg_speed,move_eggs)

    def egg_dropped(egg):
        eggs.remove(egg)
        c.delete(egg)
        lose_a_life()
        if lives_remaning == 0:
            game_music()
            messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
            win.destroy()


    def lose_a_life():
        global lives_remaning
        lives_remaning -= 1
        print('lives : ',lives_remaning)
        c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))

    def catch_check():
        (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
        for egg in eggs:
            (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
            if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40:
                eggs.remove(egg)
                c.delete(egg)
                increase_score(egg_score)
        print('Score : ',score , '\nEgg Speed : ',egg_speed , '\nEgg Interval : ',egg_interval)
        win.after(100,catch_check)

    def increase_score(points):
        global score , egg_speed , egg_interval
        score += points
        egg_speed = int(egg_speed * difficulty_factor)
        egg_interval = int(egg_interval * difficulty_factor)
        c.itemconfigure(score_text , text='Score : ' + str(score))

    def move_left(event):
        (x1,y1,x2,y2) = c.coords(catcher)
        if x1 > 0:
            c.move(catcher,-20,0)

    def move_right(event):
        (x1,y1,x2,y2) = c.coords(catcher)
        if x2 < canvas_width:
            c.move(catcher,20,0)

    def game_music():
        pygame.mixer.music.stop()
        


    c.bind('<Left>' , move_left)
    c.bind('<Right>' , move_right)
    c.focus_set()

    win.after(1000,create_eggs)
    win.after(1000,move_eggs)
    win.after(1000,catch_check)
    pygame.init()
    pygame.mixer.music.load('sounds/skar_track.mp3')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
    win.mainloop()


if __name__ == '__main__':
    egg_main()
