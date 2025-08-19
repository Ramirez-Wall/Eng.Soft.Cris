from colorama import Fore, Style, init
import emoji

# Inicializa o Colorama
init(autoreset=True)

# Função para mostrar mensagens coloridas com emojis
def funcao(message: str, level: str = "info"):
    if level == "success":
        print(Fore.GREEN + emoji.emojize(message, language="alias"))
    elif level == "info":
        print(Fore.BLUE + emoji.emojize(message, language="alias"))
    elif level == "error":
        print(Fore.RED + emoji.emojize(message, language="alias"))
    else:
        print(Style.RESET_ALL + message)

# Testando a função
funcao("Olá! :smile:", "success")
funcao("sucesso.", "success")
funcao("Hoje é um ótimo dia para programar! :laptop:", "info")
funcao("Erro detectado! :x:", "error")
funcao("Mensagem normal sem cor ou emoji.")
funcao("Mensagem normal sem cor ou emoji, só para criar o problema de merge.")
