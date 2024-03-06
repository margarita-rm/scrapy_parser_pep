import scrapy
from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Должен собирать ссылки на документы PEP."""
        main_tag = response.css('section#pep-content')
        rows = main_tag.css("tr.row-even, tr.row-odd")

        for row in rows[1:]:
            columns = row.css('td')
            if not columns:
                continue
            data_columns = columns.css('a::text')
            if not data_columns:
                continue
            number_tag, name_tag = data_columns
            url = columns.css('a::attr(href)')
            if not url:
                continue
            yield response.follow(
                url.get(),
                callback=self.parse_pep,
                cb_kwargs={
                    'number': number_tag.get(),
                    'name': name_tag.get(),
                }
            )

    def parse_pep(self, response, number, name):
        """Должен парсить страницы с документами и формировать Items."""
        status = response.css('dt:contains("Status") + dd abbr::text').get()

        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )
