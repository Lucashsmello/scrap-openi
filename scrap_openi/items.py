from dataclasses import dataclass


@dataclass
class ImageItem:
    case_uid: str
    case_pmcid: str
    docSource: str  # 'MPX' or 'PMC'
    articleType: str
    title: str
    journal_title: str
    journal_abbr: str
    journal_date: dict
    affiliate: str
    Problems: str
    imgLarge: str
    detailedQueryURL: str
    licenseType: str
    image_id: str
    image_caption: str
    image_modalityMajor: str
    image_mention: str
    image_urls: list[str]  # Special attribute that scrapy looks at in order to automatically download images.
    metainfo_api_params: dict
    image_captionConcepts: list[str] = None
    image_modalityMinor: str = None
    pmid: str = None
    ccLicense: str = None
    ### medpix specific attributes ###
    medpixFigureId: str = None
    medpixArticleId: str = None
    medpixImageURL: str = None
    #######
    ### pmc specific attributes ###
    pmc_url: str = None
    #######
