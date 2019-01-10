class Sort:
    """各种排序的Python实现
    """

    @staticmethod
    def merge(list_a, list_b):
        """将两个有序的序列从小到大合并到一起
        """
        new_list = []
        i = 0
        while i < len(list_a) and i < len(list_b):
            if list_a[i] < list_b[i]:
                new_list.append(list_a[i])
                list_a.pop(i)
            else:
                new_list.append(list_b[i])
                list_b.pop(i)
        if list_a:
            new_list.extend(list_a)
        if list_b:
            new_list.extend(list_b)
        return new_list

    @staticmethod
    def quick_sort_helper(my_list, left, right):
        mid_index = (left + right) // 2
        mid_value = my_list[mid_index]
        while left < right:
            while my_list[left] < mid_value:
                left += 1
            while my_list[right] > mid_value:
                right -= 1
            if left < right:
                temp = my_list[left]
                my_list[left] = my_list[right]
                my_list[right] = temp
                left += 1
                right -= 1
        return left

    @classmethod
    def merge_sort(cls, my_list):
        """归并排序
        """
        if len(my_list) < 2:
            return my_list
        mid_index = len(my_list) // 2
        left_list = cls.merge_sort(my_list[:mid_index])
        right_list = cls.merge_sort(my_list[mid_index:])
        return cls.merge(left_list, right_list)

    @classmethod
    def buble_sort(cls, my_list):
        """冒泡排序
        """
        len_my_list = len(my_list)
        for i in range(len_my_list-1):
            min_item = my_list[i]
            for j in range(i+1, len_my_list):
                if my_list[j] < min_item:
                    min_item = my_list[j]
                    my_list[j] = my_list[i]
                    my_list[i] = min_item
        return my_list

    @classmethod
    def quick_sort(cls, my_list):
        """快速排序
        """
        len_my_list = len(my_list)
        if len_my_list < 2:
            return my_list
        index = cls.quick_sort_helper(my_list, 0, len_my_list-1)
        if index > 0:
            cls.quick_sort_helper(my_list, 0, index-1)
        if index < len_my_list - 1:
            cls.quick_sort_helper(my_list, index, len_my_list-1)
        return my_list
