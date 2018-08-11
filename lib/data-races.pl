#################### 種族 ####################
use strict;
use utf8;

package data;

# ['カテゴリ(常/宣/主)',習得できる最小Lv','名前',ナンバリングいくつまでか,'概要']
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
  ['007', 'リカント', '［暗視(獣変貌)］［獣変貌］'],
  ['008', 'リルドラケン', '［鱗の皮膚］［尻尾が武器］［剣の加護／風の翼］'],
  ['009', 'グラスランナー', '［マナ不干渉］［虫や植物との意思疎通］'],
  ['010', 'シャドウ', '［暗視］［月光の守り］'],
  ['011', 'フィー', '［妖精の加護］［浮遊］'],
  ['012', 'フロウライト', '［魂の輝き］［鉱石の生命］［晶石の身体］'],
  ['013', 'ハイマン', '［魔法の申し子］［デジャヴ］'],
  ['014', 'ミアキス', '［暗視］［猫変化］［獣性の発露］'],
  ['015', 'ヴァルキリー', '［戦乙女の光羽］［戦乙女の祝福］'],
  ['016', 'ソレイユ', '［輝く肉体］［太陽の再生］［太陽の子］'],
  ['017', 'レプラカーン', '［暗視］［見えざる手］［姿なき職人］'],
  ['017', 'センティアン（ルミエル）',   '［刻まれし聖印］［神の恩寵］［神の御名と共に］'],
  ['017', 'センティアン（イグニス）',   '［刻まれし聖印］［暗視］［神の兵士］［神への礼賛］'],
  ['018', 'センティアン（カルディア）', '［刻まれし聖印］［神の庇護］［神への祈り］'],
  ['101', 'ノーブルエルフ', '［暗視］［剣の加護／水の申し子］［カリスマ］［痛みに弱い］'],
  ['102', 'マナフレア', '［溢れるマナ］［マナの手］'],
  ['201', '魔動天使', '［暗視］［造られし強さ］［鋼鉄の翼］［契約の絆］'],
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

our @race_names;
our %race_ability;
foreach (@races){
  push (@race_names, @$_[1]);
  $race_ability{@$_[1]} = @$_[2];
}

## ●種族ごとの言語
 # '種族名' => [
 #   [ '言語名' , 会話, 読文 ], 習得＝1　会話／読文なし＝0　未習得＝2
 # ],
our %race_language = (
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
  'リカント' => [
    [ '交易共通語', 1, 1 ],
    [ 'リカント語', 1, 1 ],
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
    [ '交易共通語', 1, 1 ],
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

1;