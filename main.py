import pygame
from controller.game_controller import GameController
from view.interface_drawer import InterfaceDrawer


def main():
    """
    The main function initializes the game and starts the game loop.
    """
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
            else:
                controller.handle_event(event)

        controller.update()
        game_state = controller.get_game_state()
        drawer.draw(game_state)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
