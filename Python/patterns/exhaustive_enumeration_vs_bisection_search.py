# exhaustive enumeration (guess and check) incrementing
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    print("guess", guess)
    print("guess**2-x", abs(guess**2-x))
    print(abs(guess**2-x) >= epsilon)
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

# now with bisection search:
# logarithmic time algorithm, works more quickly than linear time.
# to do with first step divides options by half, then half again, so for gth guess its N/2^g
# guess converges on the order of log2N steps.
x = 25
epsilon = 0.01
num_guesses = 0
low = 0
high = x
guess = (high + low)/2
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2
    num_guesses += 1
print("num_guesses", num_guesses)
print(guess, "is close to the square root of", x)
