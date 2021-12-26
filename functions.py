cache = {}

def cache_decorator(func):
    def wrapper(*argv):
        argList = []
        for arg in argv:
            argList.append(arg)

        argTuple = tuple(argList)

        if argTuple in cache:
            print('Getting value from cache')
            result = cache[argTuple]
        else:
            print('Putting value into cache')
            result = func(*argv)
            cache[argTuple] = result

        return result

    return wrapper

def type_check(**kwargs_types):
    def decorator_type_check(func):
        def wrapper(*argv):

            i = 0
            for var_name,var_type in kwargs_types.items():
                if len(argv) == i:
                    break

                if type(argv[i]) is not var_type:
                    raise Exception(f'Variable with name \'{var_name}\' should has type {var_type}, but has type {type(argv[i])}')
                i+=1
            return func(*argv)
        return wrapper
    return decorator_type_check

