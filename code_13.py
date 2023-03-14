# Jose Miguel Reyes
# CIS 3301
# Merge sort algorithm

def merge(bottom, top):
    i = j = 0

    final = []

    while(i < len(bottom) and j < len(top)):
        if bottom[i] > top[j]:
            final.append(top[j])
            j += 1
        else:
            final.append(bottom[i])
            i += 1

    if i <= len(bottom): final.extend(bottom[i:])
    if j <= len(top): final.extend(top[j:])

    return final

def get_merge_sorted_list(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    
    mid = len(unsorted_list) // 2

    low = get_merge_sorted_list(unsorted_list[:mid])
    high = get_merge_sorted_list(unsorted_list[mid:])

    return merge(low, high)



if __name__ == "__main__":
    pass #Remove this line and program your function calls to locally test the functionallity of merge sort