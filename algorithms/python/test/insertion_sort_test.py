from insertion_sort import *
import time

test_cases = [([4, 3, 2, 1],[1, 2, 3, 4]), ([9, 5, -3, 7],[-3, 5, 7, 9])]

def test(input1, expected_output):
    print("--------------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    start = time.time()
    result = insertion_sort(input1)
    end = time.time()
    timeout = 1.00
    if(end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        print(f"Actual: {result}")
        print("Fail")
        return False
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
        print(f"Actual: {result}")
        print("Fail")
        return False
    
def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed +=1
        else:
            failed += 1
    if failed == 0:
        print("========== PASS ==========")
    else:
        print("========== FAIL ==========")
    print(f"{passed} passed, {failed} failed")


main()
