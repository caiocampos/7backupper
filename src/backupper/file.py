"""
Módulo para processamento dos arquivos de entrada e saída
"""

import os
import py7zr
from py7zr.exceptions import ArchiveError


def parse_folder(folder: str) -> str:
    """
    Função para corrigir possíveis problemas com formato de nome de pasta
    """
    if folder.endswith(os.path.sep):
        return folder

    return folder + os.path.sep


def create_archive(input_folder: str, output_folder: str, output_file: str) -> str:
    """
    Função para gravar o arquivo de saída com o texto desejado
    """
    if not os.path.isdir(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError as ex:
            print(f"Could not create the folder {output_folder} \nError: {ex}")
            return ""

    full_path = parse_folder(output_folder) + output_file

    try:
        with py7zr.SevenZipFile(full_path, "w") as archive:
            archive.writeall(input_folder, "base")

            return full_path

    except (OSError, ArchiveError) as ex:
        print(f"Could not write the file {full_path} \nError: {ex}")
        return ""
