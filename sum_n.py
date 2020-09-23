# sum_n.py
# Marcela Gomez

# This program asks for a number input, then adds the whole numbers from
# 1 to n and prints the total. 

def main():

    print("This program adds the numbers from 1 to n.")

    total = eval(input("Enter a number: "))
    for i in range(1,total,1):
        total = total + i

    print(total)

main()
        



    
