"""
import sys
print("the command line arguments are :")
for i in sys.argv:
    print(i)

print("\n\n The Python is ", sys.path, '\n')
"""

if __name__ == "__main__":
    print("This program is being run itself")
else:
    print("I am being imported from another module")
    
