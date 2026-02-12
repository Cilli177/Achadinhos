# Achadinhos

Projeto base profissional com **FastAPI**, **Pytest**, **Ruff**, **GitHub Actions** e **GitHub Codespaces**.

## Stack escolhida

- **API:** FastAPI
- **Runtime:** Python 3.10+
- **Configuração:** `pydantic-settings`
- **Qualidade:** Ruff (lint/import sort)
- **Testes:** Pytest
- **CI:** GitHub Actions
- **Ambiente cloud dev:** GitHub Codespaces (`.devcontainer`)

## Estrutura

- `app/main.py`: inicialização da aplicação
- `app/api/router.py`: agregador de rotas
- `app/api/routes/health.py`: endpoint de health check
- `app/core/config.py`: configurações da aplicação
- `tests/`: testes automatizados

## Como rodar no GitHub Codespaces

1. Abra o repositório no GitHub.
2. Clique em **Code > Codespaces > Create codespace on branch**.
3. Após criar o ambiente, rode:

```bash
make check
```

4. Para subir a API:

```bash
make run
```

A API ficará em `http://localhost:8000`.

## Como rodar localmente

```bash
make install
make check
make run
```

## Endpoints

- `GET /` → metadados do serviço
- `GET /health` → status da aplicação
