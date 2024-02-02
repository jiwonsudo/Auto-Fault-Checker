from account import Account
from status_gui import StatusGUI

def start_main(account_list: [str], type_of_OS: str):
    gui = StatusGUI()

    for id, account in enumerate(account_list):
        globals()[f'account_{id}'] = Account(account)
        gui.add_account(globals()[f'account_{id}'], 'windows')
    
    gui.start(type_of_OS)
    
account_name_list = ['f033025', 'f01191221', 'f01340400', 'f01310053', 'f01784916']

start_main(account_name_list, 'windows')