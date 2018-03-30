age = int(input())

years = int(age) / int(365)
months = (int(age) - (int(years)*int(365))) / int(30)
days = (int(age) - (int(years)*int(365))) % int(30)

print("{:d} ano(s)".format(int(years)))
print("{:d} mes(es)".format(int(months)))
print("{:d} dia(s)".format(int(days)))
