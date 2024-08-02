## Розрахунки

1.  **Метод Монте-Карло**:
    
    -   Випадково згенеровано 10,000 точок у прямокутнику, обмеженому межами інтегрування.
    -   Підраховано частку точок, що потрапляють під графік функції.
    -   Обчислено площу під графіком як наближення до значення інтегралу.
2.  **Перевірочне обчислення**:
    
    -   Використано функцію `quad` з бібліотеки SciPy для точного обчислення визначеного інтеграла на заданому інтервалі.

## Результати

### Метод Монте-Карло


`Estimated area under the curve (Monte Carlo): 2.652` 

### Перевірочний результат

`Test result (quad): 2.666666666666667` 

## Висновки

-   **Точність результатів**: Значення, отримане за допомогою методу Монте-Карло, близьке до результату, отриманого функцією `quad`. Збільшення кількості випадкових точок підвищує точність розрахунків, наближаючи результат до аналітичного значення.
    
-   **Ефективність методу Монте-Карло**: Метод Монте-Карло є потужним інструментом для обчислення інтегралів, особливо коли аналітичне рішення складне або неможливе. Він надає приблизні результати, які можна уточнити, збільшуючи кількість випадкових точок.
    
-   **Порівняння з перевірочним розрахунком**: Результати обчислень методом Монте-Карло підтверджують свою правильність, оскільки вони близькі до точного значення, отриманого за допомогою функції `quad`.
    

Метод Монте-Карло добре працює для оцінки площі під кривою, і хоча його точність може залежати від кількості випадкових точок, він є надійним варіантом для чисельних інтегралів.