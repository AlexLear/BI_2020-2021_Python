print('Converter for PRESSURE measure units')
print('Available measure units are Pa, at, bar, mmHg')


value = float(input('Enter the value of pressure '))
unit = input('Enter the unit of this value ')


# Calculations and output
if unit == 'Pa':
    print('Other units: ' + str(value / 101325) + ' at' + '\t' + str(value / 100000) +
          ' bar' + '\t' + str(value / 133.32) + ' mmHg')
elif unit == 'at':
    print('Other units: ' + str(value * 101325) + ' Pa' + '\t' + str(value * 1.01325)
          + ' bar' + '\t' + str(value * 760) + ' mmHg')
elif unit == 'bar':
    print('Other units: ' + str(value * 0.987) + ' at' + '\t' + str(value * 100000)
          + ' Pa' + '\t' + str(value * 750.06) + ' mmHg')
elif unit == 'mmHg':
    print('Other units: ' + str(value / 760) + ' at' + '\t' + str(value * 0.001333) + ' bar'
          + '\t' + str(value * 133.32) + ' Pa')
else:
    print('Wrong input. Please, choose a correct measure unit.')
