from account import Account

account_list = ['f033025', 'f01191221', 'f01340400', 'f01310053', 'f01784916']

acc0 = Account(account_list[0])
acc1 = Account(account_list[1])
acc2 = Account(account_list[2])
acc3 = Account(account_list[3])
acc4 = Account(account_list[4])

accounts: [Account] = [acc0, acc1, acc2, acc3, acc4]

for acc in accounts:
    print(acc.status)