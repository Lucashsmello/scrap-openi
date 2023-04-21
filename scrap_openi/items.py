from dataclasses import dataclass


@dataclass
class ImageItem:
    case_uid: str
    case_pmcid: str
    docSource: str  # 'MPX' or 'PMC'
    title: str
    journal_title: str
    affiliate: str
    Problems: str
    imgLarge: str
    detailedQueryURL: str
    image_id: str
    image_caption: str
    image_modalityMajor: str
    image_mention: str
    image_urls: list[str]  # Special attribute that scrapy looks at in order to automatically download images.
    metainfo_api_params: dict
    MeSH_minor: list[str]
    MeSH_major: list[str]
    abstract: str = None
    articleType: str = None
    journal_abbr: str = None
    journal_date: dict = None
    image_captionConcepts: list[str] = None
    image_modalityMinor: str = None
    pmid: str = None
    licenseType: str = None
    ccLicense: str = None
    ### medpix specific attributes ###
    medpixFigureId: str = None
    medpixArticleId: str = None
    medpixImageURL: str = None
    #######
    ### pmc specific attributes ###
    pmc_url: str = None
    #######
