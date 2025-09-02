# 🤖 Study of Artificial Intelligence (AI)

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/PYTHON-000000?style=for-the-badge&logo=python&logoColor=facc56" alt="Python"></a>
<a href="https://www.langchain.com/"><img src="https://img.shields.io/badge/LANGCHAIN-000000?style=for-the-badge&logo=langchain&logoColor=203c3c" alt="LangChain"></a>
<a href="https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br/"><img src="https://img.shields.io/badge/GEMINI-000000?style=for-the-badge&logo=googlegemini&logoColor=5088ea" alt="Google Gemini"></a>

Esse repositório é destinado ao estudo de inteligência artificial com Python e LangChain, com a utilização da API do Google Gemini, visando conhecer melhor os conceitos que cercam essa vasta área da tecnologia mundial.

Além disso, ressalta-se que o conhecimento adquirido é fruto da dedicação e disponibilização do curso **[Introdução a LLMs](https://ticemtrilhas.org.br/trail/4dc77e6f-a048-4bea-9d5e-de4890d31b9b)** da plataforma
**[TIC em Trilhas](https://ticemtrilhas.org.br/#anchor-about)**. Meus agradecimentos ao _[Alberto Sardinha](https://www.inf.puc-rio.br/blog/professor/alberto-sardinha/)_ e _[Felipe P. Kestelman](https://www.linkedin.com/in/felipe-procaci-kestelman/)_.

### 🧠 Progresso de Estudo
O progresso de estudo deste repositório é relacionado a estrutura de aulas disponibilizada pelo curso, sendo três módulos composto cada por quatro aulas em versão escrita com atividade avaliativa e práticas da seguinte maneira:

- [x] Módulo 1 | Modelos de linguagem - fundamentos e funcionamento
  - [x] Como um computador aprendeu a escrever? 1.1
  - [x] Palavras e frases são números - Embeddings 1.2
  - [x] Transformers - o cérebro dos LLMs 1.3
  - [x] Redes neurais, um cérebro digital 1.4
- [ ] Módulo 2 | Introdução ao LangChain
  - [ ] Como usar um LLM em código? 2.1
  - [ ] LangChain - esqueleto de uma aplicação com LLMs 2.2
  - [ ] Conversando com LLMs por código 2.3
  - [ ] Passando PDFs para um LLM 2.4
- [ ] Módulo 3 | Desenvolvimento de uma aplicação com LLMs
  - [ ] ??? 3.1
  - [ ] ??? 3.2
  - [ ] ??? 3.3
  - [ ] ??? 3.4

>[!important]  Aproveite o conhecimento, passe por todas as trilhas calmamente e ao final, obtenha uma certificação totalmente gratuita.

## 💻 Pré-requisitos
Para adiantar uma etapa, antes de iniciar o curso, verifique se você possui todos os requisitos:

- Você possui instalado uma versão estável da linguagem `python`.
- Você possui instalado um ambiente de desenvolvimento, como `Visual Studio Code` ou outro de sua preferência.
- Certifique-se de possuir uma `API KEY` de alguma plataforma de IA, como Gemini e/ou OpenAI.
- Certifique-se de possuir todas as dependências que coincidirem com a sua opção de estudo. Caso contrário, verifique a seção `🚀 Instalando as dependências`.

>[!important] Não é necessário adicionar a API KEY nas suas variáveis de ambiente, basta utilizar o dotenv.

## 🚀 Instalando as dependências
Para instalar as dependências do curso, basta abrir o terminal e copiar as seguintes linhas de código:

*Se for utilizar a API KEY da OpenAI:*
```
pip install openai
```

*Se for utilizar a API KEY da Gemini:*
```
pip install -q -U google-genai
```

*LangChain para OpenAI:*
```
pip install -qU "langchain[openai]"
```

*LangChain para Gemini:*
```
pip install -qU "langchain[google-genai]"
```

*LangGraph:*
```
pip install langgraph
```

>[!important] Execute cada linha individualmente e certifique que a instalação foi realizada com sucesso.

## 📝 References
**PYTHON SOFTWARE FOUNDATION**. Disponível em: https://www.python.org/. Acesso em: 1 set. 2025.

**LANGCHAIN**. Disponível em: https://python.langchain.com/docs/introduction/. Acesso em: 1 set. 2025.

**LANGCHAIN. LangGraph.** Disponível em: https://langchain-ai.github.io/langgraph/concepts/why-langgraph/. Acesso em: 1 set. 2025.

**GOOGLE. Documentação da API Gemini.** Disponível em: https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br/. Acesso em: 1 set. 2025.

**OPENAI. Libraries.** Disponível em: https://platform.openai.com/docs/libraries?language=python. Acesso em: 1 set. 2025.

**TICEMTRILHAS. About.** Disponível em: https://ticemtrilhas.org.br/#anchor-about. Acesso em: 1 set. 2025.