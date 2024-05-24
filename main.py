import pygame
from controller.game_controller import GameController
from view.interface_drawer import InterfaceDrawer


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("RogueLike Game")
    clock = pygame.time.Clock()

    controller = GameController()
    drawer = InterfaceDrawer(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            controller.handle_event(event)

        controller.update()
        drawer.draw(controller.get_game_state())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
