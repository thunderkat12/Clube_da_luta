from personagem_base import PersonagemBase


class MeuLutador(PersonagemBase):
    """Lutador simples que se aproxima, ataca e se protege entre golpes."""

    @property
    def vida(self):
        """Permite consultar a vida sem acessar o atributo privado."""
        return self.__vida

    @vida.setter
    def vida(self, valor):
        # Mantém a vida entre 0 e 100, inclusive ao receber dano.
        self.__vida = max(0, min(100, valor))

    @property
    def dano_base(self):
        """Retorna o dano armazenado no atributo privado."""
        return self.__dano_base

    @dano_base.setter
    def dano_base(self, valor):
        if valor < 0:
            raise ValueError("O dano não pode ser negativo.")
        self.__dano_base = valor

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
