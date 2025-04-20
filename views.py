## 第三方 API 搜索（views.py）
import requests
from django.views import View
from music.utils.config import get_api_keys  # 从setting.yml获取API密钥

class QQMusicSearch(View):
    def get(self, request):
        keyword = request.GET.get('q')
        api_url = f"https://c.y.qq.com/soso/fcgi-bin/client_search_cp?keywords={keyword}"
        response = requests.get(api_url)
        return JsonResponse(response.json())  # 返回搜索结果

class KuGouSearch(View):
    def get(self, request):
        keyword = request.GET.get('q')
        api_url = f"https://www.kugou.com/yy/index.php?r=search/song&keyword={keyword}"
        response = requests.get(api_url)
        return JsonResponse(response.json())