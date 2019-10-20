import datetime
import decimal


def books_to_dict(header: tuple, records: list) -> list:
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
        result.append(dict(zip(header, record)))
    return result
