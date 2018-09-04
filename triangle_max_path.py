import time


tr = [[5],[1,7],[3,4,6],[8,4,3,1]] # 21


class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


class InvalidLengthError(Exception):
    pass


class InvalidNumberError(Exception):
    pass


def max_path(tr, i=0, j=0):
    # try:

    # 1 check for array - IvalidInputError
    # 2 check len  - InvalidLengthError
    # 3 check for int in array - InvalidNumberError

    # try:
    #     for i in range(len(tr)-1):
    #         if len(tr[i+1])-len(tr[i]) != 1:
    #             raise InvalidLengthError
    #     for row in tr:
    #         for num in row:
    #             if not int(num):
    #                 raise InvalidInputError
    # except InvalidInputError:
    #     print("Incorrect input value")
    # except InvalidLengthError:
    #     print("Incorrect length of triangle")

    step = len(tr)
    if i == step:
        return 0
    return tr[i][j] + max(max_path(tr, i+1, j), max_path(tr, i+1, j+1))


# def max_path_bottom_up(tr):
#     while len(tr)>1:
#         t0 = tr.pop()
#         t1 = tr.pop()
#         tr.append([max(t0[i], t0[i+1]) + t for i,t in enumerate(t1)])
#     return tr[0][0]    

def main():
    print(max_path(tr))
    # print(max_path_bottom_up(tr2))


if __name__ == "__main__":
    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))
    main()