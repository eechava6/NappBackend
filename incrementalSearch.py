from function import f
import numpy as np

def incrementalSearch (start, step, stop, decimals = 4):
    return_list = []
    evaluated = f(start)
    points = np.arange(start,stop,step)

    for point in points:
        mult = evaluated * f(point)
        root = True if evaluated < 0 else False 
        row = {'f(x)' : round(f(point), decimals),
            'root': root,
            'f(a)*f(b)':round(mult,decimals),
            'range':[round(point-step,decimals),round(point,decimals)]
            }
        return_list.append(row)
        evaluated = f(point)
        

    return return_list



def main():
    print("ingrese start")
    start = input()
    print("ingrese stop")
    stop = input()
    print("ingrese step")
    step = input()

    result = incrementalSearch(1,1,10)

    i=0
    while i < len(result):
        print(" | "+str(result[i][0])+" | "+str(result[i][1])+" | "+str(result[i][2])+" | "+str(result[i][3])+" | "+str(result[i][4])+" | "+str(result[i][5])+" | ")
        i += 1


if __name__ == "__main__":
    main()

