def transfer_money(src, dst, amount):
    db.execute(f'UPDATE accounts SET balance = balance - {amount} WHERE id = {src}')
    db.execute(f'UPDATE accounts SET balance = balance + {amount} WHERE id = {dst}')
