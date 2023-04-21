import scrapy
from scrapy import http
import logging
from ..items import ImageItem
import requests
from tqdm import tqdm


_LOGGER = logging.getLogger(__name__)


# scrapy crawl case -s USER_AGENT="lhsmello (+http://github.com/Lucashsmello)" --logfile logs/log.log


class CaseSpider(scrapy.Spider):
    """This spider uses the following settings:
    CASESPIDER_MIN_INDEX, CASESPIDER_MAX_INDEX, CASESPIDER_API_GET_PARAMS
    """
    name = "case"
    _OPENI_PAGE_MAX_SIZE = 100

    def start_requests(self):
        url = 'https://openi.nlm.nih.gov/api/search'

        params = self.settings.getdict('CASESPIDER_API_GET_PARAMS')
        params.update({
            'm': '1',
            'n': '1',
        })

        total = int(requests.get(url, params=params).json()['total'])
        min_idx = self.settings.getint('CASESPIDER_MIN_INDEX')
        max_idx = self.settings.getint('CASESPIDER_MAX_INDEX', 1000000)
        max_idx = min(total, max_idx)
        _LOGGER.info(f'Total number of objects to scrap: {max_idx}')

        for i in tqdm(range(min_idx, max_idx+1, CaseSpider._OPENI_PAGE_MAX_SIZE)):
            params.update({
                'm': str(i),
                'n': str(min(i + CaseSpider._OPENI_PAGE_MAX_SIZE-1, max_idx))
            })
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

        # Only fields that are mapped in ImageItem Object
        case_params = {k: v for k, v in rjson.items() if k in ImageItem.__annotations__.keys()}
        case_params['case_uid'] = rjson['uid']
        case_params['case_pmcid'] = rjson['pmcid']

        extra_image_data = {f'image_{k}': v for k, v in rjson['image'].items()}
        extra_image_data = {k: v for k, v in extra_image_data.items() if k in ImageItem.__annotations__.keys()}

        mesh_data = {'MeSH_minor': rjson['MeSH']['minor'],
                     'MeSH_major': rjson['MeSH']['major']
                     }

        image_urls = [response.urljoin(case_params['imgLarge'])]

        yield ImageItem(image_urls=image_urls,
                        metainfo_api_params=self.settings.getdict('CASESPIDER_API_GET_PARAMS'),
                        **mesh_data,
                        **extra_image_data,
                        **case_params)
