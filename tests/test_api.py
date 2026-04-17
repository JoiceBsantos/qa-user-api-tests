import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_cadastro_usuario():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/usuarios", json={
            "nome": "Teste Pytest",
            "email": "pytest1@teste.com",
            "senha": "123456"
        })
        assert resp.status_code == 200

@pytest.mark.asyncio
async def test_listar_usuarios():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.get("/usuarios")
        assert resp.status_code == 200

@pytest.mark.asyncio
async def test_buscar_usuario_por_id():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.get("/usuarios/1")
        assert resp.status_code in [200, 404]

@pytest.mark.asyncio
async def test_atualizar_usuario():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.put("/usuarios/1", json={
            "nome": "Atualizado",
            "email": "pytest2@teste.com",
            "senha": "654321"
        })
        assert resp.status_code in [200, 400]

@pytest.mark.asyncio
async def test_excluir_usuario():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.delete("/usuarios/1")
        assert resp.status_code in [200, 404]
