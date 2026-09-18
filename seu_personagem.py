from personagem_base import PersonagemBase


class MeuLutador(PersonagemBase):
    """Lutador simples que se aproxima, ataca e se protege entre golpes."""

    def atualizar(self, oponente):
        distancia = oponente.x - self.x
        self.direcao = 1 if distancia >= 0 else -1

        # Libera a defesa antes de decidir a próxima ação.
        self.defender(False)

        if abs(distancia) > self.alcance_ataque:
            self.mover(self.direcao)
        elif self.cooldown_ataque == 0:
            self.atacar(oponente)
        else:
            # Enquanto o ataque recarrega, reduz o dano recebido.
            self.defender(True)
