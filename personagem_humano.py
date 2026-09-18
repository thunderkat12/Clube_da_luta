import pygame
import math


from personagem_base import PersonagemBase


class PersonagemHumano(PersonagemBase):
    """Personagem controlado via teclado (Seta/WASD) para o modo Treino."""
    def atualizar(self, oponente):
        teclas = pygame.key.get_pressed()

        # Movimentação
        if teclas[pygame.K_LEFT]:
            self.mover(-1)
        elif teclas[pygame.K_RIGHT]:
            self.mover(1)

        # Pulo
        if teclas[pygame.K_UP]:
            self.pular()

        # Defesa
        self.defender(teclas[pygame.K_DOWN])

        # Ataque
        if teclas[pygame.K_SPACE]:
            self.atacar(oponente)


class PersonagemHumano2(PersonagemBase):
    """Personagem controlado via teclado (Seta/WASD) para o modo Treino."""
    def atualizar(self, oponente):
        teclas = pygame.key.get_pressed()

        # Movimentação
        if teclas[pygame.K_a]:
            self.mover(-1)
        elif teclas[pygame.K_d]:
            self.mover(1)

        # Pulo
        if teclas[pygame.K_w]:
            self.pular()

        # Defesa
        self.defender(teclas[pygame.K_s])

        # Ataque
        if teclas[pygame.K_q]:
            self.atacar(oponente)
