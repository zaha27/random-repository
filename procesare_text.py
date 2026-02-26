def menu():

    print("1 - spatii duble")
    print("2 - pentru a scoate toate numerele")
    selected_mode = input()
    return int(selected_mode)

def main() :

    try:

        with open("text_de_procesat.txt", "r") as f: #deschidem fisierul prin f
            print("\t textul neprelucrat:")
            raw_text = f.read()
            print(raw_text) #afisam continutul fisierului 
            
            

            vector_caractere = list(raw_text) #bagam intr un vector fiecare caracter \
                                            #in parte pentru a il procesa ulterior
            #print(vector_caractere) #nu mai e nevoie de verificarea vectorului asa ca comentam

            
            #pas 1 oricum scoatem semnele de punctuatie deci:
            caractere_ilegale = [",", ".", "!", ";", "?", "-"]
            
            #in text_after_first_clean vom avea fiecare caracter in vector_caractere care nu apare in caractere_ilegale
            arr = [c for c in vector_caractere if c not in caractere_ilegale]


            #afisam textul curatat
            print("\t dupa primul pas de procesare - scoatem semnele de punctuatie")        
            list_text_after_first_clean = "".join(arr)
            print(list_text_after_first_clean)
            
            #pasul 2: curatare cu meniu
            selected_mode = menu()  #meniu din care alegi care din operatii doresti sa efectuezi
            if selected_mode == 1 :
                
                #spatii duble 
                c = 0
                while c < len(arr) - 1:
                    if arr[c] == ' ' and arr[c + 1] == ' ' :
                        del arr[c + 1]
                    c = c + 1


            elif selected_mode == 2 :

                #cifre 
                c = 0
                while c < len(arr):
                    if arr[c].isdigit() :
                        del arr[c]
                    else :
                        c = c + 1
            
            #afisam textul curatat
            text_curatat = "".join(arr)
            print("\t text dupa curatare: ")
            print(text_curatat)


    except FileNotFoundError:
        print("Eroare: Fisierul text_de_procesat.txt nu a fost gasit!")
        return

    
if __name__ == "__main__":
    main()  

