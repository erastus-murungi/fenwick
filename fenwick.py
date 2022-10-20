import operator as op


class Fenwick1D:
    def __init__(self, data, group_operation=op.add):
        self.group_operation = group_operation
        data = [0] + data
        for index in range(1, len(data)):
            parent = index + (index & -index)
            if parent < len(data):
                data[parent] = group_operation(data[parent], data[index])
        self.data = data

    def point_update(self, index, diff):
        while index < len(self.data):
            self.data[index] = self.group_operation(diff, self.data[index])
            index += index & -index

    def prefix_sum(self, index):
        aggregate = 0
        while index != 0:
            aggregate = self.group_operation(aggregate, self.data[index])
            index -= index & -index
        return aggregate

    def range_query(self, frm, to):
        return self.prefix_sum(to) - self.prefix_sum(frm - 1)

    def __repr__(self):
        return repr(self.data)


if __name__ == "__main__":
    bit = Fenwick1D([1, 2, 3, 4, 5, 6])
    print(bit)
    print(bit.prefix_sum(1))
    print(bit.prefix_sum(2))
    print(bit.prefix_sum(3))
    print(bit.prefix_sum(4))
    print(bit.prefix_sum(5))
    print(bit.prefix_sum(6))
    bit.point_update(1, 2)
    print(bit.prefix_sum(6))

