from colorama import Fore, Style, init
import emoji

# Inicializa o Colorama
init(autoreset=True)

# Função para mostrar mensagens coloridas com emojis
def log(message: str, level: str = "info"):
    if level == "success":
        print(Fore.GREEN + emoji.emojize(message, language="alias"))
    elif level == "info":
        print(Fore.BLUE + emoji.emojize(message, language="alias"))
    elif level == "error":
        print(Fore.RED + emoji.emojize(message, language="alias"))
    else:
        print(Style.RESET_ALL + message)

# Testando a função
log("Olá! :smile:", "success")
log("sucesso.", "success")
log("Hoje é um ótimo dia para programar! :laptop:", "info")
log("Erro detectado! :x:", "error")
log("Mensagem normal sem cor ou emoji.")
