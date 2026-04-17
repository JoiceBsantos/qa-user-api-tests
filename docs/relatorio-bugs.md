
# Relatório de Bugs – API de Usuários

Este documento descreve os problemas identificados durante a execução dos testes na API.

---

## BUG 01 – Cadastro com nome vazio

**ID:** BUG-01
**Severidade:** Média
**Prioridade:** Alta

### Descrição

A API permite o cadastro de usuário com o campo "nome" vazio, o que não é um comportamento esperado.

---

### Passos para reproduzir

1. Enviar requisição POST para `/usuarios`
2. Utilizar o seguinte body:

```json
{
  "nome": "",
  "email": "bug@test.com",
  "senha": "123456"
}
```

---

### Resultado atual

* Status: 200 OK
* Usuário criado com nome vazio

---

### Resultado esperado

* Status: 422 Unprocessable Entity
* Mensagem de erro indicando campo obrigatório

---

### 📸 Evidência

![BUG01](evidencias/bug-nome-vazio.png)

---

### Sugestão de melhoria

Adicionar validação para garantir que o campo "nome" não seja vazio.

---

## BUG 02 – Inconsistência na validação de senha

**ID:** BUG-02
**Severidade:** Baixa
**Prioridade:** Média

---

### Descrição

A API apresenta inconsistência na validação de senha curta, retornando ora status 422, ora 400.

---

### Passos para reproduzir

1. Enviar requisição POST para `/usuarios`
2. Utilizar o seguinte body:

```json
{
  "nome": "Teste",
  "email": "teste@test.com",
  "senha": "123"
}
```

---

### Resultado atual

* Retorna status 422 ou 400 dependendo do cenário

---

### Resultado esperado

* Retornar sempre o mesmo padrão (preferencialmente 422)

---

### 📸 Evidência

![BUG02](evidencias/ct08-senha-curta.png)

---

### Sugestão de melhoria

Padronizar o tratamento de erro para manter consistência na API.

---
