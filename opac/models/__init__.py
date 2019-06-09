# -*- coding: utf-8 -*-


'''
### A. 必須仕様

1. jbisc.txt のデータをすべて取り込むこと
2. データベースに格納するフィールドは，NBC，ISBN，TR，PUB とする(done)
3. TR はタイトル (本タイトルやタイトル関連情報等) と著者 (責任表示) の 2 つのフィールドに分けて格納すること(done)
4. PUB は出版者 (出版地や出版者名) と出版年の 2 つのフィールドに分けて格納すること(done)
5. 検索語を入力する窓を一つ設定し，検索語を 1 語入れると，タイトルと責任表示を検索し，結果を返すこと
6. 結果には，データベースに格納したフィールドの全てを表示すること．表示は見やすいように配置し，色遣いも工夫すること

### B. 加点仕様 (中級)

1. NBC，ISBN，TR，PUB だけでなく，全てのフィールドをデータベースに格納すること(done)
2. 検索語を入力する窓に複数の語を入力し，検索が行えること
3. 全てのフィールドを同じ条件で検索する
ANY 検索，フィールドを個別に指定した検索の両方が行えること．
フィールドの指定はボタンによる切り替え，入力用の窓を別にするなど，複数の方法がある

### C. 加点仕様 (上級)

1. 検索結果一覧は一部のフィールドを用いた簡易表示として，
   検索結果の一つを選んでクリックすると，詳細表示画面を出し，すべてのフィールドを表示すること
2. 検索結果は 1 行につき 1 データとし，20 件ごとに表示すること．
   20 件を超えたら次ページに表示すること

'''


# FROM 一つ上のディレクトリ.カレントディレクトリ.対象ファイル import 対象ファイル内のクラス
# または
# FROM カレントディレクトリ import 対象ファイル

from opac.models.bibliography import BIBLIO
# NBC
# from opac.models.isbn import ISBN
# from opac.models.tr import TR
# ## RESPONSIBILITY: TR の外部キー
# from opac.models.responsibility import RESPONSIBILITY # 使用せず
# ED
# from opac.models.pub import PUB
# PHYS
# SERIES
# NOTE
# TITLEHEADING
# from opac.models.authorheading import AUTHORHEADING
# HOLDINGSRECORD
# HOLDINGPHYS
# HOLODINGLOC






