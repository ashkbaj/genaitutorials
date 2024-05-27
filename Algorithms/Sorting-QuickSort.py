arr = [96, 45, 56, 34, 12, 67, 87, 32, 54, 65, 34, 76, 23]

def quicksort(array)-> list:
    totalelements = len(array)
    index1 = 0
    index2 = totalelements-1
    pivot = array[0]
    pivotelement = array[0]

    for i in range(0, totalelements-1, +1):
        print(array[i])
        print(pivot)
        for j in range(totalelements-1, 0, -1):
            print(array[j])
            #while (j>=i):
            print(array[j] < pivot)
            print(array[i] > pivot)
            print(j>=i)
            if(array[j] < pivot) and (array[i] > pivot) and (j>=i):
                value1 = array[i]
                value2 = array[j]
                array[j] = value1
                array[i] = value2
                #break
                print("Replaced")
            else:
                print(array)
            pivot = array[j]
            j-=1
        i+=1




    #print(f"{pivotelement}")



quicksort(arr)