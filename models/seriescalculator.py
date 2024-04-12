from utils import datahandler
import pandas as pd

def get_dialog_count_per_character():
    target_file = datahandler.get_target_file()
    character_column = datahandler.get_character_column_name()
    
    df = pd.DataFrame(target_file)
    dialog_count_per_character = df[character_column].value_counts()
    dialog_count_per_character.name = 'Dialog Count'
    dialog_count_per_character.index.name = None
        
    return dialog_count_per_character

def get_chars_count_per_character():
    target_file = datahandler.get_target_file()
    character_column = datahandler.get_character_column_name()
    dialog_column = datahandler.get_dialog_column_name()
    
    df = pd.DataFrame(target_file)
    grouped = df.groupby(character_column)
    chars_count_per_character = grouped[dialog_column].apply(lambda dialog: dialog.str.len().sum())
    chars_count_per_character.name = 'Chars Count'
    chars_count_per_character.index.name = None
    
    return chars_count_per_character

def get_term_count_per_character():
    target_file = datahandler.get_target_file()
    character_column = datahandler.get_character_column_name()
    dialog_column = datahandler.get_dialog_column_name()
    search_term = datahandler.get_search_term()
    
    df = pd.DataFrame(target_file)
    grouped = df.groupby(character_column)
    
    if search_term:
        term_count_per_character = grouped[dialog_column].apply(lambda dialog: dialog.str.count(search_term).sum())
        
    else:
        term_count_per_character = pd.Series(0, index=grouped.indices.keys())
        
    term_count_per_character.name = 'Term Count'
    term_count_per_character.index.name = None
        
    return term_count_per_character