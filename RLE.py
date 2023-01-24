# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
with open('file_encode.txt', 'w') as data:
    data.write('aaaaabbbcccc')
with open('file_encode.txt', 'r') as data:
    string = data.readline()
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
                count += 1
    else:
        encoding += str(count) + prev_char
    return encoding
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)
print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))






