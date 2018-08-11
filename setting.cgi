###################### 設定 ######################
use strict;
use utf8;

package set;

## ●種族リスト
 # ['ソート順' , '名前' , '種族特徴' , '6Lv追加特徴' ,'11Lv追加特徴' ,'16Lv追加特徴']
   our @races = (
     ['001', '人間', '［剣の加護／運命変転］'],
     ['002', 'エルフ', '［暗視］［剣の加護／優しき水］'],
     ['003', 'ドワーフ', '［暗視］［剣の加護／炎身］'],
     ['004', 'タビット', '［第六感］'],
     ['005', 'ルーンフォーク', '［暗視］［HP変換］'],
     ['006', 'ナイトメア（人間）', '［異貌］［弱点／土］'],
     ['006', 'ナイトメア（エルフ）', '［異貌］［弱点／水・氷］'],
     ['006', 'ナイトメア（ドワーフ）', '［異貌］［弱点／炎］'],
     ['006', 'ナイトメア（リルドラケン）', '［異貌］［弱点／風］'],
     ['007', 'リルドラケン', '［鱗の皮膚］［尻尾が武器］［剣の加護／風の翼］'],
     ['008', 'グラスランナー', '［マナ不干渉］［虫や植物との意思疎通］'],
     ['009', 'シャドウ', '［暗視］［月光の守り］'],
     ['010', 'フィー', '［妖精の加護］［浮遊］'],
     ['011', 'フロウライト', '［魂の輝き］［鉱石の生命］［晶石の身体］'],
     ['012', 'ハイマン', '［魔法の申し子］［デジャヴ］'],
     ['013', 'ミアキス', '［暗視］［猫変化］［獣性の発露］'],
     ['014', 'ヴァルキリー', '［戦乙女の光羽］［戦乙女の祝福］'],
     ['015', 'ソレイユ', '［輝く肉体］［太陽の再生］［太陽の子］'],
     ['016', 'レプラカーン', '［暗視］［見えざる手］［姿なき職人］'],
     ['017', 'センティアン（ルミエル）',   '［刻まれし聖印］［神の恩寵］［神の御名と共に］'],
     ['017', 'センティアン（イグニス）',   '［刻まれし聖印］［暗視］［神の兵士］［神への礼賛］'],
     ['017', 'センティアン（カルディア）', '［刻まれし聖印］［神の庇護］［神への祈り］'],
     ['018', 'ノーブルエルフ', '［暗視］［剣の加護／水の申し子］［カリスマ］［痛みに弱い］'],
     ['019', 'マナフレア', '［溢れるマナ］［マナの手］'],
     ['101', '魔動天使', '［暗視］［造られし強さ］［鋼鉄の翼］［契約の絆］'],
     ['a01', 'ダークドワーフ', '［暗視］［黒炎の遣い手］'],
     ['b01', 'ドレイク（ナイト）', '［暗視］［魔剣の所持］［飛行（飛翔）］［竜化］'],
     ['b02', 'ドレイク（ブロークン）', '［暗視］［限定竜化］'],
     ['b03', 'バジリスク', '［邪視と瞳石］［猛毒の血液］［魔物化］'],
     ['b04', 'リザードマン', '［尻尾が武器］［水中活動］［無呼吸活動］', ['［仲間との連携］','［敵への憤怒］'], ['［仲間との連携］','［敵への憤怒］'], ['［仲間との連携］','［敵への憤怒］'] ],
     ['b05', 'ケンタウロス', '［半馬半人］［馬人の武術］'],
     ['b06', 'ダークトロール', '［暗視］［弱体化］［トロールの体躯］' , '', '［限定再生］'],
     ['b07', 'ラミア', '［暗視］［ラミアの身体］［ラミアの吸血］［変化］'],
     ['b08', 'ライカンスロープ', '［暗視］［獣人の力］［獣化］'],
     ['b09', 'コボルド', '［種の限界］［軽視］［小さな匠］'],
     ['b10', 'ウィークリング（ガルーダ）', '［蛮族の身体］［未熟な翼］［切り裂く風］'],
     ['b10', 'ウィークリング（バジリスク）', '［蛮族の身体］［石化の視線］［毒の血液］'],
     ['b10', 'ウィークリング（マーマン）', '［蛮族の身体］［水中適性］［水・氷耐性］', '［バブルフォーム］'],
     ['b10', 'ウィークリング（ミノタウロス）', '［蛮族の身体］［暗視］［剛力］'],
     ['b11', 'ラルヴァ', '［暗視］［吸血の祝福］［忌むべき血］［弱体化］'],
     ['b12', 'バルカン', '［暗視］［炎無効］［バルカンの宝石］', '［強制召喚］'],
   );

