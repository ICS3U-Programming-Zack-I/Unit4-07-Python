# Created by: Zack Isingoma
# Created on: 18th Jan 2022.
# uses a for loop to print
# numbers from 1000 to 2000
def main():
    for counter in range(1000, 2001, 1):
        if counter % 5 == 0:
            print("")
        print(counter, "", end="")
    print(" \nThanks for playing")


if __name__ == "__main__":
    main()
