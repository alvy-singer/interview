class Search:

    @classmethod
    def binary_search(cls, my_list, x):
        """二分法搜索
        """
        len_my_list = len(my_list)
        if len_my_list == 1:
            if my_list[0] == x:
                return True
            else:
                return False
        mid_index = len_my_list // 2
        mid_value = my_list[mid_index]
        if x < mid_value:
            return cls.binary_search(my_list[:mid_index], x)
        elif x > mid_value:
            return cls.binary_search(my_list[mid_index:], x)
        else:
            return True
