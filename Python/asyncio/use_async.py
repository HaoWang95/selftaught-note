from time import sleep


import asyncio

async def my_coroutine() -> None:
    sleep(100)
    print('Hello World')


async def co_add_one(num: int) -> int:
    return num +1

def add_one(num: int) -> int:
    return num + 1


if __name__ == '__main__':
    print("Test async and await with coroutine") 
    co_add_one_result = asyncio.run(co_add_one(1))
    add_one_result = add_one(1)
    print(f'Function {co_add_one.__name__} is called -> {co_add_one_result}, type: {type(co_add_one_result)}')
    print(f'Function {add_one.__name__} is called -> {add_one_result}, type: {type(add_one_result)}')