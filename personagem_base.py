import pygame
import math

from constants import *


class PersonagemBase:
    """
    Classe Abstrata/Base de Personagem.
    NÃO alterem esta classe! Vocês devem criar uma subclasse herdando dela.
    """
    def __init__(self, x, nome, cor, direcao=1):
        self.nome = nome
        self.x = x
        self.y = CHAO_Y - 80
        self.largura = 50
        self.altura = 80
        self.cor = cor

        # Atributos de Estado
        self.vida = 100
        self.velocidade = 5
        self.vel_y = 0
        self.em_pulo = False
        self.defendendo = False
        self.atacando = False
        self.cooldown_ataque = 0
        self.direcao = direcao  # 1 para direita, -1 para esquerda

        # Alcance e Dano
        self.alcance_ataque = 60
        self.dano_base = 10

    def mover(self, direcao):
        """Move o personagem: direcao -1 (esquerda) ou 1 (direita)"""
        if not self.defendendo:
            self.direcao = direcao
            self.x += direcao * self.velocidade
            # Limites de tela
            self.x = max(0, min(LARGURA - self.largura, self.x))

    def pular(self):
        """Aciona o pulo do personagem"""
        if not self.em_pulo and not self.defendendo:
            self.em_pulo = True
            self.vel_y = -15

    def defender(self, ativo):
        """Ativa/desativa a postura defensiva (Reduz dano em 80%)"""
        self.defendendo = ativo

    def atacar(self, oponente):
        """Realiza um ataque contra o oponente se estiver no alcance"""
        if not self.atacando and self.cooldown_ataque == 0 and not self.defendendo:
            self.atacando = True
            self.cooldown_ataque = 30  # Frames de espera

            # Checar colisão do ataque com o oponente
            distancia = abs((self.x + self.largura/2) - (oponente.x + oponente.largura/2))
            if distancia <= self.alcance_ataque and abs(self.y - oponente.y) < 50:
                dano_final = self.dano_base
                if oponente.defendendo:
                    dano_final *= 0.2  # Defesa reduz 80% do dano
                oponente.receber_dano(dano_final)

    def receber_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida < 0:
            self.vida = 0

    def aplicar_gravidade(self):
        if self.em_pulo:
            self.y += self.vel_y
            self.vel_y += 1  # Gravidade
            if self.y >= CHAO_Y - self.altura:
                self.y = CHAO_Y - self.altura
                self.em_pulo = False
                self.vel_y = 0

    def atualizar(self, oponente):
        """
        MÉTODO OBRIGATÓRIO PARA OS ALUNOS IMPLEMENTAREM NA SUBCLASSE.
        Aqui deve residir a LÓGICA DO BOT (IA) do seu personagem.
        """
        pass

    def desenhar(self, tela):
        # Gerenciador de cooldowns internos
        if self.cooldown_ataque > 0:
            self.cooldown_ataque -= 1
            if self.cooldown_ataque < 20:
                self.atacando = False

        # Aplicar gravidade
        self.aplicar_gravidade()

        # Renderizar o Personagem (CorPO e Estado)
        cor_render = self.cor
        if self.defendendo:
            cor_render = CINZA

        # Corpo
        pygame.draw.rect(tela, cor_render, (self.x, self.y, self.largura, self.altura))

        # Indicador de Direção (Olhos)
        olho_x = self.x + (35 if self.direcao == 1 else 10)
        pygame.draw.circle(tela, BRANCO, (olho_x, self.y + 20), 5)

        # Efeito Visual de Ataque
        if self.atacando:
            ataque_x = self.x + self.largura if self.direcao == 1 else self.x - 30
            pygame.draw.rect(tela, VERMELHO, (ataque_x, self.y + 20, 30, 20))

        # Barra de Vida acima do personagem
        pygame.draw.rect(tela, VERMELHO, (self.x, self.y - 15, 50, 8))
        pygame.draw.rect(tela, VERDE, (self.x, self.y - 15, 50 * (self.vida / 100), 8))

