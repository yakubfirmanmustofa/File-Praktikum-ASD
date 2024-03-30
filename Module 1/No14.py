def formatRupiah(nominal):
    nominal_str = str(nominal)
    length = len(nominal_str)
    formatted_nominal = ''
    
    for i in range(length):
        if i % 3 == 0 and i != 0:
            formatted_nominal = '.' + formatted_nominal
            
        formatted_nominal = nominal_str[length - 1 - i] + formatted_nominal
    
    return 'Rp ' + formatted_nominal