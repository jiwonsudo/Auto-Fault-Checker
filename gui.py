import tkinter as tk
from datetime import datetime
import threading

from account import Account

class GUI(Account):
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('Filecoin Status Auto Checker (FSAC) by Jiwon')
        self.root.geometry('600x400+100+100')
        self.root.resizable(False, False)
        
        self.num_of_account = 0
        self.time_str = tk.StringVar(self.root)
    
    def load(self):
        self.time_str.set('|----------Welcome----------|')
        
        lbl = tk.Label(self.root, textvariable=self.time_str, width=40, height=1, bg='blue', fg='yellow', anchor='w')
        lbl.place(x=0, y=0)
        
        
    def set_interval(self, func, sec):
        def func_wrapper():
            self.set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t
    
    def add_account(self, account: Account):
        globals()[f'self.account_{self.num_of_account}']: Account = account  # account_{id}
        
        globals()[f'self.account_{self.num_of_account}_strVar'] = tk.StringVar(self.root)
        globals()[f'self.account_{self.num_of_account}_strVar'].set(f'여기에 계정 {self.num_of_account}의 상태가 표시됩니다.')
        
        globals()[f'self.account_{self.num_of_account}_lbl'] = tk.Label(self.root, textvariable=globals()[f'self.account_{self.num_of_account}_strVar'], width=100, height=1, bg='white', fg='black', anchor='w')
        globals()[f'self.account_{self.num_of_account}_lbl'].place(x=0, y=(self.num_of_account*23 + 23))
        
        self.num_of_account += 1
        
    def update_account_strVar(self, account_id: int):
        globals()[f'self.account_{account_id}'].update_status()
        globals()[f'self.account_{account_id}_strVar'].set(f'Account {account_id} ({globals()[f'self.account_{account_id}'].id}):TOTL {globals()[f'self.account_{account_id}'].status['total']}, ACTV {globals()[f'self.account_{account_id}'].status['active']}, FALT {globals()[f'self.account_{account_id}'].status['fault']}, RECV {globals()[f'self.account_{account_id}'].status['recovery']} - LAST {globals()[f'self.account_{account_id}'].last_check_time}')
    
    def start(self):
        timer = 180  #3 minutes (=180 sec)
        
        def clock():
            now = datetime.now()
            self.time_str.set(f'CURRTIME: {now.strftime('%Y-%m-%d %H:%M:%S')}')
            nonlocal timer
            timer -= 1
            if timer <= 0:
                for id in range(0, self.num_of_account):
                    self.update_account_strVar(id)

                    
        for id in range(0, self.num_of_account):
            self.update_account_strVar(id)
                    
        self.set_interval(clock, 1)
        
        self.load()
        
        self.root.mainloop()