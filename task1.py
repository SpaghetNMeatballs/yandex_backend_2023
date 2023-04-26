class Datacenter:
    def __init__(self, m: int):
        self.r = 0
        self.m = m
        self.a = m
        self.state = set()

    def reset(self):
        self.r += 1
        self.state = set()
        self.a = self.m

    def disable(self, to_disable: int):
        if to_disable not in self.state:
            self.state.add(to_disable)
            self.a -= 1

    def get_val(self) -> int:
        return self.a * self.r


def getmaxind(dc_arr: list[Datacenter], n: int) -> int:
    result = 0
    for i in range(1, n):
        cur = dc_arr[i].get_val()
        if cur > dc_arr[result].get_val():
            result = i
    return result + 1


def getminind(dc_arr: list[Datacenter], n: int) -> int:
    result = 0
    for i in range(1, n):
        if dc_arr[i].get_val() < dc_arr[result].get_val():
            result = i
    return result + 1


if __name__ == "__main__":
    n, m, q = [int(i) for i in input().split()]
    dc_arr = [Datacenter(m) for i in range(n)]
    for i in range(q):
        operation = input().split()
        if operation[0] == 'GETMAX':
            print(getmaxind(dc_arr, n))
            continue
        elif operation[0] == 'GETMIN':
            print(getminind(dc_arr, n))
            continue
        dc_index = int(operation[1]) - 1
        if operation[0] == 'RESET':
            dc_arr[dc_index].reset()
            continue
        elif operation[0] == 'DISABLE':
            server_index = int(operation[2]) - 1
            dc_arr[dc_index].disable(server_index)
