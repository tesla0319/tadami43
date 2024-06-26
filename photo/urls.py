from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

# URLパターンを登録変数
urlpatterns = [
    # photoアプリへのアクセスは viewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    # 写真投稿ページへのアクセスは viewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),

    #　投稿完了ページへのアクセスは viewsモジュールのPostSuccessViewを実行
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),

    # カテゴリ一覧ページ
    # photos/<Categoryテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>', views.CategoryView.as_view(), name = 'photos_cat'),

    # ユーザーの投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>', views.UserView.as_view(), name = 'user_list'),

    # 詳細ページ
    # photo\detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk:id値(int)}としてDetailViewに渡される
    path('photo-detail/<int:pk>', views.DetailView.as_view(), name = 'photo_detail'),

    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    # 投稿写真の削除
    # photo/<Photo postsテーブルのid値>/detailにマッチング
    # <int:pk>は辞書{pk: id値(int)}としてPhotoDeleteViewに渡される
    path('photo/<int:pk>/detail/', views.PhotoDeleteView.as_view(), name ='photo_delete'),

    # 検索結果一覧ページ
    path('result_list/', views.ResultView.as_view(), name='result_list'),

#tuika
    path('photo/<int:pk>/nice/', views.count, name = 'nice_success'),
 
    path('mypage/', views.mypage_view, name='mypage_view'),

# ソート
    path('old/', views.AscView.as_view(), name='asc'),
    path('st/', views.NiceDescView.as_view(), name='nice_desc'),

   
]


 