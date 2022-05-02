from pos_log.tests.tools.customed_api_testcase import CustomedAPITestCase
from typing import Callable, Iterable, Dict, List
from collections import deque
import json

"""
    Writer: 하정현
"""

def validator_certain_type(t, a) -> Callable:
    if isinstance(a, Dict):
        return t.assertDictContainsSubset
    elif isinstance(a, Iterable):
        return t.assertItemsEqual
    else:
        return t.assertEqual

def test_runner(test_func : Callable):
    def __test_runner(func: Callable):
        def __wrapper(test_e: CustomedAPITestCase):
            # 테스트 파일
            test_f: str = f"{test_e.input_root}/{test_e.input_files[func.__name__]}"

            # 테스트 케이스 가져오기
            with open(test_f, 'rt') as f:
                cases = json.load(f)['case']
                
            for case in cases:
                # 테스트 케이스 마다 실행
                topic, ipt, answer = case['topic'], case['input'], case['answer']

                output = test_func(test_e, **ipt)
                err_msg: str \
                    = f"\n\nIn Topic: {topic}\ninput: {ipt}\noutput: {output}\nbut answer: {answer}"

                validator_certain_type(test_e, answer)(answer, output, msg=err_msg)
            return func(test_e)
        return __wrapper
    return __test_runner