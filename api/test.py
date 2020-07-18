import sys
sys.path.append('../lib')
import youtubedl


info = youtubedl.getinfo('https://www.youtube.com/watch?v=BaW_jenozKc')
print(info)