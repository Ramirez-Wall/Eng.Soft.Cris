from colorama import Fore, Style, init
import emoji
import io
from contextlib import redirect_stdout

# Inicializa o Colorama
init(autoreset=True)

def lag(message: str, level: str = "info"):
    try:
        if not isinstance(message, str):
            raise TypeError("A mensagem deve ser uma string.")
        if not isinstance(level, str):
            raise TypeError("O nível deve ser uma string.")

        if not message.strip():  # mensagem vazia ou só espaços
            print("")  # sem códigos ANSI
            return

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


def capturar_saida(func, *args, **kwargs):
    f = io.StringIO()
    with redirect_stdout(f):
        func(*args, **kwargs)
    return f.getvalue().strip()
