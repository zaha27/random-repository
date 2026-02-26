def menu():

    print("1 - spatii duble")
    print("2 - pentru a scoate toate numerele")
    selected_mode = input()
    return selected_mode

def main() :

    with open("text_de_procesat.txt", "r") as f: #deschidem fisierul prin f
        print("\t textul neprelucrat:")
        raw_text = f.read()
        print(raw_text) #afisam continutul fisierului 
        
        

        vector_caractere = list(raw_text) #bagam intr un vector fiecare caracter \
                                          #in parte pentru a il procesa ulterior
        print(vector_caractere)

        
        #pas 1 oricum scoatem semnele de punctuatie deci:
        caractere_ilegale = [",", ".", "!", ";", "?", "-"]
        
        #in text_after_first_clean vom avea fiecare caracter in vector_caractere care nu apare in caractere_ilegale
        text_after_first_clean = [c for c in vector_caractere if c not in caractere_ilegale]


        print("\t dupa primul pas de procesare - scoatem semnele de punctuatie")
        print(text_after_first_clean)


if __name__ == "__main__":
    main()  

