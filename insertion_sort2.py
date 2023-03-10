class Solution:
    def insertion_sort(self, lst: List[int]) -> None:
        for i in range(1, len(lst)):
            min_ind = i

            while min_ind > 0 and lst[min_ind - 1] > lst[min_ind]:
                # Swap elements that are out of order
                lst[current_index], lst[current_index - 1] = lst[current_index - 1], lst[current_index]
                current_index -= 1
                
#may be it is better than first implementation of insertion sort on my repository. anyway it is easier implementation
