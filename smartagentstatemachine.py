!pip install matplotlib

import random
import matplotlib.pyplot as plt

class GameAgent:
    def __init__(self, secret_number, max_attempts=5, difficulty_level="fácil"):
        self.secret_number = secret_number
        self.max_attempts = max_attempts
        self.attempts = 0
        self.state = "Esperando tentativa"
        self.history = []  # Histórico de tentativas
        self.difficulty_level = difficulty_level

    def make_guess(self, guess):
        self.attempts += 1
        self.history.append(guess)

  # Easter Egg do Gigante de Alterosa
        if guess == 13:
            print("GALO! 🐓")

        if guess == self.secret_number:
            if self.difficulty_level == "armageddon":
                self.state = "Acertou!"
                return "Não sei como, mas você conseguiu! Você é um verdadeiro DEUS GAMER!"
            else:
                self.state = "Acertou!"
                return "Parabéns! Você acertou o número."
        elif self.attempts >= self.max_attempts:
            self.state = "Fim do jogo."
            if self.difficulty_level == "armageddon":
                return "Que pena... O número era {}.".format(self.secret_number)
            else:
                return f"Game Over! O número era {self.secret_number}."
        elif self.difficulty_level == "difícil":

            self.state = "Tentativa errada."
            return "Tentativa errada. Tente novamente."
        elif guess < self.secret_number:
            self.state = "Tentativa errada (muito baixo)."
            return "O número é maior. Tente novamente."
        else:
            self.state = "Tentativa errada (muito alto)."
            return "O número é menor. Tente novamente."

    def get_hint(self, guess):
        if self.difficulty_level == "fácil":
            # Dicas para o nível fácil
            hint = ""
            # Dica 1: Par ou ímpar
            if self.secret_number % 2 == 0:
                hint += "Dica: O número secreto é par. "
            else:
                hint += "Dica: O número secreto é ímpar. "
            # Dica 2: Proximidade
            difference = abs(self.secret_number - guess)
            if difference <= 10:
                hint += "Você está próximo do número secreto."
            else:
                hint += "Você está longe do número secreto."
            return hint

        elif self.difficulty_level == "médio":
            # Dicas para o nível médio
            difference = abs(self.secret_number - guess)
            if difference <= 10:
                return "Dica: Você está próximo do número secreto."
            else:
                return "Dica: Você está longe do número secreto."

        elif self.difficulty_level == "difícil":
            # Sem dicas para o nível difícil
            return "Modo difícil: Sem dicas por aqui!"

        elif self.difficulty_level == "armageddon":
            # Sem dicas para o modo Armageddon
            return ""  # Coloquei isso aqui para não ficar aparecendo aquela mensagem redundante no Game Over

        else:
            return "Sem dicas disponíveis."


def escolher_dificuldade():
    while True:
        nivel = input("Escolha a dificuldade: Fácil(1), Médio(2), Difícil(3) ou ARMAGEDDON(4): ")
        if nivel in ["1", "2", "3", "4"]:
            break
        else:
            print("Entrada inválida. Por favor, escolha 1, 2, 3 ou 4.")

    if nivel == "1":
        return "fácil", 10
    elif nivel == "2":
        return "médio", 5
    elif nivel == "3":
        return "difícil", 3
    elif nivel == "4":
        # Confirmação para o Modo ARMAGEDDON
        while True:
            confirmacao = input("Tem certeza que quer selecionar o modo ARMAGEDDON? (S/N): ").strip().upper()
            if confirmacao == "S":
                return "armageddon", 1
            elif confirmacao == "N":
                print("Voltando para a seleção de dificuldades...")
                return escolher_dificuldade()  # Volta para a seleção de dificuldades
            else:
                print("Entrada inválida. Digite S para confirmar ou N para voltar.")


def plot_attempts(agent):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(agent.history) + 1), agent.history, marker='o', linestyle='-')
    plt.axhline(y=agent.secret_number, color='r', linestyle='--', label='Número Secreto')
    plt.xlabel("Tentativas")
    plt.ylabel("Valor do Palpite")
    plt.title("Evolução das Tentativas do Jogador")
    plt.legend()
    plt.show()


# Iniciando o jogo
dificuldade, max_attempts = escolher_dificuldade()
agent = GameAgent(secret_number=random.randint(1, 100), max_attempts=max_attempts, difficulty_level=dificuldade)

print(f"Modo de dificuldade: {dificuldade.capitalize()}")
print(f"Você tem {max_attempts} tentativas. Boa sorte!")

while agent.state not in ["Acertou!", "Fim do jogo"]:
    guess = int(input("Digite um número: "))
    print(agent.make_guess(guess))
    if agent.state == "Fim do jogo":
        break  # Estive tentando encerrar o jogo logo após que o jogador perde no modo ARMAGEDDON, não consegui
    if agent.state != "Acertou!" and agent.state != "Fim do jogo" and agent.difficulty_level != "armageddon":
        print(agent.get_hint(guess))  # Só exibe dicas se não for o modo Armageddon

# Gráfico das tentativas
plot_attempts(agent)

# Na verdade, eu queria que o jogo terminasse imediatamente após você perder em qualquer dificuldade, mas não consegui implementar isso
