import hashlib
import json
from secrets import token_bytes, token_hex, token_urlsafe
import os
from pathlib import Path
import hmac

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


def use_hmac():
    hmac_sha256 = hmac.new('secret_key'.encode('utf-8'), msg='thisismypassword'.encode(), digestmod=hashlib.sha256)
    hmac_sha256.digest_size = 64
    hashed_value = hmac_sha256.digest()
    print(f'A hased sha256 value: {hashed_value}')
    if hashed_value == hmac_sha256.digest():
        print(f'Hasing the same value generates same results of length {hmac_sha256.digest_size}')

    hmac_sha256.digest_size = 32
    print(f'A 32bit hashed value: {hmac_sha256.digest()}')
    print(f'hex version: {hmac_sha256.hexdigest()}')
    print(hmac_sha256.name)


def authenticate_message(msg: str='default message'):
    hash_algo = hmac.new(b'secret_key', msg=msg.encode() ,digestmod=hashlib.sha256)
    hash_value = hash_algo.hexdigest()
    authenticated_message = {
        'message': list(msg),
        'hash_value': hash_value
    }
    return json.dumps(authenticated_message)


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
    use_hmac()
    json_result = authenticate_message(msg='How are you doing today?')
    print(f'hashed json message: {json_result}')