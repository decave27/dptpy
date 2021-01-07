import os
from .. import Node_Ignore, Node_Docker, Python_Ignore, Python_Docker
class Help():
    def __init__(self, lang : str = "kr"):
        if lang == "kr":
            self.KR()
    def KR(self):
        e = """Deplux 비공식 설정 도구

optional arguments:
  -h, --help            이 도움말 메세지를 출력합니다(EN)
  --kh, --krhelp        이 도움말 메세지를 출력합니다(KR)
  --i, --init, --setup  배포를 위한 Dockerfile을 생성합니다
  --z, --zip, --build   명령어를 실행한 루트 디렉터리를 Deplux용 호스팅 파일로 압축합니다
  --n,  --new           새로운 deplux 프로젝트를 만듭니다
        """
        print(e)

   