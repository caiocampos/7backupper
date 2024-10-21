"""
Utilitário para criar arquivos de backups através de um arquivo de configuração
"""

from .process import process

CONF_FILE = "7b.conf.json"


def main() -> int:
    process(CONF_FILE)
    return 0
