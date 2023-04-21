from scrapy.pipelines.images import ImagesPipeline
import logging
from .items import ImageItem

LOGGER = logging.getLogger(__name__)


class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item: ImageItem = None):
        image_filename = f'{item.case_uid}/{item.image_id}'
        return image_filename
