import yt_dlp
import os
import shutil  # <-- ¡NUEVA IMPORTACIÓN! Para buscar ejecutables

# =====================================================
# --- DETECCIÓN AUTOMÁTICA DE FFMPEG ---
# =====================================================
# shutil.which() busca 'ffmpeg' en el PATH del sistema.
# Devuelve la ruta si lo encuentra, o None si no.
# bool() convierte la ruta (True) o None (False) en un booleano.
FFMPEG_DISPONIBLE = bool(shutil.which('ffmpeg'))
# =====================================================

def descargar_video_universal(url, ydl_opts, output_path='Descargas_Videos'):
    """
    Toma CUALQUIER URL (YT, IG, TikTok) y la descarga usando
    las opciones (ydl_opts) proporcionadas.
    (Esta función no cambia, ya es perfectamente flexible).
    """
    print(f"\n--- Iniciando descarga ---")
    
    # Asegurarnos de que el output_path esté en las opciones
    ydl_opts['outtmpl'] = os.path.join(output_path, '%(title)s.%(ext)s')

    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Carpeta '{output_path}' creada.")
    
    try:
        # Ejecutar la descarga con las opciones dadas
        print(f"Obteniendo información de: {url}...")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url]) # Le pasamos la URL como una lista
            
        print(f"¡Éxito! Contenido descargado en '{output_path}'")

    except yt_dlp.utils.DownloadError as de:
        print(f"\nError de yt-dlp: {de}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

# =====================================================
# --- Bucle principal (CON MENÚ DINÁMICO) ---
# =====================================================
if __name__ == "__main__":
    print("--- Asistente de Descarga Universal (YouTube, Instagram, TikTok) ---")
    
    # 1. Informar al usuario sobre el estado de FFMPEG
    if FFMPEG_DISPONIBLE:
        print("\n[Estado: FFMPEG detectado. Todas las opciones avanzadas habilitadas.]")
    else:
        print("\n[ADVERTENCIA: FFMPEG no fue detectado en el PATH del sistema.]")
        print("[-> La unión de video+audio (MP4) y la conversión a MP3 están deshabilitadas.]")
        print("[-> Para habilitarlas, instala FFMPEG y agrégalo al PATH.]")
    
    # 2. Pedir la URL
    video_url = input("\nPor favor, ingresa la URL del video: ")
    
    if not video_url:
        print("No se ingresó ninguna URL. Saliendo.")
    else:
        # 3. Mostrar el menú DINÁMICO
        print("\n¿Qué quieres descargar?")
        
        # Opciones base
        common_opts = {'noplaylist': True, 'quiet': False}
        final_opts = None
        output_folder = 'Descargas_Videos' # Default
        
        # Mostramos las opciones según si FFMPEG existe
        if FFMPEG_DISPONIBLE:
            # Menú completo
            print(" [1] Mejor Video (MP4 - Une Video+Audio, requiere FFMPEG)")
            print(" [2] Solo Audio (MP3 - Conversión, requiere FFMPEG)")
            print(" [3] Video Simple (Calidad 'Best', formato original, sin FFMPEG)")
            
            choice = input("Elige una opción (1, 2 o 3): ")
            
            if choice == '1':
                print("Opción 1: Mejor Video (MP4)")
                video_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'merge_output_format': 'mp4',
                }
                final_opts = {**common_opts, **video_opts}

            elif choice == '2':
                print("Opción 2: Solo Audio (MP3)")
                audio_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                final_opts = {**common_opts, **audio_opts}
                output_folder = 'Descargas_Audio' # Cambiamos carpeta

            elif choice == '3':
                print("Opción 3: Video Simple (Calidad 'Best')")
                video_opts = {'format': 'best'}
                final_opts = {**common_opts, **video_opts}
            
            else:
                print("Opción inválida. Saliendo.")

        else:
            # Menú limitado (SIN FFMPEG)
            print(" [1] Video Simple (Calidad 'Best', formato original)")
            choice = input("Elige una opción (solo 1 disponible): ")
            
            if choice == '1':
                print("Opción 1: Video Simple (Calidad 'Best')")
                video_opts = {'format': 'best'}
                final_opts = {**common_opts, **video_opts}
            else:
                print("Opción inválida. Saliendo.")

        # 4. Ejecutar la descarga (solo si se eligió una opción válida)
        if final_opts:
            descargar_video_universal(video_url, final_opts, output_path=output_folder)