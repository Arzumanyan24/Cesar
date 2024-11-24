alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def cesar():
    tarer=""
    shift=int(input("asa shift"))
    bar=input('enter secret message ')
    for element in bar:
        tar_index = alphabet.index(element)
        tar_index +  shift
        tar = alphabet[tar_index]
        tarer += tar
    print(tarer)
            
cesar()
