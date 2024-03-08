import datetime as dt
from collections import defaultdict
from pathlib import Path

from .settings import RESULTS_DIR

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        statuses = defaultdict(int)
        for item in self.items:
            statuses[item['status']] += 1
        now_formatted = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        (BASE_DIR / RESULTS_DIR).mkdir(exist_ok=True)
        with open(
            BASE_DIR / RESULTS_DIR / file_name, 'w', encoding='utf-8'
        ) as file:
            file.write('Status,Amount\n')
            file.writelines([
                f'{key},{value}\n'
                for key, value in statuses.items()
            ])
            file.write(f'Total,{sum(statuses.values())}\n')
