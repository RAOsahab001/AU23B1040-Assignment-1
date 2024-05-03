from ice_cream import *
 
def main():

    scoop_size=input('Enter size of scoop: ')
    toopings=input('Enter toopings: ')
    add_topping(scoop_size, toopings)

    s=input('Enter shake: ')
    make_shake(s)



if __name__ == "__main__":
    main()
