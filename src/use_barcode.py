import barcode_detect 

a = barcode_detect.get_barcode()

print(a)
print(type(a))
print(a.decode('utf-8'))
