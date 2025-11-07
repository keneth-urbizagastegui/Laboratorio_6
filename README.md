# Laboratorio_6

Proyecto de práctica dividido en dos partes:

- pregunta_1: Pequeña aplicación Flask que consulta Pokémon y renderiza resultados en una plantilla Jinja2 (`templates/index.html`).
- pregunta_2: Descargador universal de videos y audio basado en `yt-dlp`, con menú interactivo y soporte para FFmpeg.

## Requisitos

- Python 3.10 o superior.
- pip actualizado.
- Paquetes:
  - Flask (para pregunta_1)
  - yt-dlp (para pregunta_2)
- FFmpeg (recomendado y necesario para unir video+audio y convertir a MP3 en pregunta_2).

## Instalación de dependencias

```bash
pip install Flask yt-dlp
```

### FFmpeg (Windows)

1. Descarga un build completo de FFmpeg (incluye carpeta `bin`).
2. Descomprime y ubica la ruta de la carpeta `bin`, por ejemplo:
   `C:\ffmpeg\bin` o `C:\Users\<usuario>\Downloads\ffmpeg-<version>\ffmpeg-<version>\bin`
3. Agrega la ruta al PATH del usuario y verifica:
   - ffmpeg -version

Con FFmpeg disponible, el script de `pregunta_2` habilitará la unión de `bestvideo+bestaudio` a MP4 y la generación de MP3.

### Instalación por sistema operativo

- Windows:
  1. Descarga un build completo de FFmpeg (full build) que incluya la carpeta `bin`.
  2. Descomprime y agrega la ruta `...\ffmpeg\bin` al PATH del usuario.
  3. Verifica con `ffmpeg -version`.

- macOS:
  - Con Homebrew:
    ```bash
    brew install ffmpeg
    ```
    Verifica con `ffmpeg -version`.

- Linux (Debian/Ubuntu):
  ```bash
  sudo apt update
  sudo apt install -y ffmpeg
  ffmpeg -version
  ```

## Estructura del proyecto

```
Laboratorio_6/
├── pregunta_1/
│   ├── app.py
│   └── templates/
│       └── index.html
└── pregunta_2/
    └── downloader.py
```

Carpetas de salida creadas por `pregunta_2` (ignoradas en Git):
- `Descargas_Videos/`
- `Descargas_Audio/`

## Uso

### pregunta_1 (Flask)

1. Ejecuta el servidor:
   ```bash
   python pregunta_1/app.py
   ```
2. Abre en el navegador: `http://127.0.0.1:5000/`
3. Ingresa el nombre del Pokémon y consulta; se mostrarán nombre, tipos, movimientos e imágenes (según disponibilidad).

### pregunta_2 (Descargador universal)

Ejecuta:
```bash
python pregunta_2/downloader.py
```

Menú (dinámico según disponibilidad de FFmpeg):
- Mejor calidad MP4 (requiere FFmpeg): descarga y une `bestvideo+bestaudio` en `Descargas_Videos/`.
- Audio MP3 de alta calidad (requiere FFmpeg): extrae audio a `Descargas_Audio/`.
- Video simple: descarga un archivo de video sin unir flujos (útil si no hay FFmpeg).

Notas:
- Soporta URLs de múltiples sitios (YouTube, Instagram, TikTok, etc.) gracias a `yt-dlp`.
- Algunos enlaces pueden requerir autenticación o tener restricciones regionales.
- Si el sitio cambia, actualiza `yt-dlp` periódicamente: `pip install -U yt-dlp`.

### Ejemplos

- Descargar video MP4 (con FFmpeg disponible):
  1) Ejecuta el script y elige “Mejor calidad MP4”.
  2) Pega la URL del video (YouTube/Instagram/TikTok).
  3) El archivo se guardará en `Descargas_Videos/`.

- Descargar audio MP3:
  1) Ejecuta el script y elige “Audio MP3 de alta calidad”.
  2) Pega la URL.
  3) El archivo se guardará en `Descargas_Audio/`.

- Video simple (sin ffmpeg):
  1) Ejecuta el script y elige “Video simple”.
  2) Pega la URL.

### Actualizar yt-dlp

```bash
pip install -U yt-dlp
```

### Solución de problemas

- “FFmpeg no detectado en el PATH”:
  - Asegúrate de que `ffmpeg` sea ejecutable en la terminal (Windows: agregar `...\ffmpeg\bin` al PATH; macOS/Linux: instalar vía brew/apt).
  - Cierra y reabre la terminal tras modificar el PATH.

- “Error al unir bestvideo+bestaudio” o al convertir MP3:
  - Verifica que FFmpeg esté accesible y actualizado.
  - Prueba la opción “Video simple” si necesitas descargar sin unión.

- “URL no soportada” o “Se requiere autenticación”:
  - Algunos sitios restringen el acceso; prueba otra URL o inicia sesión con las opciones de yt-dlp (avanzado).

## Contribución

Los PRs y mejoras son bienvenidos. Ideas útiles:
- Opción de descarga sólo audio (m4a) sin conversión.
- Selección de resoluciones específicas.
- Descarga de subtítulos.
- Integración de opciones avanzadas de `yt-dlp` (auth, cookies, subtítulos, selección de formato).

## Licencia

Uso académico/educativo.