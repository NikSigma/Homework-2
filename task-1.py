from datetime import datetime


current_year = datetime.now().year


birth_year = int(input("Введіть ваш рік народження: "))


age_now = current_year - birth_year
print(f"Ваш вік у {current_year} році: {age_now} років.")


age_in_2035 = 2035 - birth_year
print(f"У 2035 році вам буде: {age_in_2035} років.")


age_2000_in_2035 = 2035 - 2000
difference = age_in_2035 - age_2000_in_2035
print(f"У 2035 році ви будете старші за людину, яка народилася у 2000, на {difference} років.")


year = 2061
birth_year_taras = 1861
age_taras = year - birth_year_taras


age_maxym = age_taras * 5
birth_year_maxym = year - age_maxym


age_petro = age_taras // 4
birth_year_petro = year - age_petro

print(f"\nУ {year} році:")
print(f"Тарасу: {age_taras} років (народився у {birth_year_taras})")
print(f"Максиму: {age_maxym} років (народився у {birth_year_maxym})")
print(f"Петру: {age_petro} років (народився у {birth_year_petro})")
