#  导入搜索引擎
from haystack import indexes
# 导入文章
from .models import Article

# 索引类   类名
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Article
    def index_queryset(self, using=None):
        # 在这里返回的内容为文章列表索引
        return self.get_model().objects.all()
