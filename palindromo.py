def palindromo(palabra):
    pal=palabra.replace(' ','')
    pal=pal.lower()
    pal_inv=pal[::-1]
    if(pal == pal_inv):
        return True;
    else:
        return False;

def run():
    palabra=input('escriba palabra ::')
    es_pal =palindromo(palabra)
    if (es_pal):
        print('es palindromo')
    else:
        print('NO es palindromo')


if __name__ == '__main__':
    run()