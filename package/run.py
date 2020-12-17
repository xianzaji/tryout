# from m1 import foo
import sys
print(sys.path)

sys.path.append('/home/t/project/tryout')
__name__='package.run' 
from .m1 import foo