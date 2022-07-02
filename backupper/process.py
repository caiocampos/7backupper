"""
Módulo para processar os dados e gerar o arquivo final
"""

from . import configuration
from . import file


def process(conf_file_path: str):
    """
    Função para processar os dados e gerar o arquivo final
    """
    conf = configuration.load(conf_file_path)

    for file_conf in conf.files:
        print(f"Processando {file_conf.input_folder}")
        text = file.create_archive(
            file_conf.input_folder, file_conf.output_folder, file_conf.output_file)
        if text:
            print(f"Arquivo {text} gravado com sucesso!")
