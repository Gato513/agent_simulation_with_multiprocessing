#!/bin/bash
# Crear el entorno virtual con la versión de Python correcta
python3.11 -m venv .venv

# Activar el entorno
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

echo ""
echo "✓ Entorno listo. Para correr el simulador:"
echo "  source .venv/bin/activate"
echo "  python main.py"
