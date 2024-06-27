def merge(nums1, m, nums2, n):
    # cancella pass e scrivi il tuo codice
    while n != 0:
        del nums1[-1]
        n -= 1
    while len(nums2) != 0:
        nums1.append(nums2[0])
        del nums2[0]
    nums1.sort()

    return nums1

	
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)

print()	
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)

print()
nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)