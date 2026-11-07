# Resolve Nova Esperança

Plataforma web para registrar e acompanhar problemas urbanos na cidade fictícia de Nova Esperança. O projeto foi desenvolvido como um MVP para o tema **Cidades Inteligentes e Sustentabilidade Local**, aproximando moradores e órgãos públicos por meio da tecnologia.

## O problema

Problemas como buracos nas ruas, iluminação pública danificada, descarte irregular de lixo e vazamentos afetam a qualidade de vida e a sustentabilidade da cidade. Sem um canal organizado, é difícil para os moradores comunicar essas ocorrências e acompanhar o que acontece com cada solicitação. Ao mesmo tempo, equipes e recursos limitados tornam importante organizar as demandas por categoria e urgência.

## A solução

O Resolve Nova Esperança permite que o cidadão abra um chamado com as informações necessárias para identificar o problema e acompanhe seu andamento. Cada chamado pode ser associado a uma categoria vinculada a um órgão, ajudando a organizar as solicitações. A prioridade informada também pode apoiar a análise das demandas.

### Funcionalidades

- Cadastro e login de usuários.
- Registro de chamados com título, descrição, categoria, endereço e prioridade.
- Anexo opcional de foto do local.
- Lista dos chamados do cidadão autenticado, com protocolo, data e informações do problema.
- Acompanhamento do status: **Aberto**, **Em andamento** ou **Concluído**.
- Filtros e contagem de chamados por status na página “Meus chamados”.
- Cadastro e administração de órgãos, categorias e atualizações de chamados pelo painel administrativo do Django (`/admin`).

## Público e funcionamento

O público principal são moradores que precisam informar problemas urbanos e equipes responsáveis por organizar e atualizar as solicitações.

1. O morador cria uma conta e entra na plataforma.
2. Abre um chamado, descrevendo o problema, selecionando uma categoria e informando o endereço e a urgência. Se quiser, anexa uma foto.
3. O chamado fica disponível em “Meus chamados”, onde o morador pode acompanhar o status.
4. A equipe responsável consulta os registros pelo painel administrativo e atualiza o andamento da solicitação.

## Impacto esperado

Um canal centralizado pode facilitar a comunicação entre cidadãos e administração, dar visibilidade às solicitações e ajudar a organizar o atendimento de acordo com categoria e prioridade. A proposta contribui para uma cidade mais participativa e sustentável, sem pressupor que todos os problemas urbanos sejam resolvidos pela plataforma.

## Tecnologias

- Python
- Django
- SQLite
- HTML e CSS

## Uso de Inteligência Artificial

Durante o desenvolvimento do **Resolve Nova Esperança**, utilizamos a Inteligência Artificial como apoio ao processo de desenvolvimento.

A IA foi utilizada principalmente para:

- **Desenvolvimento dos templates:** auxílio na criação e estruturação das páginas HTML da aplicação.
- **Estilização das páginas:** sugestões de organização visual e melhorias nos arquivos CSS.
- **Apoio ao código:** sugestões de melhorias e esclarecimento de dúvidas relacionadas ao Python e Django.

As sugestões fornecidas pela IA foram analisadas, adaptadas e implementadas pela equipe, que também ficou responsável pelos testes e validação das funcionalidades.

A Inteligência Artificial foi utilizada como ferramenta de apoio, contribuindo para agilizar o desenvolvimento, sem substituir o aprendizado e a participação dos integrantes no projeto.

## Estrutura de pastas

```text
|   .gitignore
|   db.sqlite3
|   estrutura.txt
|   instrucoes.md
|   manage.py
|   README.md
|   requirements.txt
|   
+---main
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   wsgi.py
|   |   __init__.py
|   |   
|   \---__pycache__
|           settings.cpython-314.pyc
|           urls.cpython-314.pyc
|           wsgi.cpython-314.pyc
|           __init__.cpython-314.pyc
|           
+---sistema
|   |   admin.py
|   |   apps.py
|   |   forms.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   +---migrations
|   |   |   0001_initial.py
|   |   |   0002_remove_chamado_status.py
|   |   |   0003_administrarchamado.py
|   |   |   0004_chamado_cidadao_alter_administrarchamado_usuario.py
|   |   |   0005_chamado_status.py
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           0001_initial.cpython-314.pyc
|   |           0002_remove_chamado_status.cpython-314.pyc
|   |           0003_administrarchamado.cpython-314.pyc
|   |           0004_chamado_cidadao_alter_administrarchamado_usuario.cpython-314.pyc
|   |           0005_chamado_status.cpython-314.pyc
|   |           __init__.cpython-314.pyc
|   |           
|   +---static
|   |   \---css
|   |           adm_dashboard.css
|   |           base.css
|   |           chamados.css
|   |           novo_chamado.css
|   |           
|   +---templates
|   |       adm_dashboard.html
|   |       base.html
|   |       chamados.html
|   |       conteudo_base.html
|   |       navbar.html
|   |       novo_chamado.html
|   |       
|   \---__pycache__
|           admin.cpython-314.pyc
|           apps.cpython-314.pyc
|           forms.cpython-314.pyc
|           models.cpython-314.pyc
|           urls.cpython-314.pyc
|           views.cpython-314.pyc
|           __init__.cpython-314.pyc
|           
+---users
|   |   admin.py
|   |   apps.py
|   |   forms.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   +---migrations
|   |   |   0001_initial.py
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           0001_initial.cpython-314.pyc
|   |           __init__.cpython-314.pyc
|   |           
|   +---static
|   |   \---css
|   |           login.css
|   |           logout.css
|   |           register.css
|   |           
|   +---templates
|   |       login.html
|   |       logout.html
|   \---      register.html
```

## Como executar localmente

É necessário ter Python instalado em uma versão compatível com Django 6.1.3.

No PowerShell, na pasta do projeto:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Depois, acesse:

- Aplicação: http://127.0.0.1:8000/
- Administração: http://127.0.0.1:8000/admin/

No painel administrativo, cadastre ao menos um **órgão** e uma **categoria** associada a ele para que as opções estejam disponíveis ao abrir chamados. Use uma conta administrativa para cadastrar e atualizar registros de atendimento.

## Integrantes

NOME: Joao Schulz
RGM: 114.044

NOME: Alex Vinícius
RGM: 114.056

NOME: Ellian Calebe
RGM: 114.023
