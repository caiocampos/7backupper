"""
Módulo para processamento do arquivo de configuração
"""

from dataclasses import dataclass
import json


@dataclass
class FileConf:
    """
    Classe que representa a configuração do arquivo que será gerado
    """

    def __init__(self, input_folder: str, output_folder: str, output_file: str):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.output_file = output_file

    @staticmethod
    def default():
        """
        Método para criar a instancia padrão de FileConf
        """
        return FileConf("", "", "")


@dataclass
class Conf:
    """
    Classe que representa os dados de configuração
    """

    def __init__(self, files: list[FileConf]):
        self.files = files

    @staticmethod
    def default():
        """
        Método para criar a instancia padrão de Conf
        """
        return Conf([])


def parse(config_json: dict) -> Conf:
    """
    Função para processar os dados recebidos no JSON
    """
    if not config_json:
        return Conf.default()

    files = []

    for file in config_json.get("files") or []:
        files.append(
            FileConf(
                file.get("input_folder") or "",
                file.get("output_folder") or "",
                file.get("output_file") or "",
            )
        )

    return Conf(files)


def load(conf_file_path: str) -> Conf:
    """
    Função para carregar os dados armazenados no JSON de configuração
    """
    try:
        with open(conf_file_path, "r", encoding="utf-8") as conf_file:
            config_json: dict = json.load(conf_file)

            return parse(config_json)
    except (OSError, EOFError) as ex:
        print(f"Could not read the file {conf_file_path} \nError: {ex}")
        return Conf.default()
