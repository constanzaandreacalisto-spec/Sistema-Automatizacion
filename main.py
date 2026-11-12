# config.py
import os
from pathlib import Path
from dotenv import load_dotenv

if Path(".env").exists():
    load_dotenv(dotenv_path=Path(".env"))

def obtener_config():
    return {
        "SMTP_HOST": os.getenv("SMTP_HOST", "smtp.gmail.com"),
        "SMTP_PORT": os.getenv("SMTP_PORT", "587"),
        "SMTP_USER": os.getenv("SMTP_USER", ""),
        "SMTP_PASSWORD": os.getenv("SMTP_PASSWORD", ""),
        "SMTP_USE_TLS": os.getenv("SMTP_USE_TLS", "true"),
        "MAIL_FROM_NAME": os.getenv("MAIL_FROM_NAME", "Recursos Humanos"),
        "MAIL_FROM_ADDRESS": os.getenv("MAIL_FROM_ADDRESS", ""),
        "MAIL_REPLY_TO": os.getenv("MAIL_REPLY_TO", ""),
        "MAIL_DELAY_SECONDS": os.getenv("MAIL_DELAY_SECONDS", "2"),
        "MAIL_MAX_RETRIES": os.getenv("MAIL_MAX_RETRIES", "3"),
        "EMPRESA_NOMBRE": os.getenv("EMPRESA_NOMBRE", "Mi Empresa SpA"),
        "EMPRESA_RUT": os.getenv("EMPRESA_RUT", "76.123.456-7"),
        "PDF_PASSWORD_MODE": os.getenv("PDF_PASSWORD_MODE", "none")
    }