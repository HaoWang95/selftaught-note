import re
from typing import List, Pattern

pattern_str: str = r'(.*\_[0-9])'

pattern = re.compile(pattern=pattern_str)

source_str = [
    'INVALID_0', 'INVALID_1', 'INVALID_2', 'INVALID_3','INVALID_4',
    'INVALID_5', 'INVALID_6', 'INVALID_7', 'INVALID_8', 'INVALID_9'
    ]

def match_lists(pattern: Pattern[str], source: List[str]):
    """
    Perform the regex matching and print the matching results.
    """
    for item in source:
        temp = pattern.match(item)
        if temp:
            print(f'{item} against {pattern.pattern}: matched part {temp.group()}')

if __name__ == '__main__':
    match_lists(pattern=pattern,source=source_str)