import configparser

def get_config(session=None):
    file_name = 'config.ini'
    file_path = f"config/{file_name}"
    config = configparser.ConfigParser()
    config.read_file(open(file_path, 'r', encoding='utf-8'))
    
    if session:
        return config[session]
    
    return config