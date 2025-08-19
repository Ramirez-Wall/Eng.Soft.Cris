from colorama import Fore, Style, init
import emoji

# Inicializa o Colorama
init(autoreset=True)

# Função para mostrar mensagens coloridas com emojis
def lag(message: str, level: str = "info"):
    if level == "success":
        print(Fore.GREEN + emoji.emojize(message, language="alias"))
    elif level == "info":
        print(Fore.BLUE + emoji.emojize(message, language="alias"))
    elif level == "error":
        print(Fore.RED + emoji.emojize(message, language="alias"))
    else:
        print(Style.RESET_ALL + message)

# Testando a função
lag("Olá! :smile:", "success")
lag("sucesso.", "success")
lag("Hoje é um ótimo dia para programar! :laptop:", "info")
lag("Erro detectado! :x:", "error")
lag("Mensagem normal sem cor ou emoji.")