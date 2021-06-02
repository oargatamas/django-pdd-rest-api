from . import models
from ppd_rest_api import settings


def init_paging_details(page_number):
    page_size = settings.PAGE_SIZE
    start = (page_number - 1) * page_size
    return models.PagingDetails(
        page_number=page_number,
        start_record=start,
        end_record=start + page_size,
        prev_page="",
        next_page="",
    )
