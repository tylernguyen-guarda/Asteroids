import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    containers = []

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius  # type: ignore
        b = self.position - forward * self.radius - right  # type: ignore
        c = self.position - forward * self.radius + right  # type: ignore
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # type: ignore

    def rotate(self, delta_time):
        self.rotation += delta_time * PLAYER_TURN_SPEED

    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)  # type: ignore
        shot_velocity = pygame.Vector2(0, 1)
        new_shot.velocity = shot_velocity.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.cooldown_timer += PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt

        if keys[pygame.K_SPACE] and self.cooldown_timer <= 0:
            self.shoot()
