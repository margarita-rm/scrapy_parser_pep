import scrapy
from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        """Собирает ссылки на документы PEP."""
        rows = response.css("section#pep-content tr.row-even, tr.row-odd")

        for row in rows[1:]:
            url = row.css('td a::attr(href)').get()
            if url:
                yield response.follow(
                    url,
                    callback=self.parse_pep,
                    meta={"row": row}
                )

    def parse_pep(self, response):
        """Парсит страницы с документами и формирует Items."""
        number_tag, name_tag = response.meta['row'].css('td a::text')
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        yield PepParseItem(
            number=number_tag.get(),
            name=name_tag.get(),
            status=status,
        )
