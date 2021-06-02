from . import models


def init_paging_details(page_number, page_size):

    return models.PagingDetails(
        page_number=page_number,
        start_record=(page_number-1) * page_size,
        end_record=0,
        prev_page="",
        next_page="",
    )