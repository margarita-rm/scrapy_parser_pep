import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent


class PepParsePipeline:
    items = []

    def open_spider(self, spider):
        ...

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        statuses = {}
        for item in self.items:
            item = dict(item)
            statuses.update(
                {item['status']: statuses.get(item['status'], 0) + 1}
            )
        now_formatted = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        with open(
            BASE_DIR / 'results' / file_name, 'w', encoding='utf-8'
        ) as file:
            file.write('Статус,Количество\n')
            for key, value in statuses.items():
                file.write(f'{key},{value}\n')
            file.write(f'Total,{sum(statuses.values())}\n')
