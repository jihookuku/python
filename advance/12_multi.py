# try 코드 안에서 여러개의 예외가 발생한 경우...
import traceback

# 1. 생겨난 예외마다 각기 다른 처리를 해주고 싶은 때
try:
    pass
except IOError:
    pass
except KeyboardInterrupt:
    pass
except ValueError:
    pass

# 2. 어떤 예외가 발생하던지 동일한 처리를 하고 싶을때
try:
    pass
except Exception as e: # 예외의 최상위 부모이기 때문에 다른 자식 예외들이 모두 들어올 수 있다.
    traceback.print_exc()