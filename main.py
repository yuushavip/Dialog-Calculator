from services import dataservices

def main():
    results = [
        dataservices.get_data_counts_per_character(),
        dataservices.get_total_data_counts()
    ]
    
    for result in results:
        print(result, "\n")
    
if __name__ == "__main__":
    main()