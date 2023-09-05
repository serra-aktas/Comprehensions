# MÜLAKAT SORUSU

# Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Key'ler orijinal değerler, value'ler ise değiştirilmiş değerler olacak.

#klasik bir yöntemle

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
        
        print(new_dict)
        

#daha şık bir yöntemle
        
numbers = range(10) 
new_dict = {}
        
{n: n ** 2 for n in numbers if n % 2 == 0}
