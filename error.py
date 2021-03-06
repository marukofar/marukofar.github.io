class NotAllowFileError(Exception):
    def __init__(self, filename):
        self.message = filename + 'is not allowed'
        super().__init__(self.message)

try:
    f1 = open('neis0736.txt')
    # f2 = open('ab.txt','x')
    # f3 = open('def.txt')
    f4 = open('sdf.txt')

    # if f3.name == 'def.txt':
    #     raise NotAllowFileError(f3.name)

    # var = bad_var

except FileNotFoundError as e:
    print(e)

except FileExistsError as e:
    print(e)

except NotAllowFileError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print(f1.read())

    f1.close()

finally:
    print('End Process')
