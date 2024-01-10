# Projeto de Repositório de TCCs com Django

Este projeto é um repositório de Trabalhos de Conclusão de Curso (TCCs) desenvolvido com o framework Django.

## Configuração do Projeto

Siga as etapas abaixo para configurar o ambiente de desenvolvimento:

1. **Clone o repositório**
    ```
    git clone https://github.com/tatianysouza/TCCs-Django.git
    ```

2. **Configurando o Ambiente Virtual**

    1. **Instale o pacote virtualenv**
        Se você ainda não tem o pacote `virtualenv` instalado, você pode instalá-lo com o seguinte comando:
        ```
        pip install virtualenv
        ```

    2. **Crie o ambiente virtual**
        No diretório do projeto, crie um ambiente virtual chamado `venv` com o seguinte comando:
        ```
        python -m venv .venv
        ```

    3. **Ative o ambiente virtual**
        Depois de criar o ambiente virtual, você precisa ativá-lo. O comando para ativar o ambiente virtual varia dependendo do seu sistema operacional:

        - No Windows:
            ```
            .\.venv\Scripts\activate
            ```

        - No Linux:
            ```
            source .venv/bin/activate
            ```

3. **Instale as dependências**
    Abra o terminal e execute o seguinte comando:
    ```
    pip install -r requirements.txt
    ```

## Configurções do Projeto

1. **Crie um arquivo .env na raiz do projeto** e adicione as seguintes variáveis de ambiente:
    Abra o arquivo `.env` em um editor de texto e adicione suas variáveis de ambiente. Por exemplo:
    ```
    SECRET_KEY=your-secret-key
    DEBUG=True
    DB_NAME=biblioteca
    DB_USER=your-db-user
    DB_PASSWORD=your-db-password
    DB_HOST=localhost
    DB_PORT=5432
    ```

2. **Configure o banco de dados**
    No SGBD PostgreSQL, crie o banco de dados com o nome de "biblioteca". Lembre-se de alterar o USER e o PASSWORD do seu banco no arquivo settings.py.

3. **Realize as migrações**
    Após a criação do banco, realize as migrações para a criação das tabelas no banco de dados. No terminal, execute os seguintes comandos:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Executando o Projeto

Depois de configurar o ambiente e o banco de dados, você pode executar o projeto localmente com o seguinte comando:
```
python manage.py runserver
```

Agora, você deve ser capaz de acessar o aplicativo em seu navegador em `http://localhost:8000`.

## Contribuição

Contribuições são bem-vindas! Por favor, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Suporte

Se você encontrar algum problema ou tiver alguma dúvida sobre este projeto, por favor, abra uma issue no GitHub.
