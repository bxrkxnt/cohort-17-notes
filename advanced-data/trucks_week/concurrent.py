from multiprocessing import Pool

def a_function(num: int) -> int:
    return num**2

def a_function_two_params(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    with Pool(5) as p:
        print(p.starmap(a_function_two_params, [(1, 1), (2, 2), (3, 3)]))
