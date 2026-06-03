# try_except2.py
print("try-except")
# path = 'myfile.txt'
path = r'ch13\exception\myfile.txt'

# # FileNotFoundError
# f = open(path)      # mode 기본값: 'r'
# # f = open(path, 'w')
# # f.write('hello')
# # io.UnsupportedOperation
# s = f.readline()
# # ValueError
# i = int(s.strip())

try:
    f = open(path)
    s = f.readline()
    i = int(s.strip())
except (RuntimeError, TypeError, NameError):
    print("RuntimeError, TypeError, NameError 중 하나의 예외 처리!")
except OSError:
    print("OSError!")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except ValueError as e:
    print("정수형으로 변환할 수 없습니다.")
    print('e:', e)        # 예외 관련 정보 표시
except Exception as err:
    print('Exception:', err)

print("program exit")

# BaseException
#  |___ Exception
#         |____ OSError
#         |____ ValueError
#         |____ ...