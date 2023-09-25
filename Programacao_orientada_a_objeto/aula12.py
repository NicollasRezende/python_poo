# class Caneta:
#     #private
#     def __init__(self, cor): 
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# caneta = Caneta('azul')

# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
#comumente usado em outras linguagens^^^^


class Caneta:
    #private
    def __init__(self, cor): 
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    

caneta = Caneta('azul')


print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)

#python e foda...^^^^^^