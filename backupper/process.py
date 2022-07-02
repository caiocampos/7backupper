"""
Módulo para processar os dados e gerar o arquivo final
"""

from .configuration import load as config_load
from .file import create_archive


def process(conf_file_path: str):
    """
    Função para processar os dados e gerar o arquivo final
    """
    conf = config_load(conf_file_path)

    for file_conf in conf.files:
        print(f"Processando {file_conf.input_folder}")
        text = create_archive(
            file_conf.input_folder, file_conf.output_folder, file_conf.output_file)
        if text:
            print(f"Arquivo {text} gravado com sucesso!")
