import scrapy
from scrapy import http
import logging
from ..items import ImageItem

_LOGGER = logging.getLogger(__name__)


# scrapy crawl case -s USER_AGENT="lhsmello (+http://github.com/Lucashsmello)" --logfile logs/log.log

class CaseSpider(scrapy.Spider):
    name = "case"

    def start_requests(self):
        url = 'https://openi.nlm.nih.gov/api/search'
        params = {'it': ['x', 'xg'],
                  'm': '1',
                  'n': '4'
                  }
        yield scrapy.FormRequest(url=url,
                                 method='GET',
                                 formdata=params,
                                 callback=self.parse)

    def parse(self, response: http.TextResponse, **kwargs):
        rjson = response.json()['list']
        for sr in rjson:
            yield response.follow(url=sr['detailedQueryURL'],
                                  callback=self.parse_detailed_case,
                                  # cb_kwargs=
                                  )

    def parse_detailed_case(self, response: http.TextResponse):
        rjson = response.json()['list'][0]

        case_params = {k: v for k, v in rjson.items() if k in ImageItem.__annotations__.keys()}
        case_params['case_uid'] = rjson['uid']
        case_params['case_pmcid'] = rjson['pmcid']

        extra_image_data = {f'image_{k}': v for k, v in rjson['image'].items()}

        image_urls = [response.urljoin(case_params['imgLarge'])]

        yield ImageItem(image_urls=image_urls,
                        **extra_image_data,
                        **case_params)
