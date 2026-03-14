#!usr/bin/env python3
"""
system_info.py - información del sistema actual.
"""

import sys
import os
import platform
from datetime import datetime

def get_system_info() -> dict:
    """Recopila información del sistema."""
    return{
	"Python": sys.version.split()[0],
	"OS": f"{platform.system()} {platform.release()}",
	"Usuario": os.getlogin(),
	"Directorio": os.getcwd(),
	"Fecha/hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
	}

def print_info(info:dict) -> None:
    """Imprime la información formateada"""
    print("="*50)
    print("INFORMACIÓN DEL SISTEMA")
    print("="*40)
    for clave, valor in info.items():
        print(f"{clave:<12}:{valor}")
    print("="*40)

if __name__ == "__main__":
    print_info(get_system_info())


