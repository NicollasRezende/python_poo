class Minha_str(str):
    def upper(self):
        print('UPPER')#e possivel executar coisas antes do super
        return super().upper()
    

string  = Minha_str('Ola')
print(string.upper())