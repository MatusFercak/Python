def string_ends_with(string, ending):
    return True if string[len(string) - len(ending):] == ending else False







def main():
	print(string_ends_with('ahoj', 'hoj'))

if __name__ == '__main__':
	main()