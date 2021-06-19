def string_ends_with(string, ending):
    return True if string[len(string) - len(ending):] == ending else False

def move_zeros(array):
    for a in array:
        for i in range(len(array)-1):
            if array[i] == 0:
                array[i],array[i+1] = array[i+1],array[i]
    return array


def main():
	print(string_ends_with('ahoj', 'hoj'))
	print(move_zeros([0,1,2,30,50,0,4,0]))

if __name__ == '__main__':
	main()