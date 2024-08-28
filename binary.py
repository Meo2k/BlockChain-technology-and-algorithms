
a = int(input('Input : '))

is_mod = True
swap_binary = ''
binary = ''
while (is_mod):
    temp = str(a % 2)
    swap_binary += temp
    a = a // 2
    if (a == 0):
        is_mod = False

for char in range(len(swap_binary) - 1, -1, -1):
    binary += swap_binary[char]

binary = int(binary)
print("binary: ", binary)
