import discord # インストールした discord.py
import random

client = discord.Client() # 接続に使用するオブジェクト
#locaton = ['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']

# 起動時に通知してくれる処理tests
@client.event
async def on_ready():
    print('Fortnite Location Ready')


@client.event
async def on_message(message):
    if message.content.startswith('!flocation'):
        await client.send_message(message.channel, random.choice(['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']))

    if message.content.startswith('!fteam'):
        c = client.get_channel('489330400032849940')
        t1 = client.get_channel('519678340232249344')
        t2 = client.get_channel('519678398214176789')
        mem = c.voice_members
<<<<<<< HEAD
        length = len(mem)
        teammem = -(- length // 2 )
=======
        length = -(- len(mem) // 2 )
>>>>>>> f88de1db83579afbd7162b9502965a9d49036615
        for x in mem:
            await client.send_message(message.channel, x.display_name)
            t1len = len(t1.voice_members)
            t2len = len(t2.voice_members)
<<<<<<< HEAD
            if t1len < teammem and t2len < teammem:
                client.move_member(x, random.choice([t1,t2]))
            elif t1 < teammem:
                client.move_member(x, t1)
            elif t2 < teammem:
=======
            if t1len < length and t2len < length:
                client.move_member(x, random.choice([t1,t2]))
            elif t1 < length:
                client.move_member(x, t1)
            elif t2 < length:
>>>>>>> f88de1db83579afbd7162b9502965a9d49036615
                client.move_member(x, t2)

    if message.content.startswith('!fgather'):
        c = client.get_channel('489330400032849940')
        t1 = client.get_channel('519678340232249344')
        t2 = client.get_channel('519678398214176789')
        t1mem = t1.voice_members
        for x in t1mem:
            client.move_member(x, c)
        t2mem = t2.voice_members
        for x in t2mem:
            client.move_member(x, c)

    if message.content.startswith('!fcommand'):
        if client.user == message.author:
            return
        await client.send_message(message.channel,'!flocation, !fteam, !fgather')


    if message.content.startswith('!fcommand'):
        if client.user == message.author:
            return
        await client.send_message(message.channel,'!flocation, !fteam, !fgather')




# botの接続と起動
<<<<<<< HEAD
=======
<<<<<<< HEAD
# （tokenにはbotアカウントのアクセストークンを入れてください）
=======
>>>>>>> f7b706c4d4f77770b6505fa571928d9a4e1dc683
>>>>>>> f88de1db83579afbd7162b9502965a9d49036615
client.run('NTE5NTU0NDUzODM0MTcwMzk0.DuhAjg.5yDotuamRFXDJQ2e19twGhIJKsE')
