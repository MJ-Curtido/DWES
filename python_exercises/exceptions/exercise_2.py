try:
	print(int("3.5")) # --> ValueError
	print([1, 2][5]) # --> IndexError
	print({}["x"]) # --> KeyError
	print("a" + 1) # --> TypeError
	print(1 / 0) # --> ZeroDivisionError
	print(float("1,5")) # --> ValueError
except ValueError:
	print('ValueError')
except IndexError:
	print('IndexError')
except KeyError:
	print('KeyError')
except TypeError:
	print('TypeError')
except ZeroDivisionError:
	print('ZeroDivisionError')
except Exception as e:
	print(e)
