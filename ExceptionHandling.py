#Exception Handling & try-catch block
class MetesError(Exception):
    pass

def badMethod():
    raise MetesError("Index out of bounds")


try:
    badMethod()
except MetesError as me:
    print("Oha! {0}".format(me))
except Exception as e:
    print("Oops! {0}".format(e))
