from colorama import Fore, Style, init
import emoji

# Inicializa o Colorama
init(autoreset=True)

# Função para mostrar mensagens coloridas com emojis
def lag(message: str, level: str = "info"):
    try:
        if not isinstance(message, str):
            raise TypeError("A mensagem deve ser uma string.")
        if not isinstance(level, str):
            raise TypeError("O nível deve ser uma string.")

        if level == "success":
            print(Fore.GREEN + emoji.emojize(message, language="alias"))
        elif level == "info":
            print(Fore.BLUE + emoji.emojize(message, language="alias"))
        elif level == "error":
            print(Fore.RED + emoji.emojize(message, language="alias"))
        else:
            print(Style.RESET_ALL + message)
    except Exception as e:
        print(Fore.RED + f"[EXCEPTION] {e}")


# ==========================
# CASOS DE TESTE
# ==========================
def testar_lag():
    print("\n--- TESTES POSITIVOS ---")
    # Casos Positivos
    lag("Olá! :smile:", "success")                       # 1
    lag("sucesso.", "success")                          # 2
    lag("Hoje é um ótimo dia para programar! :laptop:", "info")  # 3
    lag("Erro detectado! :x:", "error")                 # 4
    lag("Mensagem normal sem cor ou emoji.")            # 5 (nível não passado > default info)
    lag("Processo concluído! :check_mark_button:", "success")    # 6
    lag("Carregando dados... :hourglass:", "info")      # 7
    lag("Falha ao conectar ao servidor :cloud_with_lightning:", "error")  # 8
    lag("Nível desconhecido, mas ainda mostra mensagem", "debug")        # 9 (cai no else)
    lag("Mensagem sem nível definido")                  # 10 (default "info")

    print("\n--- TESTES NEGATIVOS ---")
    # Casos Negativos
    lag("", "success")                                  # 1 (mensagem vazia)
    lag("Mensagem com nível inválido", "INVALIDO")      # 2 (nível não existe > else)
    lag("Mensagem com nível None", None)                # 3 (nível None > exception)
    lag(None, "success")                                # 4 (mensagem None > exception)
    lag(123, "info")                                    # 5 (mensagem não string)
    lag("Mensagem com nível numérico", 404)             # 6 (nível numérico)
    lag("Mensagem com emoji inválido :emoji_fake:", "info")  # 7 (emoji não existe)
    lag(" "*50, "error")                                # 8 (string só com espaços)
    lag("", "")                                         # 9 (mensagem e nível vazios)
    lag([], "info")                                     # 10 (mensagem como lista)

# Rodar os testes
if __name__ == "__main__":
    testar_lag()
