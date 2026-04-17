import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_cadastro_usuario():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/usuarios", json={
            "nome": "Usuário Teste",
            "email": "teste@exemplo.com",
            "senha": "123456"
        })
        assert resp.status_code == 200
