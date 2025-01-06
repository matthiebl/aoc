def memoize(cache: dict = {}):
    """Memoize wrapper that caches the results of a function call and returns earlier if already cached."""
    def decorator(fn):
        def wrapper(*args, **kwargs):
            key = (args) + tuple(kwargs.values())
            if key in cache:
                return cache[key]
            res = fn(*args, **kwargs)
            cache[key] = res
            return res
        return wrapper
    return decorator


def echo(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{func.__name__}({args}, {kwargs}) = {res}')
        return res
    return wrapper
