import random
import math
import time
def buffon_fun(tou_sum,length=1.0,spacing=1.0):
    if not (0 < length <= spacing):
        print("warning,L should shorter than spaceing")
        
    intersection_count = 0

    for _ in range(tou_sum):
        y_center = random.uniform(0, spacing)
        theta = random.uniform(0, math.pi)
        half_proj_length = (length/2)*math.sin(theta)
        if (y_center - half_proj_length < 0) or \
            (y_center + half_proj_length > spacing):
            intersection_count += 1
        
    if intersection_count == 0:
        estimated_pi = float('inf')
    else:
        estimated_pi = (2 * length * tou_sum) / (intersection_count * spacing)
    return estimated_pi, intersection_count

if __name__ == "__main__":
    print("starting")
    L_str = input("请输入针长L:")
    D_str = input("请输入线距离D:")

    L = float(L_str)
    D = float(D_str)

    trails_counts = [1000, 1000, 50_000, 100_000]

    print(f"针长(L):{L},线距(D):{D}\n")

    for tou_sum in trails_counts:
        start_time = time.time()
        estimated_pi, intersection_count = buffon_fun(tou_sum, L, D)
        end_time = time.time()

        print(f"投掷次数: {tou_sum:,}")
        print(f"  相交次数: {intersection_count:,}")
        print(f"  估算 π: {estimated_pi:.6f}")
        print(f"  真实 π: {math.pi:.6f}")
        print(f"  误差: {abs(estimated_pi - math.pi):.6f}")
        print(f"  耗时: {end_time - start_time:.4f} 秒")
        print("-" * 30)
    
    print("\nend")