## ●種族ごとの言語
 # '種族名' => [
 #   [ '言語名' , 会話, 読文 ], 習得＝1　会話／読文なし＝0　未習得＝2
 # ],
   our %race_la = (
     '人間' => [
       [ '交易共通語', 1, 1 ],
     ],
     'エルフ' => [
       [ '交易共通語', 1, 1 ],
       [ 'エルフ語', 1, 1 ],
     ],
     'ドワーフ' => [
       [ '交易共通語', 1, 1 ],
       [ 'ドワーフ語', 1, 1 ],
     ],
     'タビット' => [
       [ '交易共通語', 1, 1 ],
       [ '神紀文明語', 0, 1 ],
     ],
     'ルーンフォーク' => [
       [ '交易共通語', 1, 1 ],
       [ '魔動機文明語', 1, 1 ],
     ],
     'ナイトメア（人間）' => [
       [ '交易共通語', 1, 1 ],
     ],
     'ナイトメア（エルフ）' => [
       [ '交易共通語', 1, 1 ],
       [ 'エルフ語', 1, 1 ],
     ],
     'ナイトメア（ドワーフ）' => [
       [ '交易共通語', 1, 1 ],
       [ 'ドワーフ語', 1, 1 ],
     ],
     'ナイトメア（リルドラケン）' => [
       [ '交易共通語', 1, 1 ],
       [ 'ドラゴン語', 1, 0 ],
     ],
     'リルドラケン' => [
       [ '交易共通語', 1, 1 ],
       [ 'ドラゴン語', 1, 0 ],
     ],
     'グラスランナー' => [
       [ '交易共通語', 1, 1 ],
       [ 'グラスランナー語', 1, 1 ],
     ],
     'シャドウ' => [
       [ '交易共通語', 1, 1 ],
       [ 'シャドウ語', 1, 1 ],
     ],
     'フィー' => [
       [ '交易共通語', 1, 1 ],
       [ '妖精語', 1, 0 ],
     ],
     'フロウライト' => [
       [ '交易共通語', 1, 1 ],
     ],
     'ハイマン' => [
       [ '交易共通語', 1, 1 ],
       [ '魔法文明語', 1, 1 ],
     ],
     'ミアキス' => [
       [ '交易共通語', 1, 1 ],
       [ 'ミアキス語', 1, 0 ],
     ],
     'ヴァルキリー' => [
       [ '交易共通語', 1, 1 ],
     ],
     'ソレイユ' => [
       [ '交易共通語', 1, 2 ],
       [ 'ソレイユ語', 1, 0 ],
     ],
     'レプラカーン' => [
       [ '交易共通語', 1, 1 ],
       [ '魔動機文明語', 1, 1 ],
     ],
     'センティアン（ルミエル）' => [
       [ '神紀文明語', 0, 1 ],
     ],
     'センティアン（イグニス）' => [
       [ '神紀文明語', 0, 1 ],
     ],
     'センティアン（カルディア）' => [
       [ '神紀文明語', 0, 1 ],
     ],
     'ノーブルエルフ' => [
       [ 'エルフ語', 1, 1 ],
       [ '魔法文明語', 1, 1 ],
     ],
     'マナフレア' => [
       [ '魔法文明語', 1, 1 ],
     ],
     '魔動天使' => [
       [ '交易共通語', 1, 1 ],
       [ '魔動機文明語', 1, 1 ],
     ],
     'ダークドワーフ' => [
       [ '交易共通語', 1, 1 ],
       [ 'ドワーフ語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
     ],
     'ドレイク（ナイト）' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
       [ 'ドレイク語', 1, 1 ],
     ],
     'ドレイク（ブロークン）' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
       [ 'ドレイク語', 1, 1 ],
     ],
     'バジリスク' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
       [ 'バジリスク語', 1, 1 ],
       [ 'ドレイク語', 1, 1 ],
       [ '妖魔語', 1, 0. ],
     ],
     'リザードマン' => [
       [ '汎用蛮族語', 1, 1 ],
       [ 'リザードマン語', 1, 1 ],
       [ 'ドラゴン語', 1, 0. ],
     ],
     'ケンタウロス' => [
       [ '汎用蛮族語', 1, 1 ],
       [ 'ケンタウロス語', 1, 1 ],
     ],
     'ダークトロール' => [
       [ '汎用蛮族語', 1, 1 ],
       [ '巨人語', 1, 1 ],
     ],
     'ラミア' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
       [ 'ドレイク語', 1, 1 ],
     ],
     'ライカンスロープ' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
       [ 'ライカンスロープ語', 1, 1 ],
     ],
     'ウィークリング（ガルーダ）' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
     ],
     'ウィークリング（バジリスク）' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
     ],
     'ウィークリング（マーマン）' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
     ],
     'ウィークリング（ミノタウロス）' => [
       [ '交易共通語', 1, 1 ],
       [ '汎用蛮族語', 1, 1 ],
     ],
     'ラルヴァ' => [
       [ '交易共通語', 1, 1 ],
     ],
     'バルカン' => [
       [ '汎用蛮族語', 1, 1 ],
       [ 'バルカン語', 1, 1 ],
     ],
   );

