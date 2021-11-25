import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('menu.csv')
beef_and_pork_calories = (df[df['Category'] == 'Beef & Pork']['Calories'].mean())
fish_and_chiken_calories = (df[df['Category'] == 'Chicken & Fish']['Calories'].mean())
print('Проверим гипотезу что Курица с Рыбой менее вреды для человека по сравнению с говядиной и свининой.\n')
print('В среднем в категории Chiken and Fish:', round(fish_and_chiken_calories, 2), 'калорий')
print('В среднем в категории Beef & Pork:', round(beef_and_pork_calories, 2), 'калорий\n')



beef_vitamin_a = (df[df['Category'] == 'Beef & Pork']['Vitamin A (% Daily Value)'].mean())
beef_vitamin_c = (df[df['Category'] == 'Beef & Pork']['Vitamin C (% Daily Value)'].mean())
fish_vitamin_a = (df[df['Category'] == 'Chicken & Fish']['Vitamin A (% Daily Value)'].mean())
fish_vitamin_c = (df[df['Category'] == 'Chicken & Fish']['Vitamin C (% Daily Value)'].mean())

print('Среднее значение витамина A в говядине или свинине:', round(beef_vitamin_a, 2))
print('Среднее значение витамина C в говядине или свинине:', round(beef_vitamin_c, 2))
print('Среднее значение витамина A в Курице или Рыбе:', round(fish_vitamin_a, 2))
print('Среднее значение витамина C в Курице или Рыбе:', round(fish_vitamin_c, 2))

beff_calc = (df[df['Category'] == 'Beef & Pork']['Calcium (% Daily Value)'].mean())
fish_calc = (df[df['Category'] == 'Chicken & Fish']['Calcium (% Daily Value)'].mean())

print('\nСреднее кол-во кальция в категории Deef & Pork:', round(beff_calc,2))
print('Среднее кол-во кальция в категории Fish & Chiken:', round(fish_calc,2))


a = (beef_vitamin_a + beef_vitamin_c + beff_calc)
print('\nКоличество всех витаминов в Говядине и Свинине:', round(a, 2))
b = (fish_vitamin_a + fish_vitamin_c + fish_calc)
print('Количество всех витаминов в Курице и Рыбе:', round(b, 2))

print('Сделаем вывод что в Рыбе и курице больше различных витаминов, но из-за панировки в ресторане она является более каллорийной\nВ случае говядины и свинины в них меньшее количество полезных элементов, но и меньше каллорий.')



d1 = df[df['Category'] == 'Beef & Pork'].groupby('Calories').mean()
d2 = df[df['Category'] == 'Chicken & Fish'].groupby('Calories').mean()

d1.drop(['Calories from Fat', 'Total Fat', 'Total Fat (% Daily Value)', 'Saturated Fat', 'Saturated Fat (% Daily Value)', 'Trans Fat', 'Cholesterol', 'Cholesterol (% Daily Value)', 'Sodium', 'Sodium (% Daily Value)', 'Carbohydrates', 'Carbohydrates (% Daily Value)', 'Dietary Fiber', 'Dietary Fiber (% Daily Value)', 'Sugars', 'Protein', 'Iron (% Daily Value)'], axis = 1, inplace = True)
d2.drop(['Calories from Fat', 'Total Fat', 'Total Fat (% Daily Value)', 'Saturated Fat', 'Saturated Fat (% Daily Value)', 'Trans Fat', 'Cholesterol', 'Cholesterol (% Daily Value)', 'Sodium', 'Sodium (% Daily Value)', 'Carbohydrates', 'Carbohydrates (% Daily Value)', 'Dietary Fiber', 'Dietary Fiber (% Daily Value)', 'Sugars', 'Protein', 'Iron (% Daily Value)'], axis = 1, inplace = True)

d1.plot(kind='barh', figsize=(8,5), title='Свинина с говядиной', subplots=True)
d2.plot(kind='barh', figsize=(8,5), title='Курица с рыбой', subplots=True)

plt.show()



                                        
                                           
                                            
