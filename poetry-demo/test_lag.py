import pytest
from main import lag, capturar_saida

def test_success_com_emoji():
    saida = capturar_saida(lag, "Olá! :smile:", "success")
    assert "Olá!" in saida

def test_success_sem_emoji():
    saida = capturar_saida(lag, "sucesso.", "success")
    assert "sucesso." in saida

def test_info_com_emoji():
    saida = capturar_saida(lag, "Hoje é um ótimo dia :laptop:", "info")
    assert "ótimo dia" in saida

def test_error_com_emoji():
    saida = capturar_saida(lag, "Erro detectado! :x:", "error")
    assert "Erro detectado!" in saida

def test_default_info():
    saida = capturar_saida(lag, "Mensagem normal sem cor")
    assert "Mensagem normal sem cor" in saida

def test_success_com_check():
    saida = capturar_saida(lag, "Processo concluído! :check_mark_button:", "success")
    assert "Processo concluído!" in saida

def test_info_com_hourglass():
    saida = capturar_saida(lag, "Carregando... :hourglass:", "info")
    assert "Carregando" in saida

def test_error_servidor():
    saida = capturar_saida(lag, "Falha ao conectar :cloud_with_lightning:", "error")
    assert "Falha ao conectar" in saida

def test_nivel_invalido():
    saida = capturar_saida(lag, "Nível inválido", "debug")
    assert "Nível inválido" in saida

def test_sem_nivel():
    saida = capturar_saida(lag, "Mensagem sem nível")
    assert "Mensagem sem nível" in saida

# negativos
def test_mensagem_vazia():
    saida = capturar_saida(lag, "", "success")
    assert saida == ""

def test_nivel_inexistente():
    saida = capturar_saida(lag, "Mensagem com nível inválido", "INVALIDO")
    assert "Mensagem com nível inválido" in saida

def test_nivel_none():
    saida = capturar_saida(lag, "Mensagem com nível None", None)
    assert "[EXCEPTION]" in saida

def test_mensagem_none():
    saida = capturar_saida(lag, None, "success")
    assert "[EXCEPTION]" in saida

def test_mensagem_numero():
    saida = capturar_saida(lag, 123, "info")
    assert "[EXCEPTION]" in saida

def test_nivel_numero():
    saida = capturar_saida(lag, "Mensagem", 404)
    assert "[EXCEPTION]" in saida

def test_emoji_invalido():
    saida = capturar_saida(lag, "Emoji fake :emoji_fake:", "info")
    assert "Emoji fake" in saida

def test_apenas_espacos():
    saida = capturar_saida(lag, " "*50, "error")
    assert saida.strip() == ""

def test_mensagem_e_nivel_vazio():
    saida = capturar_saida(lag, "", "")
    assert saida == ""

def test_mensagem_lista():
    saida = capturar_saida(lag, [], "info")
    assert "[EXCEPTION]" in saida
