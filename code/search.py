class Search:

    @classmethod
    def binary_search(cls, my_list, x, start_index=0):
        """二分法搜索
        """
        len_my_list = len(my_list)
        if len_my_list == 1:
            if my_list[0] == x:
                return 0
            else:
                return False
        mid_index = len_my_list // 2
        mid_value = my_list[mid_index]
        if x < mid_value:
            return cls.binary_search(my_list[:mid_index], x, start_index=start_index)
        elif x > mid_value:
            return cls.binary_search(my_list[mid_index:], x, start_index=start_index+mid_index)
        else:
            return start_index + mid_index
