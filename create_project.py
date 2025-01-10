import os

def create_backend_structure(project_name):
    base_path = r"C:\Users\Dell\OneDrive - Dadoteca\Área de Trabalho"
    project_path = os.path.join(base_path, project_name)

    # Estrutura de pastas
    base_structure = {
        "": ["tests/unit", "tests/integration", "configuration", "route", "controllers", "util"],
    }

    # Arquivos a serem criados
    files = [
        (".env.example", ""),
        ("main.py", """# Arquivo principal do projeto
if __name__ == "__main__":
    print("Bem-vindo ao projeto {project_name}!")
    # Insira aqui o código para inicializar a aplicação.
"""),
        ("requirements.txt", "# Adicione suas dependências aqui"),
        ("README.md", f"""# {project_name}

## Sobre o Projeto
Este é um projeto backend com uma estrutura organizada e modular para facilitar a manutenção e escalabilidade.

---

## Estrutura do Projeto

```
{project_name}/
├── .env.example
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── tests/
│   ├── unit/
│   └── integration/
├── configuration/
│   ├── __init__.py
│   └── configuration.py
├── route/
│   ├── __init__.py
│   └── web_scrapping.py
├── controllers/
│   ├── __init__.py
│   └── controllers.py
├── util/
│   ├── __init__.py
│   └── util.py
```

---

## Descrição das Pastas e Arquivos

### **main.py**
Arquivo principal do projeto, usado para inicializar a aplicação.

### **.env.example**
Exemplo do arquivo de variáveis de ambiente.

### **requirements.txt**
Lista de dependências do projeto.

### **README.md**
Arquivo de documentação principal do projeto.

### **tests/**
Contém os testes automatizados:
- **unit/**: Testes unitários.
- **integration/**: Testes de integração.

### **configuration/**
Contém as configurações gerais do projeto:
- **__init__.py**: Torna o diretório um pacote Python.
- **configuration.py**: Contém as configurações do projeto.

### **route/**
Contém o código para as rotas e web scraping:
- **__init__.py**: Torna o diretório um pacote Python.
- **web_scrapping.py**: Código relacionado a web scraping.

### **controllers/**
Contém a lógica dos controladores do projeto:
- **__init__.py**: Torna o diretório um pacote Python.
- **controllers.py**: Contém a lógica dos controladores.

### **util/**
Contém funções utilitárias do projeto:
- **__init__.py**: Torna o diretório um pacote Python.
- **util.py**: Funções utilitárias.

### **.gitignore**
Lista arquivos e diretórios que devem ser ignorados pelo Git, como arquivos temporários e de cache.
"""),
        (".gitignore", "*.pyc\n__pycache__/\n.env"),
        ("tests/unit/__init__.py", ""),
        ("tests/integration/__init__.py", ""),
        ("configuration/__init__.py", ""),
        ("configuration/configuration.py", "# Configurações do projeto"),
        ("route/__init__.py", ""),
        ("route/web_scrapping.py", "# Código para web scraping"),
        ("controllers/__init__.py", ""),
        ("controllers/controllers.py", "# Código para controladores"),
        ("util/__init__.py", ""),
        ("util/util.py", "# Funções utilitárias"),
    ]

    # Criar a pasta base do projeto
    os.makedirs(project_path, exist_ok=True)

    # Criar a estrutura de pastas
    for root, subfolders in base_structure.items():
        for subfolder in subfolders:
            folder_path = os.path.join(project_path, root, subfolder)
            os.makedirs(folder_path, exist_ok=True)

    # Criar os arquivos com conteúdo padrão
    for file_path, content in files:
        full_path = os.path.join(project_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(content.format(project_name=project_name))

    print(f"Projeto '{project_name}' criado com sucesso em {project_path}!")

# Executar a função
if __name__ == "__main__":
    project_name = input("Digite o nome do projeto: ")
    create_backend_structure(project_name)
