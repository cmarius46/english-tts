from gtts import gTTS


with open('title.txt') as titleFile:
	title = titleFile.read()

	print('read title')

with open('text.txt') as textFile:
	text = textFile.read()

	print('read text')



tts_en = gTTS(title, lang='en', tld='co.uk') # co.uk # us
# tts_fr = gTTS('bonjour', lang='fr')

tts_en.save('title2.mp3')

# with open('title.mp3', 'wb') as f:
#     tts_en.write_to_fp(f)


print('done')

