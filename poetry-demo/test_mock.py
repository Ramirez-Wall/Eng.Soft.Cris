from unittest.mock import patch
import pytest
from main import lag  # substitua pelo nome do seu arquivo .py

# Teste com MOCK para verificar se a função emoji.emojize é chamada corretamente
def test_lag_chama_emoji_emojize():
    mensagem = "Olá! :smile:"
    nivel = "success"
    
    with patch("main.emoji.emojize") as mock_emojize:
        with patch("builtins.print") as mock_print:
            mock_emojize.return_value = "Olá! 😄"
            lag(mensagem, nivel)
            
            # Verifica se emoji.emojize foi chamado com a mensagem
            mock_emojize.assert_called_once_with(mensagem, language="alias")
            
            # Verifica se print foi chamado com o resultado do emojize + cor
            args_print = mock_print.call_args[0][0]  # primeiro argumento do primeiro print
            assert "Olá! 😄" in args_print
