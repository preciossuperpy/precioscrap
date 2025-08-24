# Ejemplo: pylint en GitHub Actions (umbral 9.5, todo el repo)

![Estado](https://github.com/preciossuperpy/precioscrap/actions/workflows/lint.yml/badge.svg)

Este ejemplo ejecuta **pylint** sobre **todos los archivos .py rastreados por git** y
falla si el puntaje global es **< 9.5**.

## Estructura
```
.
├── .github/
│   └── workflows/
│       └── lint.yml
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       └── aritmetica.py
├── .pylintrc
├── requirements.txt
└── README.md
```

## Uso local
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pylint $(git ls-files '*.py')
```

## CI/CD
El workflow `lint.yml` instala dependencias y ejecuta:
```bash
pylint --fail-under=9.5 $(git ls-files '*.py')
```

### Notas
- Si no hay archivos `.py` rastreados por git, el job termina sin error.
- Ajusta el umbral cambiando `--fail-under=9.5` en `.github/workflows/lint.yml`.
- Para excluir rutas no rastreadas (e.g., `venv/`), no es necesario; `git ls-files` ya ignora lo no rastreado.
