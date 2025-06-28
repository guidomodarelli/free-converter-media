#!/usr/bin/env python3
"""
Free Audio Converter CLI
Convierte archivos de audio entre diferentes formatos usando FFmpeg.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


def check_ffmpeg():
    """Verifica si FFmpeg está instalado en el sistema."""
    try:
        result = subprocess.run(['ffmpeg', '-version'],
                              capture_output=True, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_supported_formats():
    """Retorna los formatos de audio soportados."""
    return ['mp3', 'wav', 'flac', 'aac', 'm4a', 'ogg', 'wma']


def convert_audio(input_file, output_file, output_format, quality='192k'):
    """
    Convierte un archivo de audio al formato especificado.

    Args:
        input_file (str): Ruta del archivo de entrada
        output_file (str): Ruta del archivo de salida
        output_format (str): Formato de salida (mp3, wav, etc.)
        quality (str): Calidad del audio (bitrate)
    """
    if not os.path.exists(input_file):
        print(f"❌ Error: El archivo '{input_file}' no existe.")
        return False

    # Construir el comando FFmpeg
    cmd = ['ffmpeg', '-i', input_file]

    # Configurar opciones según el formato
    if output_format.lower() == 'mp3':
        cmd.extend(['-codec:a', 'libmp3lame', '-b:a', quality])
    elif output_format.lower() == 'wav':
        cmd.extend(['-codec:a', 'pcm_s16le'])
    elif output_format.lower() == 'flac':
        cmd.extend(['-codec:a', 'flac'])
    elif output_format.lower() == 'aac':
        cmd.extend(['-codec:a', 'aac', '-b:a', quality])
    elif output_format.lower() == 'm4a':
        cmd.extend(['-codec:a', 'aac', '-b:a', quality])
    elif output_format.lower() == 'ogg':
        cmd.extend(['-codec:a', 'libvorbis', '-b:a', quality])

    # Sobrescribir archivo si existe
    cmd.extend(['-y', output_file])

    try:
        print(f"🔄 Convirtiendo '{input_file}' a '{output_file}'...")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Conversión completada exitosamente!")
        print(f"📁 Archivo guardado en: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error durante la conversión:")
        print(f"   {e.stderr}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="🎵 Free Audio Converter - Convierte archivos de audio usando FFmpeg",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python run.py -i audio.wav -o audio.mp3
  python run.py -i song.flac -o song.mp3 -q 320k
  python run.py -i music.m4a -f wav
  python run.py -i audio.wav -f mp3 -q 128k
        """
    )

    parser.add_argument('-i', '--input',
                       help='Archivo de audio de entrada')

    parser.add_argument('-o', '--output',
                       help='Archivo de salida (opcional)')

    parser.add_argument('-f', '--format',
                       choices=get_supported_formats(),
                       default='mp3',
                       help='Formato de salida (default: mp3)')

    parser.add_argument('-q', '--quality',
                       default='192k',
                       help='Calidad del audio - bitrate (default: 192k)')

    parser.add_argument('--list-formats', action='store_true',
                       help='Mostrar formatos soportados')

    args = parser.parse_args()

    # Mostrar formatos soportados
    if args.list_formats:
        print("🎵 Formatos de audio soportados:")
        for fmt in get_supported_formats():
            print(f"   • {fmt.upper()}")
        return

    # Verificar que se especifique archivo de entrada
    if not args.input:
        parser.error("Se requiere especificar un archivo de entrada (-i/--input)")
        return

    # Verificar que FFmpeg esté instalado
    if not check_ffmpeg():
        print("❌ Error: FFmpeg no está instalado o no está en el PATH.")
        print("💡 Instala FFmpeg con:")
        print("   Ubuntu/Debian: sudo apt install ffmpeg")
        print("   Fedora: sudo dnf install ffmpeg")
        print("   Arch: sudo pacman -S ffmpeg")
        print("   macOS: brew install ffmpeg")
        sys.exit(1)

    input_file = args.input
    output_format = args.format.lower()

    # Generar nombre de archivo de salida si no se especifica
    if args.output:
        output_file = args.output
    else:
        input_path = Path(input_file)
        output_file = str(input_path.with_suffix(f'.{output_format}'))

    # Realizar la conversión
    success = convert_audio(input_file, output_file, output_format, args.quality)

    if success:
        # Mostrar información del archivo resultante
        if os.path.exists(output_file):
            size = os.path.getsize(output_file)
            size_mb = size / (1024 * 1024)
            print(f"📊 Tamaño del archivo: {size_mb:.2f} MB")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()