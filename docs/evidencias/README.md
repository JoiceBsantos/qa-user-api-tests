# 📸 Evidências dos Testes – API de Usuários

Este documento apresenta as evidências dos testes realizados na API, conforme os casos de teste definidos.

---

## CT01 – Cadastro de usuário válido

![CT01](evidencias/ct01-cadastro.png)

Resultado: Status 200, usuário criado com sucesso.

---

## CT02 – Listar usuários

![CT02](evidencias/ct02-listar.png)

Resultado: Status 200, lista de usuários retornada.

---

## CT03 – Buscar usuário por ID

![CT03](evidencias/ct03-buscar-id.png)

Resultado: Status 200, usuário retornado corretamente.

---

## CT04 – Atualização de usuário (sucesso)

![CT04](evidencias/ct04-update-sucesso.png)

Resultado: Status 200, dados atualizados.

---

## CT04 – Erro (email duplicado)

![CT04-Erro](evidencias/ct04-update-erro-email.png)

Resultado: Status 400, regra de negócio aplicada.

---

## CT05 – Exclusão de usuário

![CT05](evidencias/ct05-delete.png)

Resultado: Status 200, usuário excluído.

---

## CT05 – Validação após exclusão

![CT05-404](evidencias/ct05-validacao-404.png)

Resultado: Status 404, usuário não encontrado.

---

## CT06 – ID inexistente

![CT06](evidencias/ct06-id-inexistente.png)

Resultado: Status 404, erro retornado corretamente.

---

## CT07 – Email inválido

![CT07](evidencias/ct07-email-invalido.png)

Resultado: Status 422, validação aplicada.

---

## CT08 – Senha curta

![CT08](evidencias/ct08-senha-curta.png)

Resultado: Status 422, validação aplicada.

---

## Bug – Nome vazio

![BUG](evidencias/bug-nome-vazio.png)

Resultado: Status 200 (INCORRETO)
Descrição: A API aceita cadastro com nome vazio, caracterizando falha de validação.

---

