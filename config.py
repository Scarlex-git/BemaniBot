import re
serverSongQueue = {}

pageParser = re.compile(r'pa?ge?.?')

numberParser = re.compile(r'\d+')

url2 = "https://cdn.vox-cdn.com/thumbor/bqASZI3uKDGxAP3mTAX1TiGuuSg=/0x0:800x800/1200x0/filters:focal(0x0:800x800)/cdn.vox-cdn.com/uploads/chorus_asset/file/10838085/4head.jpg"

urls = {
        'SOUND VOLTEX BOOTH':'https://i.imgur.com/iuQDSqu.jpg',
        'SOUND VOLTEX II -infinite infection-':'https://i.imgur.com/qfQr5Yc.jpg',
        'SOUND VOLTEX III GRAVITY WARS':'https://i.imgur.com/rJfdDKU.png',
        'SOUND VOLTEX IV HEAVENLY HAVEN':'https://i.imgur.com/wz0SIvo.png',
        'SOUND VOLTEX VIVID WAVE':'https://i.imgur.com/poqcuPt.png'
        }

reToDifficulty = {
        'n':'novice',
        'a':'advanced',
        'e':'exhaust',
        'i':'infinite',
        'm':'maximum',
        'g':'gravity',
        'h':'heavenly',
        'v':'vivid'
        }

difficultyLevelToEmoji = {
        'novice':'🇳',
        'advanced':'🇦',
        'exhaust':'🇪',
        'infinite':'🇮',
        'maximum':'🇲',
        'gravity':'🇬',
        'heavenly':'🇭',
        'vivid':'🇻'
}

emojiToDifficultyLevel = {
        '🏘️':'general',
        '🇳':'novice',
        '🇦':'advanced',
        '🇪':'exhaust',
        '🇮':'infinite',
        '🇲':'maximum',
        '🇬':'gravity',
        '🇭':'heavenly',
        '🇻':'vivid'
        }

pageChangeDictionary = {
        '➡️':1,
        '⬅️':-1
        }
