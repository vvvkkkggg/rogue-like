from controller.game_controller import GameController
from view.interface_drawer import InterfaceDrawer
from model.factory import MapFactory
from model.game import Game
import pygame
import argparse


def main():
    """
    The main function initializes the game and starts the game loop.
    """
    parser = argparse.ArgumentParser(description="RogueLike Game")
    parser.add_argument("--map_file", type=str, help="Path to the map file")
    parser.add_argument(
        "--builder",
        type=str,
        choices=["default", "generate"],
        default="generate",
        help="Map builder type",
    )
    parser.add_argument(
        "--width", type=int, default=30, help="Width of the generated map"
    )
    parser.add_argument(
        "--height", type=int, default=30, help="Height of the generated map"
    )
    args = parser.parse_args()

    map_builder = MapFactory.get_builder(
        args.builder, args.width, args.height, args.map_file
    ).build()

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("RogueLike Game")
    clock = pygame.time.Clock()

    controller = GameController(Game(map_builder))
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
