# Змінна з сумою рахунку
bill_amount = float(input())

# Обчислення чайових (10%)
tip = bill_amount * 0.10

# Загальна сума до сплати
total_amount = bill_amount + tip

print(f"Сума чайових: {tip:.2f} грн")
print(f"Загальна сума до сплати: {total_amount:.2f} грн")
