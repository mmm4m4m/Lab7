def cast(new_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                print(f'Преобразуем {result} из {type(result)} в {new_type}')
                return new_type(result)
            except:
                print(f'Ошибка преобразования, нельзя преобразовать тип {type(result)} в {new_type}')
                return result
        return wrapper
    return decorator


@cast(str)
def plus(a, b):
    return a + b


@cast(list)
def invalid_func():
    return 1


@cast(list)
def return_dict_result():
    return {'s': 1, 'k': 2}


if __name__ == '__main__':
    res1 = plus(1, 2)
    print(res1)
    res2 = invalid_func()
    print(res2)
    res3 = return_dict_result()
    print(res3)
    
