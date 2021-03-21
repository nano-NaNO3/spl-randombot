import discord
import random
TOKEN = 'ここにbotのトークンを入力'
client = discord.Client()
#ブキ種別リスト
shooter2 = [
    'ボールドマーカー', 'ボールドマーカーネオ', 'ボールドマーカー7', 'わかばシューター', 'もみじシューター', 'おちばシューター',
    'シャープマーカー', 'シャープマーカーネオ', 'プロモデラーMG(銀)', 'プロモデラーRG(金)', 'プロモデラーPG(銅)', 'スプラシューター', 'スプラシューターコラボ', 'スプラシューターベッチュー',
    '.52ガロン', '.52ガロンデコ', '.52ガロンベッチュー', 'N-ZAP85(黒)', 'N-ZAP89(赤)', 'N-ZAP83(ファミザップ)', 'プライムシューター', 'プライムシューターコラボ', 'プライムシューターベッチュー',
    '.96ガロン', '.96ガロンデコ', 'ジェットスイーパー', 'ジェットスイーパーカスタム',
    'L3リールガン', 'L3リールガンD', 'L3リールガンベッチュー', 'H3リールガン', 'H3リールガンD', 'H3リールガンチェリー', 'ボトルガイザー', 'ボトルガイザーフォイル'
]
blaster2 = [
    'ホットブラスター', 'ホットブラスターカスタム', 'ロングブラスター', 'ロングブラスターカスタム', 'ロングブラスターネクロ',
    'ラピッドブラスター', 'ラピッドブラスターデコ', 'ラピッドブラスターベッチュー', 'Rブラスターエリート', 'Rブラスターエリートデコ',
    'ノヴァブラスター', 'ノヴァブラスターネオ', 'ノヴァブラスターベッチュー', 'クラッシュブラスター', 'クラッシュブラスターネオ'
]
roller2 = [
    'スプラローラー', 'スプラローラーコラボ', 'スプラローラーベッチュー', 'カーボンローラー', 'カーボンローラーデコ', 'ヴァリアブルローラー', 'ヴァリアブルローラーフォイル',
    'ダイナモローラー', 'ダイナモローラーテスラ', 'ダイナモローラーベッチュー',
]
fude2 = [
    'パブロ', 'パブロ・ヒュー', 'パーマネント・パブロ', 'ホクサイ', 'ホクサイヒュー', 'ホクサイベッチュー'
]
charger2 = [
    'スプラチャージャー', 'スプラスコープ', 'スプラチャージャーコラボ', 'スプラスコープコラボ', 'スプラチャージャーベッチュー', 'スプラスコープベッチュー',
    'リッター4K', '4Kスコープ', 'リッター4Kカスタム', '4Kスコープカスタム', 'ソイチューバー', 'ソイチューバーカスタム', 'スクイックリンα', 'スクイックリンβ', 'スクイックリンγ',
    '14式竹筒銃・甲', '14式竹筒銃・乙', '14式竹筒銃・丙'
]
spinner2 = [
    'バレルスピナー', 'バレルスピナーデコ', 'バレルスピナーリミックス', 'スプラスピナー', 'スプラスピナーコラボ', 'スプラスピナーベッチュー', 'ハイドラント', 'ハイドラントカスタム',
    'クーゲルシュライバー', 'クーゲルシュライバー・ヒュー', 'ノーチラス47', 'ノーチラス79'
]
slocher2 = [
    'バケットスロッシャー', 'バケットスロッシャーデコ', 'バケットスロッシャーソーダ', 'ヒッセン', 'ヒッセン・ヒュー',
    'スクリュースロッシャー', 'スクリュースロッシャーネオ', 'スクリュースロッシャーベッチュー',
    'オーバーフロッシャー', 'オーバーフロッシャーデコ', 'エクスプロッシャー', 'エクスプロッシャーカスタム'
]
maneuver2 = [
    'スプラマニューバー', 'スプラマニューバーコラボ', 'スプラマニューバーベッチュー', 'スパッタリー', 'スパッタリー・ヒュー', 'スパッタリークリア', 'デュアルスイーパー', 'デュアルスイーパーカスタム',
    'ケルビン525', 'ケルビン525デコ', 'ケルビン525ベッチュー', 'クアッドホッパーブラック', 'クアッドホッパーホワイト'
]
shelter2 = [
    'パラシェルター', 'パラシェルターソレーラ', 'キャンピングシェルター', 'キャンピングシェルターソレーラ', 'キャンピングシェルターカーモ',
    'スパイガジェット', 'スパイガジェットソレーラ', 'スパイガジェットベッチュー'
]
spl2_weapons0 = [shooter2, blaster2, roller2, fude2, charger2, spinner2, slocher2, maneuver2, shelter2]
spl2_weapons = []
for i in spl2_weapons0:
    for j in i:
        spl2_weapons.append(j)




@client.event
async def on_ready():
    print("ログインしました")

class Buki:
    def __init__(self, weapons):
        self.weapons = weapons

    #ブキランダム関数
    def buki_random(self):
        random.shuffle(self.weapons)
        return self.weapons
    
    #ランダム処理後、返信メッセージをreturn
    def buki_random_msg(self, members, author, name0):
        msg = ''
        print('def')
        print(members)
        print(author)
        if author in members:
            print(members)
            print(1)
            #ボイスチャンネル参加者それぞれにブキランダム
            for name in members:
                #引数にスプラ2のブキリスト
                random.shuffle(self.weapons)
                #ランダム結果のメッセージ
                msg += name + ' >> ' +  self.weapons[0] + '\n'
            return msg
        else:
            random.shuffle(self.weapons)
            #送信者の名前
            print(members)
            print(2)
            msg = str(author) + ' >> ' +  self.weapons[0]
            return msg

@client.event
async def on_message(message):
    #送信者がbotの場合は弾く
    if message.author.bot:
        return
    #VC参加者のリストを取得する
    try:
        memberslist = [member.name for member in message.author.voice.channel.members]
        print(memberslist)
    #ボイスチャンネル参加者なしの場合エラーになるので
    except AttributeError:
        print('0 people in VC >> pass')

    #メッセージの本文が'/weapon2'の時⇒スプラ2でブキランダム
    if message.content == '/weapon2':
        buki = Buki(spl2_weapons)
        print(memberslist)
        msg = buki.buki_random_msg(memberslist, message.author.name, message.author)
        await message.channel.send(msg)

    elif message.content == '/spinner2':
        buki = Buki(spinner2)
        msg = buki.buki_random_msg(memberslist, message.author.name, message.author)
        await message.channel.send(msg)

    elif message.content == '/how':
        howtouse = '''\
        ★
        ●ブキランダム(全ブキ対象)
        コマンド　⇒　/weapon2
        ・ボイスチャンネル参加者がコマンドを送信
        ⇒ボイスチャンネル参加者全員を対象にブキランダムを行なう
        
        ・ボイスチャンネル未参加者がコマンドを送信
        ⇒送信者のみを対象にブキランダム

        ●使い方
        コマンド　⇒　/how
        '''
        await message.channel.send(howtouse)
    '''
    if message.content == 'tx/weapon2':
        buki_random(spl2_weapons)
        #送信者の名前
        name = message.author.name
        msg = str(name) + ' >> ' +  spl2_weapons[0][0]
        await message.channel.send(msg)
        '''
client.run(TOKEN)
'''
≪追加予定≫
・ブキ種ランダム
例.スピナーのみでブキランダム
・ルールランダム
エリア/ヤグラ/ホコ/アサリ/ナワバリでランダム
特定ルール除外機能付き
'''