## ●神リスト
 # ['ID' , 'ソート順', '通称' , '名前'],
   our @gods = (
     ['始' , 'A-1-1', '始祖神'    , 'ライフォス'],
     ['陽' , 'A-1-2', '太陽神'    , 'ティダン'],
     ['精' , 'A-1-3', '妖精神'    , 'アステリア'],
     ['炎' , 'A-1-4', '炎武帝'    , 'グレンダール'],
     ['紡' , 'A-1-5', '紡糸の女神', 'エルピュセ'],
     ['貨' , 'A-1-6', '貨幣神'    , 'ガメル'],
     ['月' , 'A-2-1', '月神'      , 'シーン'],
     ['酒' , 'A-2-2', '酒幸神'    , 'サカロス'],
     ['騎' , 'A-2-3', '騎士神'    , 'ザイア'],
     ['雨' , 'A-2-4', '慈雨神'    , 'フェトル'],
     ['裁' , 'A-3-5', '裁竜の魔女', 'ニコラ'],
     ['韋' , 'A-3-1', '韋駄天'    , 'ラトクレス'],
     ['制' , 'A-3-2', '制裁の双子女神', 'ヴィルトルード＆オイゲーニア'],
     ['共' , 'A-3-3', '共生神'    , 'ルイファ'],
     ['竜' , 'A-3-4', '竜帝神'    , 'シムルグ'],
     ['伝' , 'A-3-5', '伝達神'    , 'レータン'],
     ['剣' , 'A-3-6', '剣神'      , 'ヒューレ'],
     ['潮' , 'A-3-7', '潮の女神'  , 'マール'],
     ['牧' , 'A-3-8', '牧畜神'    , 'ジャージュ'],
     ['水' , 'A-3-9', '水の神'    , 'ルーフェリア'],
     ['融' , 'A-3-a', '融合神'    , 'リルズ'],
     ['槌' , 'A-3-b', '鉄槌神'    , 'エセルフィン'],
     
     ['賢' , 'B-1-1', '賢神'      , 'キルヒア'],
     ['勝' , 'B-1-2', '戦勝神'    , 'ユリスカロア'],
     ['秘' , 'B-2-1', '秘隠神'    , 'クス'],
     ['纏' , 'B-3-1', '纏いの神'  , 'ニールダ'],
     ['学' , '1-3-2', '学護神'    , 'エッケザッカ'],
     ['器' , 'A-3-3', '器械神'    , 'レパラール'],
     ['刃' , 'B-3-4', '刃神'      , 'マキシム'],
     
     ['戦' , 'C-1-1', '戦神'      , 'ダルクレム'],
     ['死' , 'C-1-2', '死の神'    , 'ザールギアス'],
     ['惑' , 'C-1-3', '惑いと偽りの神', 'ソーンダーク'],
     ['腐' , 'C-2-1', '腐敗の女神', 'ブラグザバス'],
     ['風' , 'C-2-2', '風来神'    , 'ル＝ロウド'],
     ['不' , 'C-2-3', '不死神'    , 'メティシエ'],
     ['眠' , 'C-2-4', '眠りの神'  , 'カオルルウプテ'],
     ['蛇' , 'C-2-5', '不和神'    , 'ニディスニオ'],
     ['謀' , 'C-2-6', '策謀神'    , 'ワギル＝イシナニ'],
     ['霧' , 'C-2-7', '霧闇神'    , 'フラクシス'],
     ['吸' , 'C-3-1', '吸生神'    , 'キュリアドラル'],
     ['蹂' , 'C-3-1', '蹂躙の戦乙女', 'イズマイア'],
     ['海' , 'C-3-1', '海風の神'  , 'ヴァ＝セアン'],
     ['宥' , 'C-3-2', '宥和神'    , 'アーメス'],
     ['毒' , 'C-3-3', '毒薬の神'  , 'テメリオ'],
     ['邪' , 'C-3-4', '邪妖の女神', 'ネアン'],
     ['狂' , 'E-0-0', '狂神'      , 'ラーリス'],
     ['他' , 'X-9-9', ''   , 'その他の神'],
   );

