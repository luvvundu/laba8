import asyncio
import json
from collections import defaultdict

async def process_transactions(filename):
    with open(filename, 'r') as f:
        transactions = json.load(f)

    # группировка транзакций по категории
    category_totals = defaultdict(float)

    for transaction in transactions:
        category = transaction['category']
        amount = transaction['amount']
        category_totals[category] += amount

    # вывод информации о перерасходах
    for category, total in category_totals.items():
        if total > 100:  # порог для перерасхода
            print(f'Расход в категории "{category}" превышает 100: ${total:.2f}')

async def main(filename):
    await process_transactions(filename)

if __name__ == "__main__":
    filename = 'transactions.json'
    asyncio.run(main(filename))

