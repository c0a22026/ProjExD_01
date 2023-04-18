import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]*2
    kf_img = pg.image.load("ex01/fig/3.png")
    kf_img = pg.transform.flip(kf_img, True, False)
    kf_imgs = [kf_img, pg.transform.rotozoom(kf_img, 10, 1.0)]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        tmr += 1
        x = tmr%3200
        for i in range(4):
            screen.blit(bg_imgs[i], [1600 * i - x, 0])
        screen.blit(kf_imgs[tmr % 100//50], [300, 200])
        
        print(tmr)
        pg.display.update()
        clock.tick(800)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()