## ●流派設定
 # ['流派名' ,
 #  入門に必要な名誉点,
 #         ['秘伝1',必要名誉点, ['基礎特技','前提'] ],
 #         ['秘伝2',必要名誉点, ['基礎特技','前提1','前提2','前提3..と追加可'] ],
 #         #以後、秘伝3、4..と追加可
 # ],
 # 前提に出来るのは「戦闘特技」「秘伝」「練技」「呪歌」「騎芸」「賦術」「鼓咆」「占瞳」のみです。
 # また、['label', '○○'], とすることでセレクトボックス内の見出しに出来る
  our @mysteries = (
   # フェイダン流派
     ['label', 'フェイダン流派'],
     ['アードリアン流古武道・メルキアノ道場' ,
        50, ['飛空投げ',              20, ['投げ攻撃'] ],
            ['転がしテイルスイング',  20, ['テイルスイング'] ],
            ['大転がしテイルスイング',30, ['テイルスイング','飛空投げ','転がしテイルスイング'] ],
     ],
     ['アゴウ重鎚破闘術' ,
        50, ['重破・骨喰み', 20, ['全力攻撃Ⅰ'] ],
            ['轟破・地断ち', 30, ['全力攻撃Ⅱ','重破・骨喰み'] ],
            ['爆破・神鳴り', 50, ['全力攻撃Ⅲ','轟破・地断ち'] ],
            ['禍津・罪打ち', 20, ['魔力撃'] ],
     ],
     ['イーリー流幻闘道化術' ,
        50, ['錯誤の剣', 20, ['挑発攻撃Ⅰ'] ],
            ['誤認の剣', 30, ['挑発攻撃Ⅱ'] ],
            ['誘いの舞', 20, ['かばうⅠ'] ],
     ],
     ['エルエレナ惑乱操布術' ,
        50, ['見えざる敵に苛立て',     20, ['挑発攻撃Ⅰ'] ],
            ['見えざる敵に苛立て・承', 30, ['挑発攻撃Ⅱ','見えざる敵に苛立て'] ],
            ['迫る刃に怯えよ',         20, ['必殺攻撃Ⅰ'] ],
            ['迫る刃に怯えよ・承',     30, ['必殺攻撃Ⅱ','迫る刃に怯えよ２'] ],
            ['美しき舞に惑え',         20, ['牽制攻撃Ⅰ'] ],
            ['美しき舞に惑え・承',     30, ['牽制攻撃Ⅱ','回避行動Ⅰ','美しき舞に惑え'] ],
            ['美しき舞に惑え・極',     50, ['牽制攻撃Ⅲ','回避行動Ⅱ','ディフェンススタンス','美しき舞に惑え・承'] ],
     ],
     ['岩流斧闘術アズグラック派' ,
        50, ['破岩',     20, ['全力攻撃Ⅰ'] ],
            ['破岩滅砕', 30, ['全力攻撃Ⅱ','破岩'] ],
            ['岩斬',     20, ['必殺攻撃Ⅰ'] ],
            ['岩斬両断', 30, ['必殺攻撃Ⅱ','岩斬'] ],
     ],
     ['ギルヴァン流愚人剣' ,
        50, ['愚剣',     20, ['牽制攻撃Ⅰ'] ],
            ['愚挙理剣', 30, ['牽制攻撃Ⅱ','愚剣'] ],
            ['愚究極剣', 50, ['牽制攻撃Ⅲ','愚挙理剣'] ],
     ],
     ['ドーザコット潜弓道' ,
        50, ['不可知の矢・松籟', 20, ['牽制攻撃Ⅰ'] ],
            ['貫穿の矢・野分',   20, ['必殺攻撃Ⅰ'] ],
            ['致命の二矢・雪颪', 20, ['影矢'] ],
     ],
     ['ネレホーサ舞剣術' ,
        50, ['直歩直突', 20, ['牽制攻撃Ⅰ'] ],
            ['流足直突', 30, ['牽制攻撃Ⅱ','直歩直突'] ],
            ['踊踏直突', 50, ['牽制攻撃Ⅲ','流足直突'] ],
            ['舞剣虚撃', 20, ['挑発攻撃Ⅰ'] ],
            ['舞剣幻打', 30, ['挑発攻撃Ⅱ','舞剣虚撃'] ],
     ],
     ['マルガ＝ハーリ天地銃剣術' ,
        50, ['天誘地斬の極み', 30, ['マルチアクション'] ],
            ['地援天破の極み', 30, ['マルチアクション'] ],
            ['天地鳴乱の極み', 30, ['マルチアクション'] ],
     ],
     ['ライロック魔刃術' ,
        50, ['魔光壁',     20, ['魔力撃'] ],
            ['呪陰刃',     20, ['魔力撃'] ],
            ['光陰魔刃術', 20, ['マルチアクション'] ],
     ],
     ['リシバル集団運槍術' ,
        50, ['雷速鶴嘴貫', 20, ['全力攻撃Ⅰ'] ],
            ['横転蛸足絡', 20, ['薙ぎ払いⅠ'] ],
            ['大転象鼻旋', 30, ['薙ぎ払いⅡ','横転蛸足絡'] ],
            ['崩衡鰐尾撃', 20, ['牽制攻撃Ⅰ'] ],
     ],
     ['ルシェロイネ魔導術' ,
        50, ['ルシェロイネ魔導優越', 20, ['魔法拡大／確実化'] ],
            ['ルシェロイネ魔導稠密', 20, ['魔法拡大／範囲'] ],
            ['ルシェロイネ魔導集束', 20, ['魔法収束'] ],
     ],
   # ザルツ流派
     ['label', 'ザルツ流派'],
     ['エイントゥク十字弓道場',
        50, ['ニーショット',          20, ['','精密射撃'] ],
            ['ヘッドショット',        20, ['必殺攻撃Ⅰ'] ],
            ['ウェイティングショット',20, ['牽制攻撃Ⅰ'] ],
     ],
     ['カサドリス戦奏術' ,
        50, ['線上を歩く者',        30, [''] ],
            ['言の葉は破れ散る',    30, [''] ],
            ['我、今日に生きはせず',30, ['マルチアクション'] ],
            ['我が魔琴は静に咽ぶ',  30, ['マルチアクション'] ],
     ],
     ['クウェラン闇弓術改式' ,
        50, ['闇之壱・虚心穿',   20, ['必殺攻撃Ⅰ'] ],
            ['闇之弐・凶運命',   20, ['','精密射撃','狙撃'] ],
            ['闇之番外・三首蛟', 20, ['影矢'] ],
     ],
     ['クラウゼ流一刀覇王剣',
       150, [ '覇王・渦突剣', 20, ['必殺攻撃Ⅰ','武器習熟A／ソード'] ],
            [ '覇王・剛斬剣', 20, ['全力攻撃Ⅰ','武器習熟A／ソード'] ],
            [ '覇王・輝斬剣', 20, ['全力攻撃Ⅱ','覇王・剛斬剣','武器習熟S／ソード'] ],
            [ '覇王・煌斬剣', 50, ['全力攻撃Ⅲ','覇王・輝斬剣','武器の達人'] ],
     ],
     ['ジアンブリック攻盾法' ,
        50, ['選ばれし鋼の一打', 30, [''] ],
            ['完全なる鋼の一打', 50, ['','選ばれし鋼の一打'] ],
            ['打ち砕く鋼の進撃', 50, ['全力攻撃Ⅰ','選ばれし鋼の一打'] ],
     ],
     ['タマフ＝ダツエ流浪戦瞳' ,
        50, ['戦瞳：皇帝',        20, ['マルチアクション'] ],
            ['戦瞳：節制',        30, [''] ],
            ['戦瞳：吊るされた男',20, ['双占瞳'] ],
     ],
     ['ティルダンカル古代光魔党' ,
        50, ['ティルダンカル光魔再起', 20, ['魔法拡大／確実化'] ],
            ['ティルダンカル光魔稠密', 20, ['魔法拡大／範囲'] ],
            ['ティルダンカル光魔二条', 20, ['魔法収束','魔法拡大／数'] ],
     ],
     ['ハーデン鷹爪流投擲術',
        50, ['旋鷲', 20, ['','武器習熟A／投擲'] ],
            ['鋼鷹', 20, ['','武器習熟A／投擲'] ],
            ['凶烏', 20, ['影矢'] ],
     ],
     ['ファイラステン古流ヴィンド派（双剣の型）',
        50, [ '乱風・双手分撃', 30, [''] ],
            [ '衝風・捨身相殺', 30, [''] ],
            [ '連風・虎視伏竜', 30, [''] ],
     ],
     ['ファルネアス重装馬闘技' ,
        50, ['猛虎突撃の型', 20, ['全力攻撃Ⅰ','チャージ'] ],
            ['巨像守護の型', 20, ['かばうⅠ','騎獣の献身'] ],
            ['獣王乱舞の型', 20, ['挑発攻撃Ⅰ','八面六臂'] ],
            ['獣王乱撃の型', 30, ['挑発攻撃Ⅱ','八面六臂','獣王乱舞の型'] ],
     ],
     ['ベネディクト流紳士杖道',
        50, ['慈悲深き紳士の心',     20, ['挑発攻撃Ⅰ'] ],
            ['紳士による別れの挨拶', 30, [''] ],
            ['絶えざる紳士の微笑み', 20, ['薙ぎ払いⅠ','紳士による別れの挨拶'] ],
            ['分け隔てない紳士の愛', 50, ['薙ぎ払いⅡ','紳士による別れの挨拶','絶えざる紳士の微笑み'] ],
     ],
     ['ルキスラ銀鱗隊護警術',
        70, ['銀鱗の誓い', 20, ['かばうⅠ'] ],
            ['銀鱗の矜持', 30, ['かばうⅠ','銀鱗の誓い'] ],
            ['銀鱗の魂',   30, ['かばうⅠ','銀鱗の誓い'] ],
     ],
   # ユーレリア流派
     ['label', 'ユーレリア流派'],
     ['ヴァルト式戦場剣殺法' ,
        50, ['殺し打ち・轟雷',     20, ['全力攻撃Ⅰ'] ],
            ['殺し打ち・轟震万雷', 30, ['全力攻撃Ⅱ','殺し打ち・轟雷'] ],
            ['殺し打ち・電光',     50, ['必殺攻撃Ⅰ'] ],
     ],
     ['ドバルス螺旋運手' ,
        50, ['序伝・螺旋開花の型',     30, [''] ],
            ['本伝の一・螺旋結実の型', 20, ['','かいくぐり'] ],
            ['本伝の二・螺旋散種の型', 20, ['','両手利き'] ],
     ],
     ['ガオン無双獣投術' ,
        50, ['巨獣頭槌', 20, ['投げ攻撃','投げ強化Ⅰ'] ],
            ['撃爆投獣', 20, ['投げ攻撃','投げ強化Ⅰ'] ],
            ['猛進獣殺', 20, ['','カウンター','投げ強化Ⅰ'] ],
     ],
     ['ニルデスト流実戦殺法' ,
       -30, ['口汚い挑発',     -20, ['挑発攻撃Ⅰ'] ],
            ['卑劣な目つぶし', -20, ['鎧貫き'] ],
            ['狡猾な誤導',     -20, ['牽制攻撃Ⅰ'] ],
     ],
     ['オーロンセシーレ中隊軽装突撃術' ,
        50, ['小獣角突', 20, ['必殺攻撃Ⅰ'] ],
            ['小竜咬砕', 20, ['全力攻撃Ⅰ'] ],
            ['小王完武', 30, ['','小獣角突','小竜咬砕'] ],
     ],
     ['ラステンルフト双盾護身術' ,
        50, ['風雨に耐える柳樹の構え', 20, ['ディフェンススタンス'] ],
            ['重圧に折れぬ笹竹の構え', 30, [''] ],
            ['猪突を戒める荊枝の構え', 30, [''] ],
     ],
     ['ホプレッテン機動重弩弓法' ,
        50, ['ホプレッテン機動術',     20, ['','武器習熟A／クロスボウ'] ],
            ['ホプレッテン伏射術',     20, ['牽制攻撃Ⅰ'] ],
            ['ホプレッテン機動射撃術', 30, ['','ホプレッテン機動術'] ],
     ],
     ['エイスンアデアル召喚術' ,
        50, ['理外の理を顕す',   20, ['マリオネット'] ],
            ['異界のものを諭す', 20, ['魔法拡大／確実化'] ],
            ['主従の連携を示す', 20, ['ディフェンススタンス'] ],
     ],
     ['眠り猫流擬態術' ,
        50, ['猫の着地', 30, [''] ],
            ['猫の隠密', 30, [''] ],
            ['猫の心',   50, ['','猫の隠密'] ],
     ],
     ['カンフォーラ博物学派' ,
        50, ['本草の知識', 30, [''] ],
            ['抽出の知識', 30, [''] ],
            ['採取の知識', 30, [''] ],
     ],
  # ダグニア流派
    ['label', 'ダグニア流派'],
    ['聖戦士ローガン鉄壁の型',
      50, [ '不倒なる守りの構え',   20, ['ディフェンススタンス'] ],
          [ '不屈なる庇護の意思',   20, ['かばうⅠ'] ],
          [ '不屈なる庇護の意思Ⅱ', 30, ['かばうⅡ'] ],
          [ '不屈なる庇護の意思Ⅲ', 50, ['かばうⅢ'] ],
          [ '不敵なる攻守の構え',   20, ['マルチアクション'] ],
    ],
    ['不死者討滅武技バニシングデス',
      50, [ 'キュア＆デストロイ',   20, ['魔法拡大／威力確実化'] ],
          [ 'エナジー＆ストライク', 20, ['魔力撃'] ],
          [ 'センス＆バニッシュ',   30, [''] ],
    ],
    ['ダルボン流下克戦闘術',
      50, [ '下克・草伏せ',   30, ['牽制攻撃Ⅰ'] ],
          [ '下克・蛙跳び',   20, ['牽制攻撃Ⅰ','必殺攻撃Ⅰ'] ],
          [ '下克・蛙跳びⅡ', 20, ['牽制攻撃Ⅰ','必殺攻撃Ⅱ'] ],
          [ '下克・蛙跳びⅢ', 20, ['牽制攻撃Ⅰ','必殺攻撃Ⅲ'] ],
          [ '下克・踵砕き',   20, ['牽制攻撃Ⅰ','全力攻撃Ⅰ'] ],
          [ '下克・踵砕きⅡ', 20, ['牽制攻撃Ⅰ','全力攻撃Ⅱ'] ],
    ],
    ['ヴェルクンスト砦建築一党',
      50, [ 'ブロウインパクト', 20, ['全力攻撃Ⅰ'] ],
          [ 'ガードインパクト', 20, ['かばうⅠ'] ],
          [ 'レベルインパクト', 20, ['薙ぎ払いⅠ'] ],
    ],
    ['神速確勝ボルンの精髄',
      50, [ '神眼ボルンの見切り',   20, ['牽制攻撃Ⅰ'] ],
          [ '神眼ボルンの見切りⅡ', 30, ['牽制攻撃Ⅱ'] ],
          [ '神眼ボルンの見切りⅢ', 50, ['牽制攻撃Ⅲ'] ],
          [ '神技ボルンの捌き',     20, ['必殺攻撃Ⅰ'] ],
          [ '神技ボルンの捌きⅡ',   20, ['必殺攻撃Ⅱ'] ],
          [ '神技ボルンの捌きⅢ',   20, ['必殺攻撃Ⅲ'] ],
          [ '神舞ボルンの躱し',     30, [''] ],
    ],
    ['バルナッド英雄庭流派・討神舞踏剣',
      50, [ '討神舞踏剣奥義・胡蝶艶舞',   20, ['挑発攻撃Ⅰ'] ],
          [ '討神舞踏剣奥義・胡蝶艶舞Ⅱ', 30, ['挑発攻撃Ⅱ'] ],
          [ '討神舞踏剣奥義・紅水流舞',   20, ['全力攻撃Ⅰ'] ],
          [ '討神舞踏剣奥義・紅水流舞Ⅱ', 20, ['全力攻撃Ⅱ'] ],
          [ '討神舞踏剣奥義・紅水流舞Ⅲ', 20, ['全力攻撃Ⅲ'] ],
          [ '討神舞踏剣秘奥義・絶神嵐舞之極',   30, ['全力攻撃Ⅱ','挑発攻撃Ⅰ','バトルマスター'] ],
          [ '討神舞踏剣秘奥義・絶神嵐舞之極Ⅱ', 30, ['全力攻撃Ⅲ','挑発攻撃Ⅱ','バトルマスター'] ],
    ],
    ['森の吹き矢使いたち',
      50, [ 'ブロウガンの習熟A', 20, [''] ],
          [ 'ブロウガンの習熟S', 30, [''] ],
          [ 'ブロウガンのいなし', 20, ['射手の体術'] ],
    ],
  # ミストグレイヴ流派
    ['label', 'ミストグレイヴ流派'],
    ['ソソ破皇戦槌術',
      50, [ '破皇の構え「不動」', 20, ['全力攻撃Ⅰ'] ],
          [ '破皇の構え「泰山」', 20, ['必殺攻撃Ⅰ'] ],
          [ '破皇の構え「虎伏」', 20, ['かばうⅠ','頑強'] ],
    ],
    ['バルカン流召精術',
      50, [ 'バルカン流召精・六精断裂', 20, ['魔法拡大／数'] ],
          [ 'バルカン流召精・六精魔纏', 20, ['魔力撃'] ],
          [ 'バルカン流召精・六精縮退', 20, ['魔法収束'] ],
    ],
    ['ジーズドルフ騎竜術',
      50, [ 'ストームライド',         20, ['','騎獣の献身'] ],
          [ 'テンペストダイヴ',       20, ['魔力撃',''] ],
          [ 'タービュランスマジック', 20, ['魔法拡大／数'] ],
    ],
  );

## ●種族によって必要名誉点が変わる流派の設定
 # '流派名' => [ 入門に必要な名誉点, '該当種族' ],  #該当種族が複数の場合 '種族A、種族B、' ……という感じで
  our %mys_race = (
    '岩流斧闘術アズグラック派' => [ 40, 'ドワーフ' ],
    'クウェラン闇弓術改式'     => [ 40, 'シャドウ' ],
#    '' => [ 40, ''],
  );

1;