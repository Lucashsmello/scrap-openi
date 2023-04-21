from .items import ImageItem

BOT_NAME = "scrap_openi"

SPIDER_MODULES = ["scrap_openi.spiders"]
NEWSPIDER_MODULE = "scrap_openi.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrap_openi (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

LOG_LEVEL = 'INFO'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 64

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 64
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrap_openi.pipelines.MyImagesPipeline': 1,
}


# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
# https://docs.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-exports
FEEDS_overwrite_option = True
FEEDS = {
    'extracted_dataset/images.csv': {
        'format': 'csv',
        'item_classes': [ImageItem],
        'overwrite': FEEDS_overwrite_option
    }
}

IMAGES_STORE = 'extracted_dataset/images/'


### Custom Settings used inside the spiders ###

CASESPIDER_MIN_INDEX = 1
CASESPIDER_MAX_INDEX = 121 # default is all images.

# See https://openi.nlm.nih.gov/services?it=xg#searchAPIUsingGET
# Image type: Exclude Graphics [xg], Exclude Multipanel [xm], X-ray [x], Ultrasound [u], Photographs [ph], PET [p], Microscopy [mc], MRI [m], Graphics [g], CT Scan [c],
CASESPIDER_API_GET_PARAMS = {
    'it': ['x', 'xg', 'xm'],  # Image Type
    'vid': '0'
}
