# Common Core v0.1

Base mínima modular para proyectos de AI, IoT y aplicaciones generativas.

## Estructura
- `core/` → configuración, logging, agentes base, utilidades
- `settings.yaml` → configuración central
- `tests/` → validación con pytest
- `Makefile` → tareas locales (test, lint, run)

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
└── README.md

```

## Run

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


