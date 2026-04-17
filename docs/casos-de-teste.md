# 🧪 Casos de Teste – API de Usuários

Este documento descreve os casos de teste elaborados para validar o funcionamento da API de usuários.

---

## CT01 – Cadastro de usuário válido

**Objetivo:** Verificar se o cadastro funciona com dados corretos
**Método:** POST
**Endpoint:** /usuarios

**Entrada:**

```json
{
  "nome": "Joice Teste",
  "email": "joice.teste@email.com",
  "senha": "123456"
}
```

**Resultado esperado:**

* Status 200
* Retorna usuário com ID

---

## CT02 – Listar usuários

**Objetivo:** Verificar se a API retorna todos os usuários cadastrados
**Método:** GET
**Endpoint:** /usuarios

**Entrada:** Nenhuma

**Resultado esperado:**

* Status 200
* Retorna lista (array JSON)

---

## CT03 – Buscar usuário por ID

**Objetivo:** Verificar se a busca retorna o usuário correto
**Método:** GET
**Endpoint:** /usuarios/{id}

**Entrada:** ID válido

**Resultado esperado:**

* Status 200
* Retorna dados do usuário

---

## CT04 – Atualizar usuário

**Objetivo:** Verificar atualização de dados
**Método:** PUT
**Endpoint:** /usuarios/{id}

**Entrada:**

```json
{
  "nome": "Joice Atualizada",
  "email": "joice.novo@email.com",
  "senha": "654321"
}
```

**Resultado esperado:**

* Status 200
* Dados atualizados

---

## CT05 – Excluir usuário

**Objetivo:** Verificar exclusão de usuário
**Método:** DELETE
**Endpoint:** /usuarios/{id}

**Entrada:** ID válido

**Resultado esperado:**

* Status 200
* Mensagem de sucesso

---

## CT06 – ID inexistente

**Objetivo:** Validar comportamento com ID inválido
**Método:** GET
**Endpoint:** /usuarios/9999

**Resultado esperado:**

* Status 404
* Mensagem de erro

---

## CT07 – Email inválido

**Objetivo:** Validar rejeição de email incorreto
**Método:** POST
**Endpoint:** /usuarios

**Entrada:**

```json
{
  "nome": "Teste Invalido",
  "email": "emailinvalido",
  "senha": "123456"
}
```

**Resultado esperado:**

* Status 422
* Erro de validação

---

## CT08 – Senha curta

**Objetivo:** Validar rejeição de senha curta
**Método:** POST
**Endpoint:** /usuarios

**Entrada:**

```json
{
  "nome": "Teste Senha",
  "email": "senha@test.com",
  "senha": "123"
}
```

**Resultado esperado:**

* Status 422 ou 400
* Erro de validação

---

