import numpy as np
import pygame
import body

G = 6.6743 * 10**(-11)

class System:
    def __init__(self):
        self.bodies = np.array([])

    def addBody(self, body):
        self.bodies = np.append(self.bodies, body)

    def update(self, step=.1):
        for m1 in self.bodies:
            m1.a = 0
            for m2 in self.bodies:
                if m1 != m2:
                    m1.a += ((G * m2.mass * (m2.r - m1.r))/((np.linalg.norm(m2.r - m1.r))**3))
        for b in self.bodies:
            b.v += b.a * step
            b.r += b.v * step

    def resetAll(self):
        for b in self.bodies:
            b.reset()

if __name__ == "__main__":
    print("Starting")
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    s = System()

    m1 = body.Body(1000000000000)
    m2 = body.Body(1)
    m3 = body.Body(1)

    # m1.setInitVelocity(0., 0., 0.)
    m2.setInitPosition(100., 0., 0.)
    m2.setInitVelocity(0., .75, 0.)
    m3.setInitPosition(200., 0., 0.)
    m3.setInitVelocity(0., .5, 0.)

    s.addBody(m1)
    s.addBody(m2)
    s.addBody(m3)
    s.resetAll()
    # s.update(step=1)

    # i = 1
    # for b in s.bodies:
    #     print("Body", i)
    #     print(b.r)
    #     print(b.v)
    #     print(b.a)
    #     i += 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        for b in s.bodies:
            # print(b.r)
            pygame.draw.circle(screen, "white", (b.r[0]+640, b.r[1]+360), 20)

        dt = clock.tick(60) / 10
        s.update(step=dt)

        pygame.display.flip()

    pygame.quit()

