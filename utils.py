from flask import request


def pagination(query, page, page_size):
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    return query.limit(page_size).offset((page - 1) * page_size)
