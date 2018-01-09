country_number = {'Korea':82, 'China':86, 'Japan':81, 'USA':1}


def return_key_value(dictionary):
    country_input = 82
    while country_input != 82 or 86 or 81 or 1:
        country_input = int(input('The country you want to find national number:'))
        for k, v in dictionary.items():
            if v == country_input:
                print(k)
        if country_input == '0':
            break



return_key_value(country_number)

# key = list(country_number.keys())
# values = list(country_number.values())
#
# country_input = int(input('The country you want to find national number:'))
# for i in range(len(values)):
#     if values[i] == country_input:
#         print(key[i])