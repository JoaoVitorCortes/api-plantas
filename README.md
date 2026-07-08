# 🌱 API de Catálogo de Plantas

Uma API REST para cadastrar, organizar e acompanhar as necessidades de cuidado das suas plantas — com cálculo automático de quando cada uma precisa ser regada.

Projeto desenvolvido como estudo prático de **FastAPI**, **Pydantic** e **MongoDB (via Beanie ODM)**, seguindo uma arquitetura em camadas.

---

## 🎯 Sobre o projeto

Quem tem plantas em casa sabe: cada espécie tem uma necessidade diferente de rega, luz e ambiente, e é fácil perder o controle de qual planta precisa de cuidado e quando. Este projeto nasceu como uma solução simples para esse problema — um catálogo pessoal onde cada planta cadastrada informa automaticamente se já está na hora de regar.

Mais do que uma aplicação funcional, este projeto foi construído como exercício de aprendizado de **arquitetura em camadas** aplicada a uma API real, com ênfase em separação de responsabilidades, validação de dados e boas práticas com bancos NoSQL.

---

## ✨ Funcionalidades

- ✅ Cadastrar uma nova planta (nome, espécie, frequência de rega, exposição solar, ambiente)
- ✅ Listar todas as plantas cadastradas
- ✅ Buscar uma planta específica por ID
- ✅ Editar uma planta (atualização parcial — só os campos enviados são alterados)
- ✅ Remover uma planta do catálogo
- ✅ Marcar uma planta como **regada**, atualizando a data da última rega
- ✅ Cálculo automático do campo `precisa_de_rega`, comparando a frequência ideal de rega com a data da última rega registrada

---

## 🏗️ Arquitetura

O projeto segue uma **arquitetura em camadas**, onde cada parte do código tem uma responsabilidade única e bem definida:

```
Cliente (requisição HTTP)
        │
        ▼
  Controller (rotas.py)      → recebe a requisição, delega para o service
        │
        ▼
   Services (servicos.py)    → aplica as regras de negócio
        │
        ▼
    Model (modelos.py)       → conversa com o MongoDB via Beanie
        │
        ▼
      MongoDB
```

Essa separação torna o código mais fácil de manter, testar e evoluir — por exemplo, seria possível trocar o banco de dados sem alterar a lógica de negócio, já que o _service_ nunca acessa o banco diretamente.

### Estrutura de pastas

```
app/
├── controller/
│   └── rotas.py          # Endpoints da API
├── model/
│   ├── database.py        # Conexão com o MongoDB
│   └── modelos.py         # Documents (Beanie) e operações de banco
├── services/
│   └── servicos.py        # Regras de negócio
├── utils/
│   ├── constantes.py
│   ├── data_atual.py       # Geração de datas
│   └── parser.py           # Conversão entre Document e schema de resposta
├── views/
│   └── validacoes.py       # Schemas Pydantic (entrada e saída)
├── __init__.py
└── main.py                 # Ponto de entrada da aplicação
```

---

## 🛠️ Tecnologias utilizadas

| Tecnologia                                               | Papel no projeto                                             |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| [FastAPI](https://fastapi.tiangolo.com/)                 | Framework web assíncrono, geração automática de documentação |
| [Pydantic](https://docs.pydantic.dev/)                   | Validação e tipagem dos dados de entrada e saída             |
| [MongoDB](https://www.mongodb.com/)                      | Banco de dados NoSQL, hospedado no MongoDB Atlas             |
| [Beanie](https://beanie-odm.dev/)                        | ODM assíncrono para modelar e persistir dados no MongoDB     |
| [Uvicorn](https://www.uvicorn.org/)                      | Servidor ASGI para rodar a aplicação                         |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Gerenciamento de variáveis de ambiente                       |

---

## 🚀 Como rodar o projeto

### Pré-requisitos

- Python 3.11 ou 3.12
- Uma conta no [MongoDB Atlas](https://www.mongodb.com/atlas) (camada gratuita já é suficiente)

### Passo a passo

**1. Clone o repositório**

```bash
git clone https://github.com/JoaoVitorCortes/api-plantas.git
cd API-Plantas
```

**2. Crie e ative um ambiente virtual**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto, baseado no `.env.example`:

```env
MONGO_URI=sua_string_de_conexao_aqui
DATABASE_NAME=plantas_db
```

> ⚠️ No MongoDB Atlas, lembre-se de liberar seu IP em **Network Access** para conseguir conectar.

**5. Rode a aplicação**

```bash
uvicorn app.main:app --reload
```

**6. Acesse a documentação interativa**

Com o servidor rodando, abra no navegador:

```
http://127.0.0.1:8000/docs
```

Ali você encontra todos os endpoints disponíveis, já com uma interface pronta para testar cada um (Swagger UI).

---

## 📋 Endpoints

| Método   | Rota                  | Descrição                              |
| -------- | --------------------- | -------------------------------------- |
| `POST`   | `/plantas/`           | Cadastra uma nova planta               |
| `GET`    | `/plantas/`           | Lista as plantas cadastradas           |
| `GET`    | `/plantas/{id}`       | Busca uma planta específica            |
| `PUT`    | `/plantas/{id}`       | Edita uma planta (atualização parcial) |
| `PATCH`  | `/plantas/{id}/regar` | Marca a planta como regada agora       |
| `DELETE` | `/plantas/{id}`       | Remove uma planta                      |

### Exemplo de requisição — cadastrar planta

```json
POST /plantas/

{
  "nome": "Jiboia",
  "especie": "Epipremnum aureum",
  "frequencia_rega_dias": 4,
  "exposicao_solar": "sombra parcial",
  "ambiente": "interno",
  "observacoes": "Fácil de cuidar, ideal para iniciantes"
}
```

### Exemplo de resposta

```json
{
  "id": "6a4c4647519942d3d77c12f0",
  "nome": "Jiboia",
  "especie": "Epipremnum aureum",
  "frequencia_rega_dias": 4,
  "exposicao_solar": "sombra parcial",
  "ambiente": "interno",
  "observacoes": "Fácil de cuidar, ideal para iniciantes",
  "criado_em": "2026-07-05T21:25:06.664547",
  "atualizado_em": "2026-07-05T21:25:06.664547",
  "precisa_de_rega": false
}
```

---

## 🧠 Principais aprendizados neste projeto

- Separação de responsabilidades entre camadas (controller, service, model)
- Diferença entre schemas de entrada e saída, e por que eles não devem ser o mesmo objeto
- Validação de dados com Pydantic, incluindo atualização parcial (`exclude_unset`)
- Modelagem de documentos assíncronos com Beanie e MongoDB
- Tratamento de erros HTTP (404) de forma explícita, evitando falhas silenciosas
- Cuidado com migração de schema em bancos NoSQL, quando a estrutura dos dados muda ao longo do desenvolvimento

---

## 🔮 Próximos passos

- [ ] Notificações automáticas para lembrar da rega
- [ ] Busca de espécies em catálogo externo (informações de cuidado de plantas que o usuário ainda não possui)
- [ ] Upload e associação de imagens às plantas cadastradas
- [ ] Autenticação de usuários, para suportar múltiplos catálogos pessoais
- [ ] Interface visual (web ou mobile) como alternativa ao Swagger

---

## 📝 Licença

Projeto de estudo, livre para uso e adaptação.
