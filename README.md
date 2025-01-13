# Projeto Jornaleiro

## Objetivo
Desenvolver uma ferramenta que monitore sites de notícias cadastrados pelo usuário, oferecendo funcionalidades avançadas para visualização, categorização e análise das notícias publicadas.

## Funcionalidades Principais

1. **Monitoramento de Sites de Notícias**
   - O programa será capaz de monitorar os sites de notícias cadastrados pelos usuários.
   - A ferramenta verificará regularmente esses sites em intervalos configuráveis para identificar novas publicações.
   - Será possível cadastrar um endereço RSS para sites que oferecem esse recurso.
   - Para sites sem RSS, a ferramenta usará `BeautifulSoup` e `Requests` para realizar a extração das notícias.
   - Sistema de logs integrado para rastrear erros e desempenho, com exclusão automática dos arquivos mais antigos para evitar sobrecarga de dados (ex.: uso de Loguru).
   - Configuração de alertas para monitorar falhas no scraping ou problemas de API. O scraping de sites com falhas será adiado para a próxima sessão de monitoramento, com notificações ao usuário sobre o erro.

2. **Exibição de Listas de Notícias**
   - Listagem de títulos das notícias organizadas por veículo cadastrado.
   - Configuração customizável do período de exibição.

3. **Categorização e Análise Automática**
   - **Categorização automática**: As notícias serão classificadas em editorias automaticamente.
   - **Identificação de palavras-chave**: Utilizando Stanza e técnicas adicionais de frequência.
   - **Identificação de entidades nomeadas**: Reconhecimento automático de nomes, locais, organizações, etc., utilizando Stanza.
   - **Agrupamento de notícias**: Notícias relacionadas a um mesmo assunto serão agrupadas utilizando Gensim para modelagem de tópicos e similaridade.

4. **Estatísticas e Contadores**
   - Exibição de dados estatísticos, como:
     - Assuntos mais abordados, extraídos com Gensim (modelagem de tópicos).
     - Editorias com maior número de notícias.
     - Entidades mais mencionadas, identificadas com Stanza.

5. **Configurações Customizáveis**
   - Intervalos de monitoramento definidos pelo usuário.
   - Personalização de notificações e ajustes para scraping.

## Ferramentas e Tecnologias

- **Linguagem de Programação**: Python.
- **Backend**: FastAPI.
- **Banco de Dados**: PostgreSQL.
- **Frontend**: React (ou template leve em HTML/CSS/JS).
- **Outras Bibliotecas**:
  - `Stanza`: Tokenização, lematização, reconhecimento de entidades nomeadas (NER).
  - `Gensim`: Modelagem de tópicos e agrupamento de notícias.
  - `BeautifulSoup` e `Requests`: Raspagem de sites sem suporte a RSS.
  - `Loguru`: Gerenciamento de logs.
  - `APScheduler`: Agendamento de tarefas recorrentes.

## Requisitos Técnicos

### Backend
- API REST para comunicação com o frontend.
- Validação automática de URLs e RSS cadastrados.
- Logs integrados para rastrear erros e desempenho.
- Sistema de fallback para lidar com falhas no scraping.
- Integração com Stanza para análise de texto.
- Uso de Gensim para agrupamento e modelagem de tópicos.

### Frontend
- Interface web responsiva.
- Gráficos interativos usando Chart.js ou Plotly.
- Tabelas dinâmicas para visualização de listas de notícias.

### Infraestrutura
- Deploy em serviços como Heroku ou AWS.
- Docker para gerenciamento de ambientes e deploy local.
- Segurança das APIs com autenticação JWT e HTTPS.

### Testes
- Testes unitários e de integração com Pytest.
- Funcionalidade para o usuário testar e ajustar o scraping antes de salvar o cadastro de sites.

## Próximos Passos

### 1. Preparação do Ambiente de Trabalho
- Configurar o ambiente local com Python e bibliotecas necessárias.
- Criar repositório GitHub para versionamento.
- Configurar Docker e ferramentas de linting (Black, Flake8).

### 2. Desenvolvimento do Backend
- Implementar endpoints para monitoramento, categorização e estatísticas.
- Desenvolver integração com Stanza para tokenização, lematização e reconhecimento de entidades.
- Usar Gensim para modelagem de tópicos e agrupamento de notícias relacionadas.
- Desenvolver lógica de fallback para scraping em sites sem RSS.
- Configurar banco de dados e validação de cadastros de RSS.
- Escrever e executar testes unitários e de integração.

### 3. Desenvolvimento do Frontend
- Planejar e prototipar fluxos de interface.
- Conectar frontend às APIs REST do backend.
- Implementar visualizações de dados e listas de notícias.

### 4. Finalização e Publicação
- Realizar testes integrados entre frontend e backend.
- Corrigir bugs e otimizar o desempenho.
- Fazer o deploy e divulgar o projeto para usuários iniciais.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).
