from utils import confighandler
import pandas as pd

def get_target_file():
    config = confighandler.get_config('FILE')
    file_name = config['target_file']
    sheet_name = config['target_sheet']
    file_path = f"data/{file_name}"
    
    file = pd.read_excel(file_path, sheet_name=sheet_name)
    
    return file

def get_character_column_name():
    config = confighandler.get_config('SETTINGS')
    column_name = config['character_column']
    
    return column_name

def get_dialog_column_name():
    config = confighandler.get_config('SETTINGS')
    column_name = config['dialog_column']
    
    return column_name

def get_search_term():
    config = confighandler.get_config('SEARCH')
    search_term = config['search_term']
    
    return search_term