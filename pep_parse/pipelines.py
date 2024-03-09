import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

from .settings import RESULTS_DIR

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        (BASE_DIR / RESULTS_DIR).mkdir(exist_ok=True)
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        with open(
            BASE_DIR / RESULTS_DIR / file_name,
            'w',
            newline='',
            encoding='utf-8'
        ) as file:
            csv.writer(
                file, quoting=csv.QUOTE_MINIMAL, dialect=csv.excel
            ).writerows(
                [
                    ['Status', 'Amount'],
                    *self.statuses.items(),
                    ['Total', sum(self.statuses.values())]
                ]
            )
