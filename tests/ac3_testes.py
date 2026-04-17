import requests
import time

BASE_URL = "http://localhost:8000"

def gerar_email():
    return f"ac3teste{int(time.time()*1000)}@exemplo.com"

def log(nome, passou, status, resposta):
    resultado = "✅ PASSOU" if passou else "❌ FALHOU"
    print(f"{resultado} | {nome} | Status: {status} | Resposta: {resposta}")

# ──────────────────────────────────────────
# TESTES VÁLIDOS
# ──────────────────────────────────────────

def teste_cadastro_valido():
    email = gerar_email()
    resp = requests.post(f"{BASE_URL}/usuarios", json={
        "nome": "AC3 Teste",
        "email": email,
        "senha": "123456"
    })

    passou = resp.status_code == 200
    log("Cadastro de usuário válido", passou, resp.status_code, resp.json())

    if passou:
        return resp.json().get("id"), email
    return None, None

def teste_listar_usuarios():
    resp = requests.get(f"{BASE_URL}/usuarios")
    passou = resp.status_code == 200 and isinstance(resp.json(), list)
    log("Listar todos os usuários", passou, resp.status_code, f"{len(resp.json())} usuário(s) retornado(s)")

def teste_buscar_por_id(user_id):
    resp = requests.get(f"{BASE_URL}/usuarios/{user_id}")
    passou = resp.status_code == 200 and resp.json().get("id") == user_id
    log("Buscar usuário por ID", passou, resp.status_code, resp.json())

def teste_atualizar_usuario(user_id, email):
    resp = requests.put(f"{BASE_URL}/usuarios/{user_id}", json={
        "nome": "AC3 Atualizado",
        "email": email,
        "senha": "654321"
    })
    passou = resp.status_code == 200 and resp.json().get("nome") == "AC3 Atualizado"
    log("Atualizar dados do usuário", passou, resp.status_code, resp.json())

def teste_excluir_usuario(user_id):
    resp = requests.delete(f"{BASE_URL}/usuarios/{user_id}")
    passou = resp.status_code == 200
    log("Excluir usuário", passou, resp.status_code, resp.json())

# ──────────────────────────────────────────
# TESTES INVÁLIDOS
# ──────────────────────────────────────────

def teste_email_invalido():
    resp = requests.post(f"{BASE_URL}/usuarios", json={
        "nome": "Inválido",
        "email": "emailinvalido",
        "senha": "123456"
    })
    passou = resp.status_code == 422
    log("Cadastro com e-mail inválido", passou, resp.status_code, "Erro de validação esperado")

def teste_senha_curta():
    email = gerar_email()
    resp = requests.post(f"{BASE_URL}/usuarios", json={
        "nome": "Inválido",
        "email": email,
        "senha": "123"
    })
    passou = resp.status_code in (422, 400)
    log("Cadastro com senha curta", passou, resp.status_code, "Erro de validação esperado")

def teste_id_inexistente():
    resp = requests.get(f"{BASE_URL}/usuarios/9999")
    passou = resp.status_code == 404
    log("Buscar usuário com ID inexistente", passou, resp.status_code, resp.json())

def teste_body_vazio():
    resp = requests.post(f"{BASE_URL}/usuarios", json={})
    passou = resp.status_code == 422
    log("Cadastro com body vazio", passou, resp.status_code, "Erro de validação esperado")

def teste_nome_vazio():
    email = gerar_email()
    resp = requests.post(f"{BASE_URL}/usuarios", json={
        "nome": "",
        "email": email,
        "senha": "123456"
    })

    if resp.status_code == 200:
        print(f"❌ FALHOU | Cadastro com nome vazio (Bug 1) | Status: {resp.status_code} | BUG: API aceitou nome vazio")
    else:
        print(f"✅ PASSOU | Cadastro com nome vazio | Status: {resp.status_code}")

# ──────────────────────────────────────────
# EXECUÇÃO
# ──────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("AC3 – Testes Automatizados | API de Usuários")
    print("=" * 60)

    print("\n[TESTES VÁLIDOS]")
    user_id, email = teste_cadastro_valido()
    teste_listar_usuarios()

    if user_id:
        teste_buscar_por_id(user_id)
        teste_atualizar_usuario(user_id, email)
        teste_excluir_usuario(user_id)

    print("\n[TESTES COM ERRO PROPOSITAL]")
    teste_email_invalido()
    teste_senha_curta()
    teste_id_inexistente()
    teste_body_vazio()
    teste_nome_vazio()

    print("\n" + "=" * 60)
    print("Execução concluída. Verifique os resultados acima.")
    print("=" * 60)
