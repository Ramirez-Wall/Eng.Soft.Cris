from colorama import Fore, Style, init
import emoji

# Inicializa o Colorama
init(autoreset=True)

# Mensagens coloridas com emojis
print(Fore.GREEN + emoji.emojize("Olá! :smile:", language="alias"))
print(Fore.BLUE + emoji.emojize("Hoje é um ótimo dia para programar! :laptop:", language="alias"))
print(Fore.RED + emoji.emojize("Erro detectado! :x:", language="alias"))
print(Style.RESET_ALL + "Texto normal agora.")
