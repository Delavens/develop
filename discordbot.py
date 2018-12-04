import discord # インストールした discord.py
import random

client = discord.Client() # 接続に使用するオブジェクト
#locaton = ['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']

# 起動時に通知してくれる処理tests
@client.event
async def on_ready():
    print('Fortnite Location Ready')

# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('!flocation'):
        await client.send_message(message.channel, random.choice(['ジャンク・ジャンクション', 'ホーンテッド・ヒルズ', 'プレザント・パーク', 'スノビー・ショア', 'バイキング・ビレッジ', 'ティルテッド・タワー', 'グリーシー・グローブ', 'シフティ・シャフト', 'レイジー・リンクス', 'トマト・テンプル', 'リスキー・リールズ', 'ウェイリング・ウッズ', 'ダスティ・ディポット', 'ソルティ・スプリングス', 'フェイタル・フィールド', 'リテイル・ロー', 'フラッシュ・ファクトリー', 'ラッキー・ランディング', 'パラダイス・パームズ', 'レイジーリンクスの西のモーテル', 'ティルテッドタワー西のおいしめの土地', 'フラッシュファクトリー北東のおいしめの土地', 'ロンリー・ロッジ', 'サーキット', '砂漠南のおいしめの土地', 'コンテナのとこ']))

    if message.content.startswith('!team'):
        await client.send_message(message.channel, discord.Channel().name)
        

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTE5NTU0NDUzODM0MTcwMzk0.DuhAjg.5yDotuamRFXDJQ2e19twGhIJKsE')
