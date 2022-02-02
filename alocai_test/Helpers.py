from datetime import datetime, timedelta, timezone
import json
from django.http.response import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status

import uuid
import os

SUCCESS_CODE = 1


def JsonResult(success_code, data, http_status_code):
    return JsonResponse(data=data, status=http_status_code)


def SuccessResponse(data):
    return JsonResult(SUCCESS_CODE, data, status.HTTP_200_OK)


def ErrorResponse(custom_obj, body=None):
    if body is None:
        return JsonResult(custom_obj.code, custom_obj.message, custom_obj.http_code)
    return JsonResult(custom_obj.code, body, custom_obj.http_code)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    # return os.path.join(settings.MEDIA_URL, filename)
    return filename


def send_email(to_address, subject, body):
    send_mail(
        subject=subject,
        message=body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_address],
        fail_silently=False,
    )


def get_json_dump(dictionary):
    return json.dumps(dictionary, indent=4)


def get_stringify_dict(dictionary):
    return json.loads(json.dumps(dictionary), parse_int=str)


def is_valid_str(token):
    if token is not None and token.strip() != '':
        return True
    return False


def pop_key(dictionary, key):
    try:
        return dictionary.pop(key)
    except KeyError:
        return None


def last_day_in_prev_month(dt: timezone) -> timezone:
    return dt.replace(day=1) - timedelta(days=1)


def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))


def paginate(records, page_num: int, page_size: int):
    total_records = len(records)
    # reset the page num if total records for current page are 0
    if page_num < 1:  # or total_records <= (page_num - 1) * page_size         *** add this condition if you want to redirect to page 1 for larger page numbers
        page_num = 1

    if total_records == 0:
        page_start_index = page_start = page_end = total_records
    else:
        page_start_index = (page_num - 1) * page_size
        page_start = page_start_index + 1
        page_end = page_num * page_size
        # check if page end exceeds the total records then adjust the value
        page_end = total_records if page_end > total_records else page_end

    return page_num, page_start, page_end, total_records, records[page_start_index: page_end]
