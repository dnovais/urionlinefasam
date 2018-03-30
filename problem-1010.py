line_1 = str(input())
line_2 = str(input())

order_1 = line_1.split(' ', 2)
order_2 = line_2.split(' ', 2)

total = (float(order_1[1])*float(order_1[2])) + (float(order_2[1])*float(order_2[2]))

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
