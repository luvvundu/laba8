import asyncio
import json
import random
import os
from datetime import datetime, timedelta

# варианты категорий
CATEGORIES = ["Еда", "Транспорт", "Коммунальные услуги", "Развлечения", "Одежда", "Здравоохранение"]

async def generate_transactions(num_transactions):
    transactions = []
    for i in range(num_transactions):
        transaction = {
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
            "category": random.choice(CATEGORIES),
            "amount": round(random.uniform(5.0, 500.0), 2)
        }
        transactions.append(transaction)

        # сохраняем каждые 10 транзакций в файл
        if (i + 1) % 10 == 0:
            await save_to_file(transactions)
            transactions = []  # Очищаем список после сохранения

    # сохраняем оставшиеся транзакции, если они есть
    if transactions:
        await save_to_file(transactions)

async def save_to_file(transactions):
    filename = 'transactions.json'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    existing_data.extend(transactions)

    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4)

    print(f'Сохранено {len(transactions)} транзакций в файл {filename}.')

async def main(num_transactions):
    await generate_transactions(num_transactions)

if __name__ == "__main__":
    num_transactions = int(input("Введите количество транзакций для генерации: "))
    asyncio.run(main(num_transactions))
