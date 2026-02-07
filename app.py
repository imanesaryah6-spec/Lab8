import utils

def main():
    notes = [14, 16, 10, 18]
    resultat = utils.moyenne(notes)
    
    print(f"Version: {utils.VERSION}")
    print(f"Moyenne: {resultat}")

if __name__ == "__main__":
    main()
