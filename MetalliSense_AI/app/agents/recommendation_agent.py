target_min, target_max = TARGET_COMPOSITION[element]

if value < target_min:
    diff = min(target_min - value, MAX_ADDITION_PERCENTAGE)
    recommendation[element] = f"Add {round(diff,2)}%"

elif value > target_max:
    diff = min(value - target_max, MAX_REDUCTION_PERCENTAGE)
    recommendation[element] = f"Reduce {round(diff,2)}%"