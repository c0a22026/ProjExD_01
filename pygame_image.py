import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kf_img = pg.image.load("ex01/fig/3.png")
    kf_img = pg.transform.flip(kf_img, True, False)
    kf_imgs = [pg.transform.rotozoom(kf_img, 10, 1.0), kf_img]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img, [1600 - tmr, 0])
        screen.blit(kf_imgs[tmr%2], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()