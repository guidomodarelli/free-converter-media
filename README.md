# 🎵🎬 Free Media Converter

**Free Media Converter** es una herramienta de línea de comandos ligera y fácil de usar que te permite convertir archivos de **audio y video** entre distintos formatos utilizando el poder de [FFmpeg](https://ffmpeg.org/).

Diseñado para usuarios que buscan una solución rápida y flexible, este script en Python ofrece:

* 🎧 Conversión entre formatos de audio populares (MP3, WAV, FLAC, AAC, M4A, OGG, WMA)
* 🎥 Soporte para formatos de video comunes (MP4, MKV, AVI, MOV, WebM, entre otros)
* ⚙️ Control de calidad mediante bitrate
* 🚫 Manejo de errores automático y verificación de dependencias
* 🖥️ Interfaz CLI intuitiva para flujos de trabajo rápidos y eficientes

Ideal para creadores de contenido, desarrolladores, podcasters y cualquier persona que necesite convertir medios sin complicaciones.

## 📋 Requisitos

- Python 3.6+
- FFmpeg instalado en el sistema

### Instalación de FFmpeg

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora/Red Hat
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg

# macOS (con Homebrew)
brew install ffmpeg
```

## 🚀 Uso

### Ejemplos básicos

#### 🎵 Conversión de Audio
```bash
# Convertir WAV a MP3 (calidad predeterminada 192k)
python run.py -i audio.wav -o audio.mp3

# Convertir FLAC a MP3 con alta calidad
python run.py -i song.flac -o song.mp3 -q 320k

# Convertir M4A a WAV (sin especificar archivo de salida)
python run.py -i music.m4a -f wav

# Convertir con calidad específica
python run.py -i audio.wav -f mp3 -q 128k
```

#### 🎥 Conversión de Video
```bash
# Convertir AVI a MP4
python run.py -i video.avi -f mp4

# Convertir MKV a MP4 con resolución específica
python run.py -i movie.mkv -o movie.mp4 -q 720p

# Convertir MOV a WebM para web
python run.py -i presentation.mov -f webm
```

### Opciones disponibles

```
-i, --input       Archivo de audio o video de entrada (requerido)
-o, --output      Archivo de salida (opcional)
-f, --format      Formato de salida (default: mp3)
-q, --quality     Calidad - bitrate para audio (192k) o resolución para video (720p)
--list-formats    Mostrar formatos soportados
-h, --help        Mostrar ayuda
```

### Formatos soportados

#### 🎵 Audio
- **MP3** - MPEG Audio Layer III
- **WAV** - Waveform Audio File Format
- **FLAC** - Free Lossless Audio Codec
- **AAC** - Advanced Audio Coding
- **M4A** - MPEG-4 Audio
- **OGG** - Ogg Vorbis
- **WMA** - Windows Media Audio

#### 🎥 Video
- **MP4** - MPEG-4 Video
- **MKV** - Matroska Video
- **AVI** - Audio Video Interleave
- **MOV** - QuickTime Movie
- **WebM** - Web Media Format
- **FLV** - Flash Video
- **WMV** - Windows Media Video
- **M4V** - iTunes Video

### Calidades recomendadas

#### 🎵 Audio (Bitrate)
- **128k** - Calidad básica (archivos pequeños)
- **192k** - Calidad estándar (predeterminado)
- **256k** - Calidad alta
- **320k** - Calidad muy alta (MP3 máxima)

#### 🎥 Video (Resolución)
- **480p** - Calidad básica (SD)
- **720p** - Calidad HD (predeterminado)
- **1080p** - Calidad Full HD
- **1440p** - Calidad 2K
- **2160p** - Calidad 4K Ultra HD

## 📁 Ejemplos de conversión

```bash
# Convertir toda una carpeta (requiere script adicional)
for file in *.wav; do
    python run.py -i "$file" -f mp3 -q 320k
done

# Convertir con nombre automático
python run.py -i cancion.flac -f mp3  # Resultado: cancion.mp3

# Especificar archivo de salida
python run.py -i entrada.wav -o salida_custom.mp3
```

## 🔍 Verificación

El script verificará automáticamente:
- ✅ Si FFmpeg está instalado
- ✅ Si el archivo de entrada existe
- ✅ Si la conversión fue exitosa
- 📊 Tamaño del archivo resultante

## 🐛 Solución de problemas

### FFmpeg no encontrado
```
❌ Error: FFmpeg no está instalado o no está en el PATH.
```
**Solución:** Instala FFmpeg usando los comandos de instalación arriba.

### Archivo no encontrado
```
❌ Error: El archivo 'archivo.wav' no existe.
```
**Solución:** Verifica la ruta del archivo de entrada.

### Error de conversión
Si hay errores específicos de FFmpeg, el script mostrará el mensaje de error detallado.

## 🎯 Características

- ✨ Interfaz CLI intuitiva y fácil de usar
- 🎵 Conversión completa entre formatos de audio (7 formatos)
- 🎥 Conversión completa entre formatos de video (8 formatos)
- 🔍 Detección automática del tipo de media (audio/video)
- ⚙️ Control de calidad/bitrate para audio y resolución para video
- 📊 Información del archivo resultante con tamaño
- ❌ Manejo de errores robusto y verificación automática
- 🔧 Basado en FFmpeg para máxima compatibilidad y calidad
- 🚀 Perfecto para creadores de contenido, desarrolladores y podcasters

## 🗺️ Roadmap

### ✅ Versión 1.0 (Actual)
- [x] Conversión de formatos de audio
- [x] Conversión de formatos de video
- [x] Control de calidad/bitrate para audio
- [x] Control de resolución para video
- [x] Detección automática de tipo de media
- [x] Interfaz CLI completa
- [x] Manejo de errores robusto

### 🚧 Versión 2.0 (En desarrollo)
- [ ] Conversión por lotes (batch processing)
- [ ] Presets predefinidos para casos comunes
- [ ] Interfaz web opcional
- [ ] Compresión inteligente automática

### 🔮 Futuras versiones
- [ ] Soporte para subtítulos
- [ ] Compresión inteligente
- [ ] Integración con servicios en la nube
- [ ] Plugin para editores de video populares

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
