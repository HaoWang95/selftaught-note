from secrets import token_bytes, token_hex, token_urlsafe
import os
from pathlib import Path

def get_os_urandom():
    return os.urandom(64)

def get_token_bytes():
    return token_bytes(64)

def get_token_hex():
    return token_hex(64)

def get_token_urlsafe():
    return token_urlsafe(64)

def get_current_path():
    print(Path('.'))


if __name__ == '__main__':
    os_urandom = get_os_urandom()
    print(f'os_urandom type: {type(os_urandom)}, value: {os_urandom}')
    print(os_urandom.hex())

    token_with_bytes = get_token_bytes()
    token_with_hex = get_token_hex()
    token_with_urlsafe = get_token_urlsafe()
    print(f'token_with_bytes: {token_with_bytes}')
    print(f'token_with_bytes to hex: {token_with_bytes.hex()}')
    print(f'token_with_hex: {token_with_hex}')
    print(f'token_with_urlsafe: {token_with_urlsafe}')
    print(f'token_with_urlsafe to hex: {token_with_urlsafe.encode().hex()}')
    print(f'length of token_with_urlsafe -> {len(token_with_urlsafe)}')
    print(f'length of token_with_urlsafe to hex -> {len(token_with_urlsafe.encode().hex())}')

    if len(token_with_hex) == len(token_with_bytes.hex()):
        print(f'token with bytes are the same length of token with hex, {len(token_with_hex)}')

    if len(token_with_hex) == len(token_with_urlsafe.encode().hex()) / 2:
        print(f'All three of them share the same length, {len(token_with_urlsafe.encode().hex())}')

    get_current_path()