#!/bin/bash
# Quick start script for Free Media Converter Web Interface

echo "🎵🎬 Free Media Converter - Web Interface"
echo "========================================"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    echo "💡 Instala Python 3 y vuelve a intentar"
    exit 1
fi

# Check if FFmpeg is available
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  Advertencia: FFmpeg no está instalado"
    echo "💡 Instala FFmpeg para que la aplicación funcione correctamente:"
    echo "   Ubuntu/Debian: sudo apt install ffmpeg"
    echo "   macOS: brew install ffmpeg"
    echo ""
fi

# Check if virtual environment exists
if [ ! -d "../.venv" ]; then
    echo "📦 Creando entorno virtual..."
    cd .. && python3 -m venv .venv && cd web
fi

# Activate virtual environment and install dependencies
echo "📦 Instalando dependencias..."
source ../.venv/bin/activate
pip install -r ../requirements.txt

echo ""
echo "🌐 Iniciando servidor web..."
echo "📍 La aplicación estará disponible en: http://localhost:5001"
echo "🛑 Presiona Ctrl+C para detener el servidor"
echo ""

# Start the web application
python app.py
