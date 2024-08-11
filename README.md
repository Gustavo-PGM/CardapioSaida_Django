# Sistema de Cardápio e Ordem de Saída da EEEP Adolfo Ferreira de Sousa

Sistema desenvolvido em Django para gerenciar o cardápio escolar e a ordem de saída das turmas. Oferece uma interface intuitiva para visualizar e atualizar essas informações, otimizando a organização e o planejamento diário.

## Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)
- virtualenv (opcional, mas recomendado)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Gustavo-PGM/CardapioSaida_Django.git

2. **Crie um ambiente virtual e ative-o (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt

4. **Configure o banco de dados:**

   Execute as migrações para configurar o banco de dados:

    ```bash
     python manage.py makemigrations
     python manage.py migrate


5. **Inicie o servidor de desenvolvimento:**

   ```bash
    python manage.py runserver

    O sistema estará disponível em http://127.0.0.1:8000/.

6. **Estrutura de Pastas:**
   
   ```bash
     core/: Código do sistema, incluindo configurações e URLs.
     app/: Código do sistema, incluindo modelos, visualizações e URLs.
     static/: Arquivos estáticos como CSS, JavaScript e imagens.
     media/: Arquivos carregados pelo usuário, como documentos e imagens.
     templates/: Templates HTML usados para renderizar as páginas.
     requirements.txt: Lista de dependências do projeto.
     manage.py: Script de gerenciamento do Django.

Contato
Se tiver dúvidas ou precisar de ajuda, abra uma issue no GitHub ou entre em contato com gustavo.cavalcante.gomes06@gmail.com.

Esse `README.md` cobre a instalação, estrutura do projeto, e como contribuir. Você pode ajustar conforme necessário para se adequar aos detalhes específicos do seu projeto.

