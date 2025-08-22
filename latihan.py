from typing import List
import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        window = []  # ini list terurut untuk sliding window

        for i, num in enumerate(nums):
            # cari posisi penyisipan num dalam window
            pos = bisect.bisect_left(window, num)

            # cek apakah ada kandidat di posisi pos (>= num)
            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True

            # cek kandidat di posisi sebelumnya (< num)
            if pos > 0 and abs(window[pos - 1] - num) <= valueDiff:
                return True

            # sisipkan num ke window (terurut)
            bisect.insort(window, num)

            # jaga ukuran window agar tidak lebih dari indexDiff
            if len(window) > indexDiff:
                # hapus elemen yang keluar dari jangkauan
                old = nums[i - indexDiff]
                old_pos = bisect.bisect_left(window, old)
                window.pop(old_pos)

        return False
