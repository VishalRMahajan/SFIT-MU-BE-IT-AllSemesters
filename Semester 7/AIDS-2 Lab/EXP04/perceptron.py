# Input Vectors (3 training examples, each of size 4)
X = [
    [1, -2, 0, -1],       # x1
    [0, 1.5, -0.5, -1],   # x2
    [-1, 1, 0.5, -1]      # x3
]

# Desired outputs
D = [-1, -1, 1]

# Initial weights
weights = [1, -1, 0, 0.5]

# Learning rate
alpha = 0.1


# Sign activation function
def sign(value):
    return 1 if value >= 0 else -1

# Training process
print("Initial Weights:", weights)

for i in range(len(X)):
    x = X[i]
    d = D[i]

    # Compute net input
    net = sum(weights[j] * x[j] for j in range(4))
    y = sign(net)

    print(f"\nStep {i+1}:")
    print(f"Input Vector x{i+1} = {x}")
    print(f"Desired Output d{i+1} = {d}")
    print(f"Net = {net}")
    print(f"Predicted Output = {y}")

    # Check if output matches
    if y != d:
        print("Mismatch! Updating weights...")
        error = d - y
        for j in range(4):
            weights[j] = weights[j] + alpha * error * x[j]
        print(f"Updated Weights = {weights}")
    else:
        print("Match! No update needed.")
        print(f"Weights remain = {weights}")


print("\nFinal Weights after training:", weights)
