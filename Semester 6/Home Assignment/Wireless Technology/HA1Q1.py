# Given values
C_total = 960  # Total available voice channels
cell_area = 6  # Area of each cell in km^2
total_area = 2000  # Total coverage area in km^2

def calculate_capacity(N):
    cluster_area = N * cell_area  # Area of one cluster
    num_clusters = round(total_area / cluster_area)  # Proper rounding
    channels_per_cell = C_total / N  # Channels per cell
    system_capacity = num_clusters * C_total  # Total system capacity
    return cluster_area, num_clusters, channels_per_cell, system_capacity

# For N = 4
cluster_area_N4, clusters_N4, channels_per_cell_N4, capacity_N4 = calculate_capacity(4)

# For N = 7
cluster_area_N7, clusters_N7, channels_per_cell_N7, capacity_N7 = calculate_capacity(7)

# Output results
print("• Total available channels = 960")
print(f"• Cell area = {cell_area} km^2")
print(f"• Total coverage area = {total_area} km^2\n")

# For N = 4
print(f"• Area of a cluster with reuse N=4: {cluster_area_N4} km^2")
print(f"• Number of clusters for covering total area with N=4: {clusters_N4}")
print(f"• Number of channels per cell = {int(channels_per_cell_N4)}")
print(f"• System capacity = {clusters_N4} x {C_total} = {capacity_N4} channels\n")

# For N = 7
print(f"• Area of a cluster with reuse N=7: {cluster_area_N7} km^2")
print(f"• Number of clusters for covering total area with N=7: {clusters_N7}")
print(f"• Number of channels per cell = {int(channels_per_cell_N7)}")
print(f"• System capacity = {clusters_N7} x {C_total} = {capacity_N7} channels\n")

# Impact of decreasing N
if capacity_N4 > capacity_N7:
    print("Decreasing the reuse factor N increases the system capacity but increases interference.")
else:
    print("Decreasing the reuse factor N does not significantly increase the system capacity.")