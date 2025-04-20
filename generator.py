import os
from django.core.wsgi import get_wsgi_application
from django.template.loader import render_to_string
from music.utils.config import load_config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_generator.settings')
application = get_wsgi_application()

def generate_static_files():
    config = load_config('setting.yml')
    output_dir = 'public'
    
    # 生成首页
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(render_to_string('index.html', {'config': config}))
    
    # 生成收藏页和歌曲详情页（逻辑类似）
    # ... 遍历本地/第三方音乐数据生成对应页面 ...

if __name__ == '__main__':
    generate_static_files()
    print("静态文件生成完成，输出到public目录")