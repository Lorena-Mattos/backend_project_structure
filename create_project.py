import os


def create_backend_structure(project_name):
    base_path = r"C:\Users\Dell\OneDrive - Dadoteca\Área de Trabalho"
    project_path = os.path.join(base_path, project_name)

    base_structure = {
        "app": [
            "models",
            "views",
            "controllers",
            "services",
        ],
        "config": [],
        "migrations": [],
        "tests": [
            "unit",
            "integration",
        ],
        "docs": [],
        "public": ["css", "js", "images"],
    }

    files = [
        ("main.py", """# Arquivo principal do projeto
            if __name__ == "__main__":
            print("Bem-vindo ao projeto {project_name}!")
            # Insira aqui o código para inicializar a aplicação.
                            """),
        ("app/__init__.py", ""),
        ("app/models/__init__.py", ""),
        ("app/views/__init__.py", ""),
        ("app/controllers/__init__.py", ""),
        ("app/services/__init__.py", ""),
        ("config/settings.py", "# Configurações do projeto"),
        ("requirements.txt", "# Adicione suas dependências aqui"),
        ("README.md", f"""# {project_name}

## Sobre o Projeto
Este é um projeto backend com uma estrutura organizada e modular para facilitar a manutenção e escalabilidade.

---

## Estrutura do Projeto

```
meu_projeto/
├── main.py
├── app/
│   ├── models/
│   ├── views/
│   ├── controllers/
│   ├── services/
│   └── __init__.py
├── config/
├── migrations/
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
├── public/
│   ├── css/
│   ├── js/
│   └── images/
├── README.md
└── requirements.txt
```

---
## Descrição das Pastas e Arquivos

### **main.py**
Arquivo principal do projeto, usado para inicializar a aplicação.

### **app/**
Contém os componentes principais do sistema:
- **models/**: Modelos de dados ou lógica de negócio.
- **views/**: Camada de visualização ou APIs.
- **controllers/**: Lógica de controle do sistema.
- **services/**: Funções auxiliares reutilizáveis.

### **config/**
Configurações gerais do projeto.

### **migrations/**
Scripts de migração de banco de dados.

### **tests/**
Testes automatizados:
- **unit/**: Testes unitários.
- **integration/**: Testes de integração.

### **docs/**
Documentação do projeto.

### **public/**
Arquivos estáticos, como CSS, JavaScript e imagens.

### **requirements.txt**
Lista de dependências do projeto.

### **README.md**
Arquivo de documentação principal do projeto.
                                                """),
        (".gitignore", "*.pyc\n__pycache__/\n.env"),
    ]

    # Criar a pasta base do projeto
    os.makedirs(project_path, exist_ok=True)

    # Criar a estrutura de pastas
    for folder, subfolders in base_structure.items():
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for subfolder in subfolders:
            os.makedirs(os.path.join(folder_path, subfolder), exist_ok=True)

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
