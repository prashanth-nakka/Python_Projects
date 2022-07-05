import phonenumbers
# print(dir(phonenumbers))

from phonenumbers import timezone, geocoder, carrier

pn = input("Enter Your Number with +____: ")
# print(pn)
phn = phonenumbers.parse(pn)
print(phn)  # Country Code: 91 National Number: 98*******
time = timezone.time_zones_for_number(phn)
print(time)  # ('Asia/Calcutta',)
car = carrier.name_for_number(phn, "en")
print(car)  # Airtel
reg = geocoder.description_for_number(phn, "en")
print(reg)  # India
