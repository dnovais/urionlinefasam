value = int(input())

bill_100 = int(value) / int(100)
bill_50 = int(value) % int(100) / 50
bill_20 = ((int(value) % int(100)) % 50) / 20
bill_10 = ((((int(value) % int(100)) % 50)) % 20) / 10
bill_5 = (((((int(value) % int(100)) % 50)) % 20) % 10) / 5
bill_2 = (((((((int(value) % int(100)) % 50)) % 20) % 10)) % 5) / 2
bill_1 = (((((((int(value) % int(100)) % 50)) % 20) % 10)) % 5) % 2

print(int(value))
print("{:d} nota(s) de R$ 100,00".format(int(bill_100)))
print("{:d} nota(s) de R$ 50,00".format(int(bill_50)))
print("{:d} nota(s) de R$ 20,00".format(int(bill_20)))
print("{:d} nota(s) de R$ 10,00".format(int(bill_10)))
print("{:d} nota(s) de R$ 5,00".format(int(bill_5)))
print("{:d} nota(s) de R$ 2,00".format(int(bill_2)))
print("{:d} nota(s) de R$ 1,00".format(int(bill_1)))
