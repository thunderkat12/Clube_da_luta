import pygame
import sys
import math

from constants import *
from personagem_base import PersonagemBase
from personagem_humano import PersonagemHumano, PersonagemHumano2
from seu_personagem import MeuLutador

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("POO Fighting Arena")

RELOGIO = pygame.time.Clock()

# Inicialização do Pygame
pygame.init()



# ==========================================
# EXEMPLES DE PERSONAGENS / IMPLEMENTAÇÃO
# ==========================================

class BotPadrao(PersonagemBase):
    """Um robô simples com lógica básica de aproximação e ataque."""
    def atualizar(self, oponente):
        distancia = oponente.x - self.x

        # Se estiver longe, aproxima-se
        if abs(distancia) > 40:
            if distancia > 0:
                self.mover(1)
            else:
                self.mover(-1)
        else:
            # Se estiver perto, ataca
            self.atacar(oponente)


# ==========================================
# LOOP PRINCIPAL E SELEÇÃO DE MODOS
# ==========================================
def rodar_arena(p1_class, p2_class, nome_p1, nome_p2, cor_p1, cor_p2):
    p1 = p1_class(x=150, nome=nome_p1, cor=cor_p1, direcao=1)
    p2 = p2_class(x=600, nome=nome_p2, cor=cor_p2, direcao=-1)

    rodando = True
    fonte = pygame.font.SysFont("arial", 20, bold=True)

    while rodando:
        RELOGIO.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualiza a lógica dos bots/jogadores
        p1.atualizar(p2)
        p2.atualizar(p1)

        # Renderização na Tela
        TELA.fill((30, 30, 30))  # Fundo escuro

        # Desenhar Chão
        pygame.draw.rect(TELA, (70, 70, 70), (0, CHAO_Y, LARGURA, ALTURA - CHAO_Y))

        # Desenhar Personagens
        p1.desenhar(TELA)
        p2.desenhar(TELA)

        # Interface de Texto (HUD)
        texto_p1 = fonte.render(f"{p1.nome}: {int(p1.vida)} HP", True, p1.cor)
        texto_p2 = fonte.render(f"{p2.nome}: {int(p2.vida)} HP", True, p2.cor)
        TELA.blit(texto_p1, (20, 20))
        TELA.blit(texto_p2, (LARGURA - 200, 20))

        # Checar Fim de Jogo
        if p1.vida <= 0 or p2.vida <= 0:
            vencedor = "Empate!"
            if p1.vida > 0: vencedor = f"{p1.nome} Venceu!"
            elif p2.vida > 0: vencedor = f"{p2.nome} Venceu!"

            txt_fim = fonte.render(f"FIM DE JOGO: {vencedor}", True, BRANCO)
            TELA.blit(txt_fim, (LARGURA // 2 - 120, ALTURA // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            rodando = False

        pygame.display.flip()

# ==========================================
# MENU INICIAL
# ==========================================
if __name__ == "__main__":
    print("=== SELEÇÃO DE MODO DE JOGO ===")
    print("1. Treinamento (Você vs Daniel)")
    print("2. Simulação / Torneio (Daniel vs Bot Padrão)")
    print("Controles: setas para mover/pular/defender; espaço para atacar.")

    opcao = input("Escolha a opção (1 ou 2): ")

    if opcao == "1":
        rodar_arena(
            p1_class=PersonagemHumano,
            p2_class=MeuLutador,
            nome_p1="Jogador",
            nome_p2="Daniel",
            cor_p1=AZUL,
            cor_p2=VERMELHO
        )
    else:
        rodar_arena(
            p1_class=MeuLutador,
            p2_class=BotPadrao,
            nome_p1="Daniel",
            nome_p2="Bot Padrão",
            cor_p1=VERDE,
            cor_p2=VERMELHO
        )
