from unittest.mock import patch
from main import lag

def test_lag_chama_emoji_emojize():
    mensagem = "Olá! :smile:"
    nivel = "success"

    with patch("main.emoji.emojize") as mock_emojize, patch("builtins.print") as mock_print:
        mock_emojize.return_value = "Olá! 😄"
        lag(mensagem, nivel)

        mock_emojize.assert_called_once_with(mensagem, language="alias")
        chamado_print = mock_print.call_args[0][0]
        assert "Olá! 😄" in chamado_print
