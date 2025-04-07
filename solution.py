def can_jump(nums: list[int]) -> bool:
    max_reachable = 0
    for current_pos in range(len(nums)):
        # Если текущая позиция недостижима
        if current_pos > max_reachable:
            return False
        
        max_reachable = max(max_reachable, current_pos + nums[current_pos])
        
        if max_reachable >= len(nums) - 1:
            return True
        
    return True


print(can_jump([3, 2, 1, 0, 4]))