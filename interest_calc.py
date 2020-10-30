# == SIMPLE INTEREST RATE CALCULATOR ==
#       -Morning Hernandez, mouseandweb.com

#   typical result:
#   Enter the starting balance: 1000
#   Enter the interest rate: 5
#   Initial balance: 1000.0
#   Interest rate: 5.0
#   Duration: 535 seconds
#   Compounded balance: 1000.0008498227855
#   You made 0.0008498227855398 in 535 seconds.

# importing time module for counting.

import time


# counter counts the seconds accumulating while the compound_bal loop runs.
# This way we know how much money was gained per second.
counter = 0

# init_bal and int_rate are converted to floating point numbers from user
# input. The former is the initial balance before compounding. The latter is
# the interest rate entered as a whole percentage.
init_bal = float(input('Enter the starting balance: '))

int_rate = float(input('Enter the interest rate: '))

# int_persec calculates the interest gained in one second. This does not
# account for a leap year.
int_persec = int_rate*.01/31536000

# compound_bal is the balance after compounding interest is added.
compound_bal = init_bal * int_persec + init_bal

# commented out the printing of init_bal to keep the output to one line while
# running through the coumpound_bal loop.

# using the time module to pause for one second before printing the first
# compounded balance with one second of interest gained.
time.sleep(1)

# this while loop will continuously update the one line of output showing the
# current compounded balance. As long as the init_bal input by the end user is
# greater than 0 the while loop will run.
while compound_bal > 0:
    # a try/except to allow the end user to stop the loop
    # and view their results.
    try:
        # print one line and print over it with each iteration. This keeps the
        # loop's output to one line.
        print('', compound_bal, '\r', end='')

        # 1 iteration of the loop per second.
        time.sleep(1)

        # this is compounding interest every second. This is the equivalent to
        # reinvesting your gains immediately upon receipt. This is the
        # previously compounded balance in addition to the interest gained on
        # that balance over one second of time.
        compound_bal += compound_bal * int_persec

        # add one second to the counter variable, counter.
        counter += 1

        # this is to interrupt the loop using the keyboard.
        # when the loop is interrupted the results will be printed.

    except KeyboardInterrupt:
        # break out of the loop to run the rest of the program.
        break

# printing the results. The first print statement contains \r to start the
# results on a new line.
print('\rInitial balance:', init_bal)
print('Interest rate:', int_rate)
print('Duration:', counter, 'seconds')
print('Compounded balance:', compound_bal)
print('You made', (compound_bal - init_bal), 'in', counter, 'seconds.')
