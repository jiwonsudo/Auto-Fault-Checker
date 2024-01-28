from account import Account
from gui import GUI

account_name_list = ['f033025', 'f01191221', 'f01340400', 'f01310053', 'f01784916']

id = 0

program = GUI()

for account in account_name_list:
    globals()[f'account_{id}'] = Account(account)
    program.add_account(globals()[f'account_{id}'])
    id += 1
    
print(f'총 {id}개의 계정이 추가되었습니다.')

program.start()