# My Store API - Projeto - DIO

## 📋 Sobre o Projeto

Este projeto é uma versão personalizada do desafio da DIO (Digital Innovation One) para desenvolvimento de uma API de loja utilizando TDD (Test Driven Development). A API foi desenvolvida com FastAPI, MongoDB e seguindo as melhores práticas de desenvolvimento orientado a testes.

### 🎯 Objetivo

Demonstrar na prática os conceitos de TDD através do desenvolvimento de uma API REST completa para gerenciamento de produtos, incluindo funcionalidades avançadas como filtros de busca, paginação e tratamento robusto de exceções.

## 🚀 Funcionalidades

### ✅ Funcionalidades Implementadas

- **CRUD Completo de Produtos**
  - ✅ Criar produto
  - ✅ Listar produtos com filtros e paginação
  - ✅ Buscar produto por ID
  - ✅ Atualizar produto (PATCH)
  - ✅ Deletar produto

- **Filtros Avançados**
  - ✅ Filtro por nome (busca case-insensitive)
  - ✅ Filtro por categoria
  - ✅ Filtro por faixa de preço (min_price e max_price)
  - ✅ Paginação (skip e limit)

- **Tratamento de Exceções**
  - ✅ Exceções personalizadas para produtos não encontrados
  - ✅ Tratamento de erros de criação
  - ✅ Mensagens de erro amigáveis ao usuário
  - ✅ Atualização automática do campo `updated_at`

- **Testes Abrangentes**
  - ✅ Testes de schemas (Pydantic)
  - ✅ Testes de casos de uso (business logic)
  - ✅ Cobertura de cenários de sucesso e falha

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI** - Framework web moderno e rápido
- **MongoDB** - Banco de dados NoSQL
- **Motor** - Driver assíncrono para MongoDB
- **Pydantic** - Validação de dados e serialização
- **Pytest** - Framework de testes
- **Docker & Docker Compose** - Containerização

## 📁 Estrutura do Projeto

```
my_store_api/
├── store/                      # Código principal da aplicação
│   ├── controllers/            # Controladores (rotas da API)
│   │   └── product.py
│   ├── usecases/              # Casos de uso (lógica de negócio)
│   │   └── product.py
│   ├── schemas/               # Schemas Pydantic
│   │   └── product.py
│   ├── models/                # Modelos de dados
│   │   └── product.py
│   └── db/                    # Configuração do banco de dados
│       └── mongo.py
├── tests/                     # Testes automatizados
│   ├── test_product_schema.py
│   └── test_product_usecase.py
├── main.py                    # Ponto de entrada da aplicação
├── pyproject.toml            # Configuração do Poetry
├── docker-compose.yml        # Configuração do Docker
├── Dockerfile               # Imagem Docker da aplicação
└── README.md               # Este arquivo
```

## 🔧 Como Executar o Projeto

### Pré-requisitos

- Python 3.11+
- Poetry (opcional, mas recomendado)
- Docker e Docker Compose (para MongoDB)

### 1. Clonar o Repositório

```bash
git clone <seu-repositorio>
cd my_store_api
```

### 2. Instalar Dependências

#### Com Poetry:
```bash
poetry install
poetry shell
```

#### Com pip:
```bash
pip install fastapi uvicorn pydantic pydantic-settings motor pytest pytest-asyncio httpx
```

### 3. Executar MongoDB

```bash
docker compose up -d mongodb
```

### 4. Executar a Aplicação

```bash
python main.py
```

A API estará disponível em: `http://localhost:8000`

### 5. Acessar a Documentação

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🧪 Executar Testes

```bash
# Executar todos os testes
pytest

# Executar com verbose
pytest -v

# Executar testes específicos
pytest tests/test_product_schema.py -v
```

## 📚 Exemplos de Uso da API

### Criar um Produto

```bash
curl -X POST "http://localhost:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Smartphone Samsung Galaxy",
    "description": "Smartphone com 128GB de armazenamento e câmera de 64MP",
    "price": 1500.00,
    "category": "Eletrônicos"
  }'
```

### Listar Produtos com Filtros

```bash
# Buscar produtos por nome
curl "http://localhost:8000/products/?name=smartphone"

# Buscar produtos por faixa de preço
curl "http://localhost:8000/products/?min_price=1000&max_price=2000"

# Buscar com paginação
curl "http://localhost:8000/products/?skip=0&limit=5"
```

### Buscar Produto por ID

```bash
curl "http://localhost:8000/products/{product_id}"
```

### Atualizar Produto

```bash
curl -X PATCH "http://localhost:8000/products/{product_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Produto Atualizado",
    "price": 1800.00
  }'
```

### Deletar Produto

```bash
curl -X DELETE "http://localhost:8000/products/{product_id}"
```

## 🎨 Modificações Implementadas

Este projeto implementa as seguintes melhorias em relação ao desafio original:

### 1. **Tratamento de Exceções Aprimorado**
- Exceções personalizadas (`ProductNotFoundError`, `ProductCreateError`)
- Mensagens de erro mais detalhadas e amigáveis
- Tratamento adequado nos controllers com códigos HTTP apropriados

### 2. **Filtros de Busca Avançados**
- Filtro por nome (busca case-insensitive)
- Filtro por categoria
- Filtro por faixa de preço (implementando o desafio: price > 5000 and price < 8000)
- Paginação com `skip` e `limit`

### 3. **Validações Robustas**
- Validação de preços (não podem ser negativos ou zero)
- Validação de faixa de preços (max_price >= min_price)
- Validação de limites de paginação
- Validação de tamanhos de campos

### 4. **Atualização Automática de Timestamps**
- Campo `updated_at` é automaticamente atualizado em operações PATCH
- Preservação do `created_at` original

### 5. **Arquitetura Limpa**
- Separação clara entre controllers, use cases, schemas e models
- Injeção de dependências com FastAPI
- Código mais legível e manutenível

## 🧪 Filosofia TDD Aplicada

O projeto foi desenvolvido seguindo os princípios do TDD:

1. **Red**: Escrever um teste que falha
2. **Green**: Escrever o código mínimo para o teste passar
3. **Refactor**: Melhorar o código mantendo os testes passando

### Tipos de Testes Implementados:

- **Testes de Schema**: Validação dos modelos Pydantic
- **Testes de Use Case**: Lógica de negócio com mocks
- **Testes de Integração**: (Podem ser adicionados com MongoDB de teste)

## 🚀 Próximos Passos

Funcionalidades que podem ser implementadas:

- [ ] Autenticação e autorização
- [ ] Categorias como entidade separada
- [ ] Upload de imagens para produtos
- [ ] Cache com Redis
- [ ] Logs estruturados
- [ ] Métricas e monitoramento
- [ ] Testes de integração com MongoDB de teste
- [ ] CI/CD pipeline

## 🤝 Contribuições

Este é um projeto educacional desenvolvido como parte do desafio da DIO. Sugestões e melhorias são bem-vindas!

## 📄 Licença

Este projeto é desenvolvido para fins educacionais como parte do curso da Digital Innovation One (DIO).

---

**Desenvolvido com ❤️ por um aluno da DIO aplicando TDD na prática!**

