import datetime
import decimal


BOOK_HEADER = ('ISBN', '书名', '作者', '出版社', '定价',
               '封面', '类别', '库存', '描述信息', '出版日期')
ORDER_HEADER = ()
USER_HEADER = ()


def books_to_dict(records: list):
    """
    transfrom book records into dict

    tips: all the values' type is str
    """
    result = []
    for record in records:
        record = list(record)
        for index, value in enumerate(record):
            if isinstance(value, datetime.date):
                record[index] = value.isoformat()  # date trans to str
            elif isinstance(value, decimal.Decimal):
                record[index] = str(value)  # decimal trans to str
        result.append(dict(zip(BOOK_HEADER, record)))
    return result
