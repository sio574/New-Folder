
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_usuarios.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Si hay algún error con la importación de Django
        raise ImportError(
            "No se pudo importar Django. Asegúrate de que está instalado en tu entorno virtual."
        )
    execute_from_command_line(sys.argv)
