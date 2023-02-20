import random
def main():
    with open("./hyakunin.txt", encoding="utf-8") as f:
        wakas = [s.strip() for s in f.readlines()]

        print(wakas[random.randrange(len(wakas))])
    #print(wakas[0])

if __name__ == '__main__':
   main()