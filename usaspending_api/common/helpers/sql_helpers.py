import os
import logging

from usaspending_api.common.exceptions import InvalidParameterException


logger = logging.getLogger('console')


def read_sql_file(file_path):
    # Read in SQL file and extract commands into a list
    _, file_extension = os.path.splitext(file_path)

    if file_extension != '.sql':
        raise InvalidParameterException("Invalid file provided. A file with extension '.sql' is required.")

    # Open and read the file as a single buffer
    fd = open(file_path, 'r')
    sql_file = fd.read()
    fd.close()

    # all SQL commands (split on ';') and trimmed for whitespaces
    return [command.strip() for command in sql_file.split(';') if command]
