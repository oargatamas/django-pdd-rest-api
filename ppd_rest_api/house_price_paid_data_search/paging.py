
from django.conf import settings

from . import models


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


def set_paging_links(paging, url):
    number_of_items = paging.end_record - paging.start_record
    if number_of_items >= settings.PAGE_SIZE:
        paging.next_page = url  + "?pageNo=" + str(paging.page_number + 1)

    if paging.page_number > 1 :
        paging.prev_page = url + "?pageNo=" + str(paging.page_number -1)
