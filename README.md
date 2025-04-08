<p align="center">
    <img src="assets/logo.png" alt="copilot_free logo" width="300"/>
</p>
<div align="center">
    Assistente de codigo ia offline
</div>

## Baixado repositorio

1. Faça um git clone:
    ```bash
    git clone https://github.com/Lucas-Brum/copilot_free.git
    ```

## Ambiente Virtual

Recomenda-se criar um ambiente virtual com python3.8    
para isolar as dependências do projeto. Siga os passos abaixo:

1. Crie o ambiente virtual:
    ```bash
    python3 -m venv venv
    ```
2. Ative o ambiente virtual:
    - No Linux/MacOS:
        ```bash
        source venv/bin/activate
        ```
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```

3. Instale as dependências no ambiente virtual:
    ```bash
    pip install -r requirements.txt
    ```
4. instale o ollama caso ainda n tenha instalado:

    https://ollama.com/download

5. instale o modelo que vai querer usar caso ainda não tenha:

    https://ollama.com/search

5. Crie um arquivo settings.txt (Ou o modelo ollama que tiver instalado)
    ```bash
    OLLAMA_URL = http://localhost:11434/api/generate
    MODEL_NAME = qwen2.5:3b
    ```