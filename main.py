import pygame
import sys

# Screen dimensions
pygame.init()

info = pygame.display.Info()
SCREEN_WIDTH = 512  # info.current_w
SCREEN_HEIGHT = 512  # info.current_h

FRAME_RATE_UPDATE = 20  # input in ms

sprite_sheet = pygame.image.load("images/sisyphus.png")


def get_sprite(sheet, col, row):
    width = 64
    height = 64
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sheet, (0, 0), (col * width, row * height, width, height))
    sprite = pygame.transform.scale(sprite, (512, 512))
    return sprite


class FrameCounter:
    def __init__(self, max_frame: int) -> None:
        self.current_frame = 0
        self.max_frame = max_frame

    def inc_frame(self):
        self.current_frame += 1
        if self.current_frame > self.max_frame:
            self.current_frame = 0


frame_counter = {
    "background": FrameCounter(1),
    "wall": FrameCounter(14),
    "boulder": FrameCounter(11),
    "sisyphus": FrameCounter(4),
}


def main():
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )  # , pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Sisyphus Clicker")
    current_time = 0
    last_time = 0

    # Main game loop
    while True:
        time_delta = clock.tick(1000 // FRAME_RATE_UPDATE)  # Control the frame rate
        current_time += time_delta
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # update frames
        if current_time >= last_time + 100:
            last_time = current_time
            for key in frame_counter:
                frame_counter[key].inc_frame()

        screen.fill((0, 0, 0))
        # background
        background = get_sprite(
            sprite_sheet, frame_counter["background"].current_frame, 0
        )
        screen.blit(background, (0, 0))
        # wall
        wall = get_sprite(sprite_sheet, frame_counter["wall"].current_frame, 1)
        screen.blit(wall, (0, 0))
        # boulder
        boulder = get_sprite(sprite_sheet, frame_counter["boulder"].current_frame, 2)
        screen.blit(boulder, (0, 0))
        # sisyphus
        sisyphus = get_sprite(sprite_sheet, frame_counter["sisyphus"].current_frame, 3)
        screen.blit(sisyphus, (0, 0))

        print(current_time)
        pygame.display.flip()


if __name__ == "__main__":
    main()
