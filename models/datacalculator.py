from utils import datahandler
import pandas as pd

def get_search_term_count():
    target_file = datahandler.get_target_file()
    dialog_column = datahandler.get_dialog_column_name()
    search_term = datahandler.get_search_term()
    
    df = pd.DataFrame(target_file)
    search_term_count = df[dialog_column].str.count(search_term).sum()
    
    return search_term_count

def get_total_chars_in_dialog():
    target_file = datahandler.get_target_file()
    dialog_column = datahandler.get_dialog_column_name()
    
    df = pd.DataFrame(target_file)
    total_chars_in_dialog = df[dialog_column].str.len().sum()
    
    return total_chars_in_dialog
