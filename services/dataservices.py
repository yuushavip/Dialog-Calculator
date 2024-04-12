from models import datacalculator, seriescalculator
import pandas as pd

def get_total_data_counts():
    search_term_count = datacalculator.get_search_term_count()
    total_chars_in_dialog = datacalculator.get_total_chars_in_dialog()
    
    data = {
        'Total': {
            'Chars in dialog': total_chars_in_dialog,
            'Search Term Count': search_term_count
        }
    }
    
    df = pd.DataFrame(data)
    
    return df

def get_data_counts_per_character():
    dialog_count_per_character = seriescalculator.get_dialog_count_per_character()
    chars_count_per_character = seriescalculator.get_chars_count_per_character()
    term_count_per_character = seriescalculator.get_term_count_per_character()
    
    result = pd.concat([dialog_count_per_character, chars_count_per_character, term_count_per_character], axis=1)
    result.Name = 'Data Counts Per Character'
    
    return result