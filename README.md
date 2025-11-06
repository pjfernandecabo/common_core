# Common Core v0.1

Base mínima modular para proyectos de AI, IoT y aplicaciones generativas.

## Estructura modular primaria
- `core/` → configuración, logging, agentes base, utilidades
- `settings.yaml` → configuración central
- `tests/` → validación con pytest
- `Makefile` → tareas locales (test, lint, run)

Un primer esqueleto
```css
/common_core/
├── core/
│   ├── config/               # Carga YAML/TOML + validación con Pydantic
│   ├── logging/              # Logging unificado (JSON + consola)
│   ├── db/                   # Conectores ORM (SQLModel / Mongo / TinyDB)
│   ├── ai/                   # Módulos comunes de IA (RAG, LLM, RL)
│   ├── utils/                # Funciones de sistema, paths, tiempos
│   └── security/             # Auth local, cifrado, tokens internos
│
├── services/
│   ├── api/                  # Endpoints FastAPI base
│   ├── ui/                   # Interfaces (Streamlit, Flask, etc.)
│   ├── tasks/                # Jobs periódicos, colas (Celery, etc.)
│   └── agents/               # Agentes AI o controladores de lógica
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── data/
│   ├── datasets/
│   ├── logs/
│   └── stats/
│
├── settings.yaml
├── main.py                   # Entry point (FastAPI o CLI)
└── README.md

```

## Funcionamiento core-apps

```css
/common_core/
│
├── core/
│   ├── logging/
│   ├── config/
│   └── db/
│
├── tests_core/                  # Tests base compartidos
│   ├── test_logging.py
│   ├── test_config.py
│   └── test_db.py
│
└── pytest.ini                   # Config general de pytest

/app_cctv/
│
├── core/                        # copia o submódulo de common_core
├── tests/
│   ├── test_motion_detection.py
│   └── test_integration_camera.py
└── pytest.ini

```
```css
projects/
├── common_core/
│   ├── pyproject.toml
│   └── runtime.txt        (python-3.10.18)
├── ai_email_agent/
│   ├── pyproject.toml
│   ├── runtime.txt        (python-3.10.18)
│   ├── env_conda.yml      (opcional)
│   └── uv.lock
└── ai_surveillance/
    ├── pyproject.toml
    ├── runtime.txt        (python-3.13.2)
    ├── env_conda.yml
    └── uv.lock

```



Y en Github

```css
/repos/
├── common_core/
│   └── (tests_core/, core/, etc.)
├── app_cctv/
│   └── core/ (submodule -> ../common_core)
└── app_gmail_agent/
    └── core/ (submodule -> ../common_core)

```
Situacion actual V0.1

| Tema                 | Estado actual   | Estrategia                            |
| -------------------- | --------------- | ------------------------------------- |
| Tests automáticos    | Concepto claro  | Crear suite central en `common_core`  |
| Multi-lenguaje       | Python base     | Replicar estructura en Node/TS        |
| Cookiecutter         | Nuevo           | Generará plantillas automáticas       |
| Control de versiones | Necesita setup  | Git + submódulos                      |
| CI/CD                | No implementado | Empezar local con `Makefile` y pytest |


## Manejo versiones Python

| Nivel                    | Qué define            | Dónde se controla            | Herramienta recomendada |
| ------------------------ | --------------------- | ---------------------------- | ----------------------- |
| Python                   | versión base (3.10.x) | `runtime.txt`                | `pyenv` o `uv`          |
| Dependencias comunes     | baseline              | `common_core/pyproject.toml` | Poetry / Hatch / pip    |
| Dependencias específicas | app individual        | `app/pyproject.toml`         | uv o pip                |
| Compatibilidad           | entre core y app      | versionado semántico         | tags y requirements     |



## Version V0.1
```css
common_core_v0.1/
├── core/
│   ├── config_loader.py
│   ├── logger.py
│   ├── base_agent.py
│   ├── utils.py
│   └── __init__.py
│
├── settings.yaml
├── main.py
├── Makefile
├── tests/
│   └── test_core.py
├── README.md
├── pyproject.toml       # o requirements.txt (según el gestor)
├── setup.py             # si es instalable local
├── runtime.txt          # versión de Python base
└── requirements-dev.txt # herramientas de testing, linting
```

## Start & Running

```bash
# activate virtual env
source .common_core_uv/bin/activate
```

```bash
uv run src/main.py
```
or 
```bash
make run
```

```bash
make test
```

```bash
make format
```


---

## ✅ We get

| Component | Goal |
|-------------|------------|
| Config central | Validada con Pydantic |
| Logger común | Estandarizado a nivel app |
| BaseAgent | Patrón unificado de ejecución |
| Utils | Helpers genéricos |
| Tests | Núcleo de CI local |
| Makefile | CI/CD básico |
| settings.yaml | Config declarativa |
| main.py | Entry point común |

---

## V0.1
```css
common_core/ #v0.1
│
├── pyproject.toml
├── README.md
├── setup.py
├── common_core/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings_loader.py
│   │   └── logger.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_ops.py
│   │   ├── json_ops.py
│   │   └── decorators.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── sqlite_client.py
│   │   └── mongo_client.py
│   │
│   └── tests/
│       ├── __init__.py
│       └── test_logger.py
│
├── cookiecutter.json
└── template/
    ├── {{cookiecutter.project_slug}}/
    │   ├── main.py
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── routes/
    │   │   │   └── __init__.py
    │   │   └── core/
    │   │       └── __init__.py
    │   └── settings.yaml
    └── README.md

```
