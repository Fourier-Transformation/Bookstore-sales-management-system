import datetime
import decimal


BOOK_HEADER = ('isbn', 'name', 'author', 'publisher', 'price',
               'cover', 'category', 'amount', 'description', 'publish_date')
ORDER_HEADER = ()
USER_HEADER = ()


def books_to_dict(records: list):
    """
    transfrom book records into dict
    """
    result = []
    for record in records:
        record = list(record)
        for index, value in enumerate(record):
            if isinstance(value, datetime.date):
                record[index] = value.isoformat()  # date trans to str
            elif isinstance(value, decimal.Decimal):
                record[index] = float(value.quantize(
                    decimal.Decimal('0.00')))  # decimal trans to str
        result.append(dict(zip(BOOK_HEADER, record)))
    return result
